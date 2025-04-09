vovels="aeiouAEIOU"
s = "hello"
 
c = 0
def count_vowelsads(s):
    for i in s:
        if i in vovels:
            c += 1
    return c
print(count_vowelsads(s))