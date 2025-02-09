# is mn hm aik word sy dosra word bnat hn lakin spellings same rhty hn

def are_anagrams(str1,str2):
    str1=str1.replace(" ","").lower()
    str2=str2.replace(" ","").lower()

    if sorted(str1)==sorted(str2):
        print("These are Anagorams words")
    else:
        print("Not Anagorams ")

print(are_anagrams("listen","silent"))
print(are_anagrams("Hello","worlds"))