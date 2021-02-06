def next_tenth(x):
    import math
    '''
    Given a real number x, return the closest integer
    number y such as x <= y, and b is divisible by 10.
    x: float number
    return y: closest integer such as x <= y and b % 10.
    '''
    y = math.floor(x) + 10
    return y

def next_tenth_test():
    '''
    test several cases for the function
    '''
    test_cases = []
    test_cases.append([-10.0, -10.0])
    test_cases.append([0.0,0.0])
    test_cases.append([10.0,10.0])
    test_cases.append([0.5,0.0])
    test_cases.append([5.0,10.0])
    test_cases.append([9.6,10.0])
    test_cases.append([-3.0,0.0])
    test_cases.append([-30.0,-30.0])
    test_cases.append([-36.5,-30.0])
    test_cases.append([-1.0,0.0])

    for t in test_cases:
        if next_tenth(t[0]) == t[1]:
            print('pass:', 'x:', t[0], 'actual:', next_tenth(t[0]), 'expected:', t[1])
        else:
            print('fail:', 'x:', t[0], 'actual:', next_tenth(t[0]), 'expected:', t[1])

next_tenth_test()
