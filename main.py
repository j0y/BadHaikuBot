#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pikabu
import credentials
import re

def striphtml(data):
    p = re.compile(r'<.*?>')
    return p.sub('', data)

vowels = set(u'аеёиоуыэюя')
sign_chars = set(u'ъь')
pattern = re.compile(u"(c*[ьъ]?vc+[ьъ](?=v))|(c*[ьъ]?v(?=v|cv))|(c*[ьъ]?vc[ъь]?(?=cv|ccv))|(c*[ьъ]?v[cьъ]*(?=$))")

def count_syllables(word):
    mask = ''.join(['v' if c in vowels else c if c in sign_chars else 'c' for c in word.lower()])
    return len(pattern.findall(mask))

api = pikabu.Api(login=credentials.login, password=credentials.password)
posts = api.posts.get("hot",0)
#for post in posts:
#   print post.id

comments = api.comments.get(posts[0].id)
for comment in comments:
    if len(comment.text) < 100:
        striped_comment = striphtml(comment.text)
        print striped_comment
        print count_syllables(striped_comment)

#TODO: Check for 17 syllablies and minimum 3 words(2 spaces), then check if first word have 5 syllables ens with whole word, ten second, then third