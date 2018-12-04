frequency = 0
frequencies = {}
first_repeated_frequency = False

def checkFrequency(frequency):
    global frequencies
    global first_repeated_frequency
    print(frequency)
    if frequency not in frequencies:        
        frequencies[frequency] = 1
    else:
        print('FOUND!')    
        first_repeated_frequency = True


def add(value):
    global frequency
    global first_repeated_frequency
    frequency = frequency + value
    if not first_repeated_frequency:
        checkFrequency(frequency)
    

def substract(value):
    global frequency
    global first_repeated_frequency
    frequency = frequency - value
    if not first_repeated_frequency:
        checkFrequency(frequency)


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
    #print(frequencies)


calculateFrequency()
    
    
