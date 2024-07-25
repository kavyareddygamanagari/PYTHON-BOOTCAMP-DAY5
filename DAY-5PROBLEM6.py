#sumofnumericinthegivenstring
#n="hello123"
#s=0
#for i in n:
   # if(i.isnumeric()):
       # s=s+int(i)
#print(s)
#or
vowel="aeiou"
consonent="bcgflladerthikmnbvcf"
check="0123456789"
ans=0
i="hello123world"
inp=i.lower()
for i in inp:
    if(i in check):
        ans+=int(i)
        print(ans)
