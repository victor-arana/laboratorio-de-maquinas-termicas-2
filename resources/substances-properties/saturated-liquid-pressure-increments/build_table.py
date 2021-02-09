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
    elif ( x.is_integer() and x < -1 ) or ( x.is_integer() and x > 1 ):
        next_tenth = ( math.trunc( x / 10 ) * 10 )  + 10 
    elif x < 0:
        next_tenth = ( math.trunc( x / 10 ) * 10 )
    else:
        next_tenth = ( math.trunc( x / 10 ) * 10 )  + 10 

    return next_tenth

def import_data(digits, P_low, P_high, ΔP):
    import subprocess
    call_string = "./retrieve_data.sh %s %s %s %s"  
    subprocess.check_call(call_string % (str(digits), str(P_low), str(P_high), str(ΔP)), shell=True)

def readCSV(csv_file_path):
    import csv
    rows = []
    with open(csv_file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=' ')
        for row in csv_reader:
            col = []
            for column in row:
                col.append(float(column))
            rows.append(col)
    return rows

def generateTempIncrements(i,ΔT):
    import math
    temp_increments = []
    n = 3
    low = next_tenth(i[1])
    high = ΔT * n 
    test = [[i[0], low],[i[0], low + 10], [i[0], low + 20]]
    temp_increments.extend([i])
    temp_increments.extend(test) 
    return temp_increments 

digits = 6
P_low = 0.6
P_high = 1.8
ΔP = 0.4
ΔT = 10

import_data(digits, P_low, P_high, ΔP)
P_Ts = readCSV('saturated-liquid-pressure-increments.csv')

P_T = []
for pt_s in P_Ts:
    P_Ti = generateTempIncrements(pt_s,ΔT)
    P_T.extend(P_Ti)
 
for p_t in P_T:
    print(p_t)

