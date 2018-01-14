## Knuth–Morris–Pratt algorithm

from sys import stdin

def KMP(main, sub):
    subArr = [0]
    i=1
    j=0
    while i!=len(sub):
        if sub[i] != sub[j]:
            j = subArr[j-1]
            if j==0 and sub[i] != sub[j]:
                subArr.append(0)
                i += 1
        else:
            subArr.append(j+1)
            i += 1
            j += 1
    i =0 
    j=0
    match = []
    while i != len(main):
        if main[i] == sub[j]:
            i += 1
            j += 1
        if j == len(sub):
            match.append(i-j)
            j = subArr[j-1]
        elif i < len(main) and main[i] != sub[j]:
            if j ==0:
                i += 1
            else:
                j = subArr[j-1]
    if len(match) == 0:
        return
    else:
        for i in match:
            print(i)

def main():
    sub = stdin.readline().strip()
    main = stdin.readline().strip()
    KMP(main, sub)
    
main()
