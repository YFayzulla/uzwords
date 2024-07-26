from  uzwords import words
from difflib import get_close_matches


def checkWords (word,words=words):
    word=word.lower()
    matches = set(get_close_matches(word,words))
    availble =False

    if word in matches:
        availble =True 
        matches = word 

    return { 'availble':availble,'matches': matches }

if __name__ == '__main__':

    print(checkWords('амбош'))
    print( checkWords('тарих') )