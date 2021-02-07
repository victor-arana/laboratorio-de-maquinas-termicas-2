def readCSV(file_path, delim):
    '''
    Reads a csv file
    file_path: path to the file
    delim: delimiter used in the csv file
    return: a list containing the read registers
    '''
    import csv
    rows = []
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=delim)
        for row in csv_reader:
            col = []
            for column in row:
                col.append(float(column))
            rows.append(col)
    return rows

def next_tenth(x):
    '''
    Given a real number x, return the closest integer
    number y such as x <= y, and b is divisible by 10.
    x: float number
    return y: closest integer such as x <= y and b % 10.
    '''
    import math

    next_tenth = None
    
    if x.is_integer() and (x % 10 == 0):
        next_tenth = x + 10   
    elif (math.floor(x) % 10) == 0:
        return x
    else:
        x = math.floor(x)
        if (math.floor(x) % 10) == 0:
            return x
        else:
            return -1
    return next_tenth
        
def next_tenth_test():
    '''
    test several cases for the function
    '''
    test_cases = readCSV('test-cases.csv',',')
    separator = ','
    print('status', 'argument', 'actual', 'expected', sep=separator)
    for t in test_cases:
        argument = t[0]
        actual = next_tenth(argument) 
        expected = t[1]   
        status = 'FAILURE'
        if actual == expected:
            status = 'success'
        print(status, argument, actual, expected, sep=separator)

next_tenth_test()
