#dependencies: requests(pip install requests)
#              tqdm(pip install tqdm)
#modify this
#parameters to change the word list
#book_list: choose from ["pu","ku suli","ku lili","none"]
book_list = ["pu","ku suli","ku lili","none"]



#do not modify below
from word_list import request_word_list
from char_frequency import GetCharacterUsage_OnePerWord
from tqdm import tqdm
word_list = request_word_list(book_list)
character_usage = GetCharacterUsage_OnePerWord(word_list).most_common()
characters_sorted = [(t[0],1<<i) for i,t in enumerate(character_usage)]
#print(characters_sorted)
def word_to_integer(word: str) -> int:
    rslt = 0
    for c in word:
        for ch_match in characters_sorted:
            if c == ch_match[0]:
                rslt |= ch_match[1]
    return rslt
pangram_integer = word_to_integer("aeioumnptkswlj")
word_integer_list = [word_to_integer(word) for word in word_list]

#recursion
#base case, recursion
word_len = len(word_list)
def ntuple_to_int(ntuple: tuple[int]) -> int:
    rslt=0
    for i, n in enumerate(ntuple):
        rslt+=n*word_len**i
    return rslt
def GetPangrams_NoAddingWordsThatAddsNoNewLetters(current_char_occurence: int,latest_word_id: int,character_count: int):
    if character_count>17: return
    for word_id, word in enumerate(word_list[latest_word_id+1:],start=latest_word_id+1):
        if character_count+len(word)>17: continue
        rslt_char_occurence = current_char_occurence | word_integer_list[word_id]
        if rslt_char_occurence == current_char_occurence: 
            continue
        if rslt_char_occurence == pangram_integer: 
            yield ((word_id,),character_count+len(word))
        else:
            for working_word_list in GetPangrams_NoAddingWordsThatAddsNoNewLetters(rslt_char_occurence,word_id,character_count+len(word)): 
                yield (working_word_list[0]+(word_id,),working_word_list[1])
#amount of 2 word combinations for progress bar
with tqdm(total=word_len**3) as pbar:
    with open(f"results.txt",mode='w') as result_file:
        prev_num = 0
        for a in GetPangrams_NoAddingWordsThatAddsNoNewLetters(0,-1,0):
            if(a[1]<=17): result_file.write(' '.join([ word_list[n] for n in a[0]])+'\n')
            curr_num = ntuple_to_int(a[0][-3:])
            pbar.update(curr_num-prev_num)
            prev_num = curr_num
print("finished!")