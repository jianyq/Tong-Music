from xpinyin import Pinyin
text = open('demo.txt', encoding='UTF8', errors='ignore').read()
text = text.split("\n")
rhyme_list = ['ao','ang','an','ai','a','ua','un','uo','u','ia','ie','iu','ing','in','i','ou','ong','o','ei','eng','en','er','e','vn','ve','v']
lenth = 16
def xxx(b):
    for i in range (0,len(b)):
        f=0
        if b[i]=='a':
            if i<len(b)-1:
                if b[i+1]=='o':
                    return 'ao'
                    i=i+1
                elif b[i+1]=='n':
                    if i<len(b)-2 and b[i+2]=='g':
                        return 'ang'
                        i=i+2
                    else:
                        return 'an'
                        i=i+1
                elif b[i+1]=='i':
                    return 'ai'
                    i=i+1
            else:
                return 'a'
        if b[i]=='u':
            if i<len(b)-1:
                #checkr(i+1)
                j=i+1
                f=0
                if b[j]=='a':
                    if j<len(b)-1:
                        if b[j+1]=='o' or b[j+1]=='n' or b[j+1]=='i':
                            f=1
                if b[j]=='o':
                    if j<len(b)-1:
                        if b[j+1]=='n' and b[j+2]=='g':
                            f=1
                if b[j]=='e':
                    if j<len(b)-1:
                        if b[j+1]=='i' or b[j+1]=='n':
                            f=1
                if not f>0:
                    if b[i+1]=='a':
                        return 'ua'
                        i=i+1
                    elif b[i+1]=='n':
                        return 'un'
                        i=i+1
                    elif b[i+1]=='o':
                        return 'uo'
                        i=i+1
            else:
                return 'u'
        if b[i]=='i':
            if i<len(b)-1:
                #checkr(i+1)
                j=i+1
                f=0
                if b[j]=='a':
                    if j<len(b)-1:
                        if b[j+1]=='o' or b[j+1]=='n' or b[j+1]=='i':
                            f=1
                if b[j]=='o':
                    if j<len(b)-1:
                        if b[j+1]=='n' and b[j+2]=='g':
                            f=1
                if b[j]=='e':
                    if j<len(b)-1:
                        if b[j+1]=='i' or b[j+1]=='n':
                            f=1
                if not f>0:
                    if b[i+1]=='a':
                        return 'ia'
                        i=i+1
                    elif b[i+1]=='e':
                        return 'ie'
                        i=i+1
                    elif b[i+1]=='u':
                        return 'iu'
                        i=i+1
                    elif b[i+1]=='n':
                        if b[i+1]=='g':
                            return 'ing'
                            i=i+2
                        else:
                            return 'in'
                            i=i+1
            else:
                return 'i'
        if b[i]=='o':
            if i<len(b)-1:
                if b[i+1]=='u':
                    return 'ou'
                    i=i+1
                elif b[i+1]=='n' and b[i+2]=='g':
                    return 'ong'
                    i=i+2
            else:
                return 'o'
        if b[i]=='e':
            if i<len(b)-1:
                if b[i+1]=='i':
                    return 'ei'
                    i=i+1
                elif b[i+1]=='n':
                    if b[i+1]=='g':
                        return 'eng'
                        i=i+2
                    else:
                        return 'en'
                        i=i+1
                elif b[i+1]=='r':
                    return 'er'
                    i=i+1
            else:
                return 'e'
        if b[i]=='v':
            if i<len(b)-1:
                #checkr(i+1)
                j=i+1
                f=0
                if b[j]=='a':
                    if j<len(b)-1:
                        if b[j+1]=='o' or b[j+1]=='n' or b[j+1]=='i':
                            f=1
                if b[j]=='o':
                    if j<len(b)-1:
                        if b[j+1]=='n' and b[j+2]=='g':
                            f=1
                if b[j]=='e':
                    if j<len(b)-1:
                        if b[j+1]=='i' or b[j+1]=='n':
                            f=1
                if not f>0:
                    if b[i+1]=='n':
                        return 'vn'
                        i=i+1
                    elif b[i+1]=='e':
                        return 've'
                        i=i+1
            else:
                return 'v'
def rhyme(line):
	test = Pinyin()
	b=str(test.get_pinyin(line[-1]))
	b.ljust(len(b)+10)
	c = xxx(b)
	if c == None:
		return 0.0
	num = rhyme_list.index(c)
	num /= len(rhyme_list)
	return num

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
            # print(text[line])
            st = rhyme(text[line])
            cnt += 1
            # print(visit)
            break
    for line in range(lenth):
        if rhyme(text[line]) == st:
            ans[line] = cnt
            tot += 1
print(ans)