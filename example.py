from egyBest import EgyBest

# make search object
searcher = EgyBest(search=True)

# search in egy best
print(searcher.search("fast", amount=1)) # max amount = 12
# output
"""
(
    [
        {'name': 'Fast & Furious (2009)',
            'img': 'https://i.egycdn.com/pic/RHNhSUNlY21Zdm1tbXZFY3Z3UGNOdm1EVGptRQ.jpg',
                'rating': '6.6'
            }
        ], 
        None
    )
"""
# display search
print(searcher.display_search('fast', amount=1))
# output 
"""
Name: Fast & Furious (2009)
URL: https://gose.egybest.bid/movie/fast-furious-2009
Img: https://i.egycdn.com/pic/RHNhSUNlY21Zdm1tbXZFY3Z3UGNOdm1EVGptRQ.jpg
Rating: 6.6 
"""

# make movies getattr
movies_getattr = EgyBest(search=False)

# get movie from egy best
print(movies_getattr.get_movie('Fast Furious 2009'))
# output
"""
{   'Duration': '01:46:46',
    'evaluation': ' 6.6 من 10  •  264222 264,222 صوت',
    'genres': 'PG-13 • يجب إرشاد الآباء, لا يناسب الأطفال أقل من 13 سنة.',
    'img': 'https://i.egycdn.com/pic/WmFwZndlY21Zdm1tbXZFY2NOcHZ2Y2N3UGN3Sw.jpg',
    'language': 'الانجليزية  •   الولايات المتحدة الأمريكية ',
    'name': 'Fast & Furious (2009)',
    'quality': 'BluRay  •  1080p  •  منذ 5 اعوام',
    'story': "Brian O'Conner, back working for the FBI in Los Angeles, teams "
            'up with Dominic Toretto to bring down a heroin importer by '
            'infiltrating his operation.',
    'trailer_url': 'https://www.youtube.com/embed/k98tBkRsGl4?autoplay=1',
    'translation': 'مترجم  •  شـكـراً ffatov',
    'type': 'اكشن • اثارة',
    'watch_url': 'https://gose.egybest.bid/watch/?v=pGGGShRCGSGFGSIHlFXzHFFhGzIGihISGSFSGSadKlhRNapSGFIHlIzIIVsrlIlIVSGShREGSGFGSLPnHIShljbpIIGSFSGSxaoaxhMLXSGFGGGSxNUGSGFGSdREZpQWhhShZoazGtkREGSGlFSGSERqSGFGSPhRExzNjqKGhjKhajEGSGl&h=a897d3e30f58d4f5a0b38d17985bcbe0'
    }
"""