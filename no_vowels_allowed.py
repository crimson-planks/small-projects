#dependencies: requests(pip install requests)
#https://discord.com/channels/301377942062366741/301377942062366741/1263743142692130896 for reference
import requests
from collections import Counter
r = requests.get("https://linku.la/jasima/data.json")
rjson=r.json()
word_list=[]
word_character_dict={}
for word in rjson["data"]:
    try: book=rjson["data"][word]["book"]
    except KeyError:
        continue
    else:
        if book in ["pu"]:
            word_list.append(word)
            word_character_dict[word]=set(word)
def change_word(word: str):
    return word.replace('i','j').replace('u','w').replace('o','t').replace('a','p').replace('e','s')
pokiimtoolazysoilljustcheckmanually= Counter(map(change_word,word_list))
print(pokiimtoolazysoilljustcheckmanually)