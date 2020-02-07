from rhyme_searching import *
text = open('demo.txt', encoding='UTF8', errors='ignore').read()
text = text.split("\n")
lenth = 16
tot = 0
visit = []
ans = []
cnt = 0
for _ in range(lenth):
    ans.append(0)
while 1:
    if tot == lenth:
        break
    st = 0
    for line in range(lenth):
        if rhyme(text[line]) not in visit:
            visit.append(rhyme(text[line]))
            st = rhyme(text[line])
            cnt += 1
            break
    for line in range(lenth):
        if rhyme(text[line]) == st:
            ans[line] = cnt
            tot += 1
print(ans)