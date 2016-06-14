#!/usr/bin/env python
# -*- coding: utf-8 -*-

import main

#text = u'А я думаю, чего меня не палят. А оно вон чо.... '
text = u'Реклама чего? Карт? Кошельков? Магнита? Охранника? РенТВ?'
print text
a = main.get_syllables(text)
b = main.haikufi(a)
result = '-'.join(b)
print result