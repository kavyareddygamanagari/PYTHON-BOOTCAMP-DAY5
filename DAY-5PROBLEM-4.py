#print all the vowels followed by consonants
vowel="aeiou"
consonants="bcdfghjklmnpqrstvwxyz"
ans=""
i="hello world"
inp=i.lower()
for i in inp:
    if(i in vowel):
        ans+=i
for i in inp:
    if(i in consonants):
        ans+=i
print(ans)