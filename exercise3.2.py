#Write a program to prompt the user for hours and rate per hour using input to compute gross pay
hours = input('Enter Hours:')
rate = input('Enter Rate:')
try :
   hours = float(hours)
   rate = float(rate)
except:
    print('Error.pleace enter numeric input')
    quit()
    print(hours,rate)
if hours <= 40 :
    pay = hours * rate
elif hours > 40 :
    pay =40 * rate + (hours-40) * rate * 1.5

print('Pay:',pay)
