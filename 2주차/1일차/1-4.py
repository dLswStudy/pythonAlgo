brackets = input()

length = 10
for i in range(1, len(brackets)):
   if brackets[i-1] == brackets[i]:
       length += 5
   else:
       length += 10

print(length)