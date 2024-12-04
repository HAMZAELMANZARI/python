#Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error.
print('Range score: 0.0 - 1.0')
score = input('Enter score:\n')
try :
    score = float(score)
except :
    print('errors!Range score: 0.0 - 1.0')
    quit()
if score >= 1.0 :
    print('Errors')
elif score >= 0.9 :
    print('A')
elif score >= 0.8 :
    print('B')
elif score >= 0.7 :
    print('C')
elif score >= 0.6 :
    print('D')
elif score < 0.6 :
    print('F')