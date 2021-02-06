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

    y = x
    if ( y % 10 ) == 0:
        return y
    elif (math.floor(y) % 10) == 0:
        return y
    else:
        y = math.floor(y)
        if (math.floor(y) % 10) == 0:
            return y
        else:
            return -1
        
def next_tenth_test():
    '''
    test several cases for the function
    '''
    test_cases = readCSV('test-cases.csv',',')
    for t in test_cases:
        if next_tenth(t[0]) == t[1]:
            print('pass:', 'x:', t[0], 'actual:', next_tenth(t[0]), 'expected:', t[1])
        else:
            print('fail:', 'x:', t[0], 'actual:', next_tenth(t[0]), 'expected:', t[1])

next_tenth_test()
