sk=input()
f=0
for i in range(len(sk)):
 if(sk[i].isdigit() or sk[i].isalpha() or sk[i]==(" ")):
  continue
 else:
  f+=1
print(f)
