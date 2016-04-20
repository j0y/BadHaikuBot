#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pikabu
import credentials
import re
from bs4 import BeautifulSoup

vowels = set(u'аеёиоуыэюя')
sign_chars = set(u'ъь')
pattern = re.compile(u"(c*[ьъ]?vc+[ьъ](?=v))|(c*[ьъ]?v(?=v|cv))|(c*[ьъ]?vc[ъь]?(?=cv|ccv))|(c*[ьъ]?v[cьъ]*(?=$))")

def count_syllables(word):
    mask = ''.join(['v' if c in vowels else c if c in sign_chars else 'c' for c in word.lower()])
    return len(pattern.findall(mask))

api = pikabu.Api(login=credentials.login, password=credentials.password)
posts = api.posts.get("hot",0)

for post in posts:
    comments = api.comments.get(post.id)
    for comment in comments:
        if len(comment.text) < 100:
            striped_comment = BeautifulSoup(comment.text).text
            count = count_syllables(striped_comment)
            if count == 17:
                print striped_comment


#TODO: Check for minimum 3 words(2 spaces), then check if first word have 5 syllables ens with whole word, ten second, then third