import pikabu
import credentials

import re
def striphtml(data):
    p = re.compile(r'<.*?>')
    return p.sub('', data)

api = pikabu.Api(login=credentials.login, password=credentials.password)
posts = api.posts.get("hot",0)
#for post in posts:
#   print post.id

comments = api.comments.get(posts[0].id)
for comment in comments:
    if len(comment.text) < 100:
        print striphtml(comment.text)

#TODO: Check for minimum 3 words, then check if first word have 5 syllables ens with whole word, ten second, then third