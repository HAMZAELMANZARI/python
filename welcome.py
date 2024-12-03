# This program is age barrier/Passage.
print('Welcome in the worlds PIAZZA')
nam = input('What is your name?\n')
print('Hello',nam)
old = input('Who old are you?\n')
# Tryexcept for glos in the problem old 
try:
    old=int(old)
except:
    old=-1  
    exit(print('Not a number,Try again',nam))
if int(old)<24:
    print('Small')
    print('We are sorry that you are not accepted with us, you are too young.')
    print('goodbays',nam)
elif int(old)<=24:
    print('You have been accepted')
    print('welcome in the PIAZZA MR',nam)
elif int(old)<=40:
    print('You have been accepted')
    print('welcome in the PIAZZA',nam)
elif int(old)>40:
    print('Large')
    print('We are sorry that you are not accepted with us, you are too Begginer.')
    print('goodbays',nam)





