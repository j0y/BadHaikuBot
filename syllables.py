#coding=utf-8
import re
vowels = set(u'аеёиоуыэюя')
sign_chars = set(u'ъь')
pattern = re.compile(u"(c*[ьъ]?vc+[ьъ](?=v))|(c*[ьъ]?v(?=v|cv))|(c*[ьъ]?vc[ъь]?(?=cv|ccv))|(c*[ьъ]?v[cьъ]*(?=$))")

def get_syllables(word):
    mask = ''.join(['v' if c in vowels else c if c in sign_chars else 'c' for c in word.lower()])
    return [word[m.start():m.end()] for m in pattern.finditer(mask)]

word = raw_input('слово:').decode('utf-8')
print '-'.join(get_syllables(word))