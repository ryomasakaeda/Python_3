import re
from collections import Counter
import pickle

def bigram_lm(sentence,uni_fre,bi_fre):
    sentence=sentence.rstrip(".")
    sentence=sentence.lower()
    word_list=sentence.split()
    # freq_a=bi_fre["<start>"+" "+word_list[0]]
    freq_a=uni_fre[word_list[0]]
    p=freq_a/freq
    print(word_list[0])
    for i in range(1,len(word_list)-1):
        freq_a=uni_fre[word_list[i]]
        freq_ab=bi_fre[word_list[i]+" "+word_list[i+1]]
        print(word_list[i])
        print(word_list[i+1])
        p*=freq_ab/freq_a
    return p

uni_list=[]
bi_list=[]
sent=""

filename="/mnt/c/Users/ryomasakaeda/member/work/new-member-training/text/doc0000000000.txt"
with open(filename) as my_file:
    for line in my_file:
        if re.match(r"^<PAGE URL=|^</PAGE>",line):
            # print(line)
            continue
        if "." in line or "!" in line or "?" in line:
            words=sent.split()
            print(sent)
            sent=""
            if not len(words)==0:
                uni_list.append(words[0])
            for i in range(1,len(words)):
                # if i==0:
                #     bi_list.append("<start>"+" "+words[i])
                # else:
                bi_list.append(words[i-1]+" "+words[i])
                uni_list.append(words[i])
        else:
            sent+=line

uni_fre=Counter(uni_list)
bi_fre=Counter(bi_list)
with open('unigram.pickle',mode='wb') as u:
    pickle.dump(uni_fre,u)
with open('bigram.pickle',mode='wb') as b:
    pickle.dump(bi_fre,b)
print(uni_fre)
print(bi_fre)
# with open('unigram.pickle',mode='rb') as u:
#     uni_fre=pickle.load(u)
# with open('bigram.pickle',mode='rb') as b:
#     bi_fre=pickle.load(b)
# print(uni_fre)
# print(bi_fre)
freq=sum(uni_fre.values())


sent="The man is in the house."
print(bigram_lm(sent,uni_fre,bi_fre))

        
