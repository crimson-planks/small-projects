#idea: https://discord.com/channels/301377942062366741/994960433951801374/1270176277453602907
from collections.abc import Iterator, Iterable
def file_to_generator(file): #make another function to turn other streams into iterators
    while True:
        char=file.read(1)
        if(char==''): break
        yield char
def str_to_generator(txt: str): #the same thing but for strings
    yield from txt
def char_gen_to_word_gen(char_generator: Iterable[str] | Iterator[str]): #since it is already tokenized, you can convert the stream into a generator and put it directly to DO_THE_WOOOORK.
#also how do I annotate generators?
    current_word=[]
    for char in char_generator:
        if char==' ':
            yield ''.join(current_word)
            current_word=[]
        else:
            current_word.append(char)
    yield ''.join(current_word)

def get_kml_table(phrase: list[str]) -> list[int]:
    table: list[int] = [0]*(len(phrase)+1)
    cnd = 0
    table[0] = -1
    for pos in range(1,len(phrase)):
        if phrase[pos] == phrase[cnd]:
            table[pos] = table[cnd]
        else:
            table[pos] = cnd
            while cnd >= 0 and phrase[pos] != phrase[cnd]:
                cnd = table[cnd]
        cnd += 1
    table[len(phrase)] = cnd
    return table

print(get_kml_table(["toki","ike","li","toki","pona"]))
def DO_THE_WOOOORK(word_gen: Iterable[str] | Iterator[str],phrase_to_find: list[str],table: list[int] | None = None):
    #using KMP with modifications so that when overlaps happen, only the first one is considered
    iPattern = 0
    nP = 0
    if(table is None): table = get_kml_table(phrase_to_find)
    for iWord, word in enumerate(word_gen):
        if phrase_to_find[iPattern] == word:
            iPattern+=1
            if iPattern == len(phrase_to_find):
                nP+=1
                yield iWord - iPattern + 1 #yields the index
                iPattern = 0 #this is the part that differs from usual KMP. it doesn't have to check a match that overlaps with this match, so it just set k to 0, (and check the next character)
            continue
        else:
            iPattern = table[iPattern]
            if iPattern < 0:
                iPattern += 1
def get_amount(gen: Iterable[str] | Iterator[str]):
    nP = 0
    for _ in gen:
        nP+=1
    return nP


    



with open("corpus.txt") as corpus_file:
    char_gen=file_to_generator(corpus_file)
    word_gen=char_gen_to_word_gen(char_gen)
    # mun Kekan San o, you can make a wrapper function to turn your tokenized corpus into an iterator.
    # If you do that you can remove the above 2 lines of code.
    print(get_amount(DO_THE_WOOOORK(word_gen, ["a","mu","a"])))
