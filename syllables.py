#coding=utf-8
import re
vowels = set(u'аеёиоуыэюя')
sign_chars = set(u'ъь')
pattern = re.compile(u"(c*[ьъ]?vc+[ьъ](?=v))|(c*[ьъ]?v(?=v|cv))|(c*[ьъ]?vc[ъь]?(?=cv|ccv))|(c*[ьъ]?v[cьъ]*(?=$))")

def count_syllables(word):
    mask = ''.join(['v' if c in vowels else c if c in sign_chars else 'c' for c in word.lower()])
    return len(pattern.findall(mask))

print(count_syllables("идиоты бывает разными".decode('utf-8')))