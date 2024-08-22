def request_word_list(book_list: list[str] | None = None, usage_category_list: list[str] | None = None):
    if book_list is None: book_list = ["pu"]
    if usage_category_list is None: usage_category_list = ["core","common"]
    import requests
    
    r = requests.get("https://linku.la/jasima/data.json")
    rjson=r.json()
    word_list=[]
    for word in rjson["data"]:
        try: book=rjson["data"][word]["book"]
        except KeyError:
            continue
        try: usage_category = rjson["data"][word]["usage_category"]
        except KeyError:
            continue
        else:
            if book in book_list and usage_category in usage_category_list:
                word_list.append(rjson["data"][word]["word"])
    return word_list
print("word_list ran!")
if __name__ == '__main__':
    print(request_word_list(["pu","ku suli","ku lili","none"],["core","common","uncommon","obscure"]))