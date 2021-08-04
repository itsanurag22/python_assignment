word = str(input())
word = word.lower()
final = ""
vow = ['a' , 'e' , 'i' , 'o' , 'u' , 'y']
for x in range(0, len(word)):
    if(word[x] not in vow):
        final = final + '.' + word[x]
print(final)