import re
print('Our Calculator')
print('Enter "quit" to Exit')
previous = 0
run = True

def do_math():
    global run
    global previous
    equation = ''
    if previous == 0:
        equation = input('Enter Equation:')
    else:
        equation = input(str(previous))
    if equation == 'quit':
        print('GoodBye, Buddy')
        run = False
    else:
        equation = re.sub('[A-Za-z.,:()" "]', '', equation)
        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)
        #print('you typed', previous)
while run:
    do_math()