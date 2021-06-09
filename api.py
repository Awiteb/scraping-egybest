from flask import Flask, jsonify, request
from egyBest import EgyBest

app = Flask(__name__)
searcher = EgyBest(search=True)
movies_getattr = EgyBest(search=False)

# home
@app.route('/', methods=['GET',])
def index():
    return "Methods [getMovie, search]"

# getMovie
@app.route('/getMovie', methods=['GET',])
def get_movie():
    movie_name = request.args.get('movie_name')
    if movie_name:
        try:
            movie = movies_getattr.get_movie(movie_name)
            movie.update({'ok':True})
            return jsonify(movie)
        except Exception as err:
            return jsonify({"ok":False, "error":str(err)})
    else:
        return "Invalid request example: /getMovie?movie_name=<movie name here>"

# search
@app.route('/search', methods=['GET',])
def search():
    title = request.args.get('title')
    amount = request.args.get('amount')
    if all([title, amount]):
        try:
            result = searcher.search(title, amount=amount)
            print(result)
            result.update({'ok':True})
            return jsonify(result)
        except Exception as err:
            return jsonify({"ok":False, "error":str(err)})
    else:
        return "Invalid request example: /search?title=[you want search for]&amount=[amount of result (max is 12)]"

if __name__ == '__main__':
    app.run(debug=True)