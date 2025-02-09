def vowels():
    count=0
    vowel_letters="aeiouAEIOU"
    text=str(input("Enter Text : "))
    for letters in text:
        if letters in vowel_letters:
            count+=1
    print(f"The Total vowels are {count}")
vowels()

