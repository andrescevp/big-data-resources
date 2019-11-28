#!/usr/bin/env python
from operator import itemgetter
import sys

current_word = None
word = None
translation_complete = None
# input comes from STDIN
index = 0
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip().split('\t')

    word = line[0].strip()
    translation = ''
    language = 'default'

    if len(line) == 2:
        word = line[0].strip()
        translation = ''
        language = line[1].strip()

    if len(line) == 3:
        word = line[0].strip()
        translation = line[1].strip()
        language = line[2].strip()

    if current_word == word:
        translation_complete = translation_complete + "|" + translation
        break

    if current_word:
        print('%s|%s' % (current_word, translation_complete))

    translation_complete = translation
    current_word = word

# do not forget to output the last word if needed!
if current_word == word:
    print('%s|%s' % (current_word, translation_complete))
