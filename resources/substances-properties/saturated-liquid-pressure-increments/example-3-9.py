def v(P, T):
    '''
    P: Pressure in [bar]
    T: Temperature [C]
    returns v: specific volume in [m^3/kg] 
    '''
    import csv

    v = 0
    with open('overheated-steam.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if P == float(row[0]) and T == float(row[1]):
                v = float(row[2])
    return v
               
def u(P, T):
    '''
    P: Pressure in [bar]
    T: Temperature [C]
    returns u: internal energy in [kJ/kg] 
    '''
    import csv

    u = 0
    with open('overheated-steam.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if P == float(row[0]) and T == float(row[1]):
                u = float(row[3])
    return u

def interpolate(x, a, b, f_a, f_b):
    '''
     x: value to interpolate
     a: first independent value
     b: second independent value
     f_a: function evaluated at a
     f_b: function evaluated at b
     return: f(x)		
    '''
    m = (x-a)/(b-a)
    f_x = m * (f_b - f_a) + f_a
    return f_x


u_1 = u(P_1, T_1)
Δu = (u_2 - u_1)
Q = m * ( Δu - w )
print("Q =", Q, "[kJ]")

P = 30 #[bar]
T_1 = 240 #[C]
T_2 = 320 #[C]

v_1 = v(P, T_1)
v_2 = v(P, T_2)

# Unit conversion: bar --> Pa
P = P * 10 ** 5
# specific work in [J/kg]
w = -P * (v_2 - v_1)
# Unit conversion J/kg --> kJ/kg
w = w / 10 ** 3
print("w =", w, "[kJ/kg]")

# Unit conversion:  Pa --> bar
P = P / 10 ** 5
u_1 = u(P,T_1)
u_2 = u(P,T_2)
Δu = u_2 - u_1 
q = Δu - w
print("q =", q, "[kJ/kg]")
