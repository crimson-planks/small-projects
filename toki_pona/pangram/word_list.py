def request_word_list(book_list: list[str] | None = None):
    if(book_list is None): book_list = ["pu"]
    import requests
    
    r = requests.get("https://linku.la/jasima/data.json")
    rjson=r.json()
    word_list=[]
    for word in rjson["data"]:
        try: book=rjson["data"][word]["book"]
        except KeyError:
            continue
        else:
            if book in book_list:
                word_list.append(word)
    return word_list
print("word_list ran!")
if __name__ == '__main__':
    print(request_word_list(["pu","ku suli","ku lili","none"]))