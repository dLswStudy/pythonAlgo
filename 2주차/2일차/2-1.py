words = [input() for _ in range(int(input()))]
hashTable = {}

# ex) word => las, sal
for word in words:
    if word == word[::-1] or word[::-1] in hashTable:
        print(len(word), word[len(word)//2])
        break
    else:
        hashTable[word] = 1

