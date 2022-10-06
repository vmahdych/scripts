#!/usr/bin/env python3

lang=input('What language do you speak? :')

def greet(lang):
    if lang == 'ua':
#        print('Доброго вечора, ми з України')
        return 'Доброго вечора, ми з України'
    elif lang == 'es':
#        print('Hola')
        return 'Hola'
    elif lang == 'fr':
#        print('Bonjour')
        return 'Bonjour'
    else:
#        print('Hello')
        return 'Hello'


greet(lang)
