import re

f_name = input("파일 이름을 입력하세요: ")
f_fetch = open(f_name).read()

all_low_text = f_fetch.lower()
new_low_text = re.sub(r'[^\w\s]', " ", all_low_text)

word_list = new_low_text.split()
n_gram_ls = zip(word_list, word_list[1:])

n_gram_dict = dict()

for n_gram in n_gram_ls:
    n_gram_dict.setdefault(n_gram, 0)
    n_gram_dict[n_gram] += 1

max_val = max(n_gram_dict, key = lambda x: n_gram_dict[x])

print('max2gram:', max_val, n_gram_dict[max_val])

# num_val = 0

# for n_gram in n_gram_ls:
#     if n_gram not in n_gram_dict:
#         n_gram_dict.setdefault(n_gram, num_val)
    
    # if n_gram not in n_gram_dict:
    #     n_gram_dict.setdefault(n_gram, val)
    # elif n_gram in n_gram_dict:
    #     n_gram_dict.fromkeys(n_gram, val + 1)
