import requests
import json
from collections import Counter
is_debug:bool=True
if not is_debug:
    r = requests.get('https://linku.la/jasima/data.json')
    database=r.json()
    json.dump(database,open("database.json","w"))
def debug():
    database=json.load(open("database.json","r"))
    return database
if is_debug:
    database=debug()
word_list=[]
coined_book_list=[]
word_letter_dict:dict[str,set]={}
def get_included_letter(word: str) -> set:
    counter=Counter(word)
    return set(counter.keys())
    return [x[0] for x in counter.most_common()]
for word in database["data"]:
    try:
        word_book=database["data"][word]["book"]
    except KeyError:
        coined_book_list.append(None)
        continue
    else:
        if word_book in ["pu","ku suli"]:
            word_list.append(word)
            #print(get_included_letter(word))
            word_letter_dict[word]=get_included_letter(word)
        coined_book_list.append(word_book)

#counter=Counter(coined_book_list)
#print(counter)
def depth_first_search(word: str):
    word_letter=word_letter_dict[word]
    available_word_list=[]
    for word in word_list:
        added_letters=(word_letter|word_letter_dict[word])-word_letter
        print(added_letters)
        if added_letters:
            available_word_list.append(added_letters)
        print(available_word_list)
    pass
#depth_first_search("kijetesantakalu")