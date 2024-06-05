import string
alphabets = list(string.ascii_lowercase + string.ascii_uppercase)

word = input()
def isItPrimeword(num):
    for i in range(num):
        n = i+1
        if (n != 1 and
                n != num and
                num % n == 0):
            return False
    return True

wordNum = 0
for char in word:
    wordNum += alphabets.index(char) + 1

print('It is a prime word.'
      if isItPrimeword(wordNum) else 'It is not a prime word.')


