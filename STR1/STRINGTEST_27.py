def countnotsyllables(word):
    vowels = "aeiouAEIOU?!.,:;"
    count = 0
    for i in range(len(word)):
        if word[i] not in vowels:
            count += 1
    return count
import re
a = input()

res = re.split("\s+", a)
while res.__contains__(''):
    res.remove('')
for i in res:
    print(countnotsyllables(i))
