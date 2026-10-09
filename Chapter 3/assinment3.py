#Write a program that takes a sentence and print:
#Total Character(len())
#UpperCase version
#Lowercase version

i = input("Enter a sentence: ")

i = i.upper()

print(i)

i = i.lower()

print(i)


#Write a python program that takes any word  or sentence and print:

#the first Character
#the last character
#the total number of character
first_character = i[0]
last_character = i[-1]
total_character = len(i)

print("First character:", first_character)
print("Last character:", last_character)
print("Total characters:", total_character)