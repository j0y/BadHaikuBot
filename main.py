#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pikabu
import credentials
import re
from bs4 import BeautifulSoup

vowels = set(u'аеёиоуыэюя')
sign_chars = set(u'ъь')
pattern = re.compile(u"(c*[ьъ]?vc+[ьъ](?=v))|(c*[ьъ]?v(?=v|cv))|(c*[ьъ]?vc[ъь]?(?=cv|ccv))|(c*[ьъ]?v[cьъ]*(?=$))")

def get_syllables(word):
    mask = ''.join(['v' if c in vowels else c if c in sign_chars else 'c' for c in word.lower()])
    return [word[m.start():m.end()] for m in pattern.finditer(mask)]

api = pikabu.Api(login=credentials.login, password=credentials.password)
posts = api.posts.get("hot",0)

for post in posts:
    comments = api.comments.get(post.id)
    for comment in comments:
        if len(comment.text) < 100:
            striped_comment = BeautifulSoup(comment.text).text
            count = len(get_syllables(striped_comment))
            #5 7 5 notation
            if count == 17:
                #checking for minimum 3 words
                if striped_comment.count(" ") >= 2:
                    print striped_comment
                    print '-'.join(get_syllables(striped_comment))


#TODO: Check if first word have 5 syllables ens with whole word, ten second, then third