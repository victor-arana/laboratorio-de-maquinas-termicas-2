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
    test = [[3,4]]
    t_0 = i[1]
    t_1 = t_0 + math.floor(abs(t_0))%10 
    print('t_0:', t_0) 
    print('t_1:', t_1)
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

