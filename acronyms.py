# A simple program to make an acronym from a phrase

phrase = input("Enter a Phrase: ")
text = phrase.split()
Acronyms = " "
for i in text:
    Acronyms = Acronyms+str(i[0]).upper()
print(Acronyms)