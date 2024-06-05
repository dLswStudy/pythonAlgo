x=input().upper()

s='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

ans=[0]*26

for i in s:  #26번
    if i in x:
        ans[s.index(i)]=x.count(i)  # 10**6
#2.6*(10**7)

if ans.count(max(ans))>1:  #26
    print('?')
else:
    print(s[ans.index(max(ans))])