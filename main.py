print ('Welcome to Senseialex Anagram Identifier Program AKA SAIP')
print('Enter two words and I will tell you if they are anagrams or not')
print('Cool right?')
print('Lets go for a spin')
First_word = input('Enter your first word')
Second_word = input ('Enter your second word')
    
print('Your first word is:' + First_word)

print('Your second word is:' + Second_word)
 
#Formating the string input to lowercase to ensure the program recognizes them 

if(sorted(First_word.lower())==sorted(Second_word.lower())): print("These words are anagrams.") 
else: print("These words aren't anagrams.") 
