def next_tenth(x):
    '''
    Given a real number x, return the closest integer
    number y such as x <= y, and b is divisible by 10.
    x: float number
    return y: closest integer such as x <= y and b % 10.
    '''
    y = x
    return y

def next_tenth_test():
    '''
    test several cases for the function
    '''
    test_cases = []
    test_cases.append([0,10])
    test_cases.append([0.5,0])
    test_cases.append([5,10])
    test_cases.append([9.6,10])
    test_cases.append([-3,0])
    test_cases.append([-30,-30])
    test_cases.append([-36.5,-30])
    test_cases.append([-1,0])

    for t in test_cases:
        if next_tenth(t[0]) == t[1]:
            print('pass')
        else:
            print('fail')

next_tenth_test()
