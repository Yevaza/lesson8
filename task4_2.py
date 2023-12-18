def extract_vowel(sentence):
    return [word for word in sentence.split() if word[0].lower() in 'aeiou']
s=(input("Предложение: "))
result=extract_vowel(s)
print("Слова на гласную букву: ",result)