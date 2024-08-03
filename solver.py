import requests

with open("wordle_words.txt", "r") as file:
    lines = file.readlines()
words = [line.strip() for line in lines]
print('Enter the letters that are in the correct spot with "?" tokens for the words that are missing:')
fixed_l = input().strip()
print('Enter the letters that are not in the correct spot with "?" tokens for the words that are missing:')
indef_l = input().strip()
print('Enter letters that are NOT in the word')
broken = input().strip()


prorated = []
for word in words:
    flag = True 
    for j in range(len(fixed_l)):
        if fixed_l[j] == '?':
            continue 
        if j >= len(word) or fixed_l[j] != word[j]:
            flag = False 
            break
    if flag:
        prorated.append(word)


filtered_words = [word for word in prorated if not any(char in set(broken) for char in word)]

words = filtered_words
stripped = list(indef_l.replace('?',''))

def match(word, chars):
    word_set = set(word)
    return all(char in word_set for char in chars)
matched_words = [word for word in words if match(word, stripped)]

print(matched_words)