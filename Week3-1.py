print('Numbers from 1 to 10')
number=4
while True:
    num=int(input("Guess the number: "))
    if num!=number:
        continue
    else :
        print('Great! You did it!')
        break
