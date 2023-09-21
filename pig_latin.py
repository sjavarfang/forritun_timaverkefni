
text_to_translate = input()
VOWELS = "aeiouyAEIOUY"
translation = ""


words = text_to_translate.split()

for word in words:
    if word[0] in VOWELS:
        translation += word + "yay"
    else:
        consonants = ""
        i = 0
        while i < len(word) and word[i] not in VOWELS:
            consonants += word[i]
            i += 1
        translation += word[i:] + consonants + "ay"

    translation += " "


print(translation)
