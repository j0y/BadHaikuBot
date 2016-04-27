#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pikabu
import credentials
import re
from bs4 import BeautifulSoup

vowels = set(u'аеёиоуыэюя')
sign_chars = set(u'ъь')
pattern = re.compile(u"(c*[ьъ]?vc+[ьъ](?=v))|(c*[ьъ]?v(?=v|cv))|(c*[ьъ]?vc[ъь]?(?=cv|ccv))|(c*[ьъ]?v[cьъ]*(?=c|v)?)")

def get_syllables(word):
    mask = ''.join(['v' if c in vowels else c if c in sign_chars else 'c' for c in word.lower()])
    return [word[m.start():m.end()] for m in pattern.finditer(mask)]

api = pikabu.Api(login=credentials.login, password=credentials.password)
posts = api.posts.get("hot",0)

#moving text to new line (replacing space with \n) in 5 and 12 syllable
def haikufi(syllables):
    for i in [5,12]:
        if syllables[i-1][-1] == " ":
            syllables[i-1] = syllables[i-1][:-1] + "\n"
        elif syllables[i][0] == " ":
            syllables[i] =   "\n" + syllables[i][1:]
        else: return 0
    return syllables

for post in posts:
    comments = api.comments.get(post.id)
    for comment in comments:
        if 20 < len(comment.text) < 100:
            striped_comment = BeautifulSoup(comment.text).text
            syllables = get_syllables(striped_comment)
            count = len(syllables)
            #5 7 5 notation
            if count == 17:
                #checking for minimum 3 words
                if striped_comment.count(" ") >= 2:
                    haiku = haikufi(syllables)
                    if haiku:
                        print striped_comment
                        print ''.join(haiku)