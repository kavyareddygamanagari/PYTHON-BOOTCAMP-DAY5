#REMOVE braces FORM THE STRING
inp=input()
for i in inp:
    if(ord(i)==40 or ord(i)==41 or ord(i)==90 or ord(i)==91 or ord(i)==123 or ord(i)==125 or ord(i)==93):
      pass
    else:
      print(i,end="")
print()