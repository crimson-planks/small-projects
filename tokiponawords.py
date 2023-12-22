#dependencies: requests(pip install requests)
import requests

r = requests.get("https://linku.la/jasima/data.json")
rjson=r.json()
word_list=[]
word_character_dict={}
for word in rjson["data"]:
    #banlist
    #if word in ["li","e","pi","o","a","n"]:
    #    continue
    try: book=rjson["data"][word]["book"]
    except KeyError:
        continue
    else:
        if book in ["pu", "ku suli"]:
            word_list.append(word)
            word_character_dict[word]=set(word)
def get_word(length: int):
    if length==1:
        for word in word_list:
            yield ([word],set(word))
        return
    for word,wordset in get_word(length-1):
        for word2 in word_list:
            if wordset|set(word2)==wordset:
                continue
            yield (word+[word2],wordset|set(word2))
for i in get_word(3):
    print(i)
