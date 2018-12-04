frequency = 0
def add(value):
    global frequency
    frequency = frequency + value    


def substract(value):
    global frequency
    frequency = frequency - value


def doOperation(operator, value):    
    if '+' in operator:
        add(int(value))
    else:
        substract(int(value))

def calculateFrequency():
    file = open('day_one_input.txt','r')

    for line in file:
        operator = line[0]
        value = line[1:]
        doOperation(operator, value)        
    print(frequency)

calculateFrequency()
    
    
