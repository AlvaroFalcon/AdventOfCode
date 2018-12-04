def doOperation(operator, value):
    if '+' in line:
        print(line[0])
    else:
        print('Resta')


file = open('day_one_input.txt','r')
frequency = 0

        
for line in file:
    doOperation(line,line)
    
    
