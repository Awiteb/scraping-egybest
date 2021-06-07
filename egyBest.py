from colorama.initialise import reset_all
import requests
from bs4 import BeautifulSoup as bs4
from colorama import Fore


MAGENTA = Fore.MAGENTA
CYAN = Fore.CYAN
GREEN = Fore.GREEN
RESET = Fore.RESET
EGY_BEST_URL = "https://gose.egybest.bid"

class EgyBest():
    def __init__(self,search:bool):
        self.is_search = search
    
    @property
    def title(self):
        return self.__title
    @title.setter
    def title(self, title:str):
        soup, r = self.get_page_source(title)
        if r.status_code == 200:
            self.__title = title
            self.soup = soup
        else:
            raise Exception("Movie not found")
    def __convert_to_url(self, movie_name:str):
        movie_name = self.__edit_movie_name(movie_name)
        return f"{EGY_BEST_URL}/{'explore/?q=' if self.is_search else 'movie/'}{movie_name}"

    def __edit_movie_name(self,movie_name:str):
        return movie_name.replace('(', '').replace(')','').replace(' ', '-')
    def get_page_source(self, movie_name) -> 'BeautifulSoup':
        r = requests.get(self.__convert_to_url(movie_name))
        return bs4(r.content, 'html.parser'), r
    
    def search(self, text:str, amount=12) -> list:
        if self.is_search:
            source, _ = self.get_page_source(text)
            div_movies = source.find('div', id="movies", class_="movies")
            movies = div_movies.find_all('a', class_="movie")
            if len(movies) == 0:
                return None, div_movies.text
            else:
                movies_lst = [{"name":None if not movie.find('span', class_="title") else movie.find('span', class_="title").text,
                                    "img":None if not movie.find('img') else movie.find('img').get('src'), 
                                        "rating":None if not movie.find('span') else movie.find('span').text} 
                                            for movie in movies]
                return movies_lst[:amount], None
        else:
            return "The object is not a method enabled on search"
    def display_search(self, text:str) -> str:
        movies, err = self.search(text)
        if movies:
            return f"{GREEN}\n{'='*30}\n".join([f"{RESET}Name: {MAGENTA}{movie['name']}\n\
                                        \r{RESET}Img: {CYAN}{movie['img']}\n\
                                        \r{RESET}Rating: {CYAN}{movie['rating']}" for movie in movies])
        else:
            return err
    def get_movie(self, movie_name) -> dict:
        self.title = movie_name
        movie_details = self.__get_movie_table()
        movie_watch_url = self.__get_movie_watch_url()
        img_url = self.__get_img_url()
        trailer_url = self.__get_trailer_url()
        movie_story = self.__get_movie_story()
        movie_details.update(watch_url=movie_watch_url, img=img_url,
                                trailer_url=trailer_url, story=movie_story)
        return movie_details
    def __get_movie_table(self):
        movie_table = self.soup.find('table', class_="movieTable").find_all('tr')
        movie_name = movie_table.pop(0)
        switcher = {
            "اللغة • البلد":"language",
            "التصنيف":"genres",
            "النوع":"type",
            "التقييم":"evaluation",
            "المدة":"Duration",
            "الجودة":"quality",
            "الترجمة":"translation",
        }
        dict = {switcher.get(t.find('td').text):t.find_all('td')[1].text.replace('\xa0', '') for t in movie_table}
        dict.update({"name":movie_name.text})
        return dict
    def __get_movie_watch_url(self):
        return EGY_BEST_URL+str(self.soup.find('iframe', class_="auto-size").get('src'))
    def __get_img_url(self):
        return self.soup.find('div', class_="movie_img").find('img').get('src')
    def __get_trailer_url(self):
        return self.soup.find('div', class_="play p api").get('url')
    def __get_movie_story(self):
        try:
            story = self.soup.find_all('div', class_="pda")[3].text
        except:
            story = None
        return story