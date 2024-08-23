from collections import Counter
def GetCharacterUsage_OnePerWord(word_list):
    char_usage_counter = Counter()
    for word in word_list:
        word_set_no_duplicates = set(word)
        char_usage_counter.update(word_set_no_duplicates)
    return Counter(char_usage_counter)
def main():
    from word_list import request_word_list
    print(GetCharacterUsage_OnePerWord(request_word_list(["pu","ku suli","ku lili","none"],["core","common","uncommon","obscure"])).most_common())
    #aioenklsupmtjwyARPg
    #kalamARR Pingo
if __name__ == '__main__':
    main()