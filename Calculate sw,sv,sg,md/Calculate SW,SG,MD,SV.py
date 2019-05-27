print('What do you want to calculate')
print('press 1 Specific Weight')
print('press 2 Specific Volume')
print('press 3 Specific Gravity')
print('press 4 Mass Density')

try:
    x = str(input('Choose the option: '))
    if x=='1':
        W = float(input('Enter weight in kg :'))
        V = float(input('Enter Volume m^3 :'))
        w1 = W*9.81
        sw =  w1/V 
        print('The specific weight is ' + str(sw) +  ' N/m^3')
    elif x==2:
        m = float(input('Enter the mass in kg: '))
        v = float(input('Enter the Volume in m^3: '))
        sv = v/m
        print('The specific Volume is '+ str(sv)+ ' m^3/kg')
    elif x==3:
        s1 = float(int("Enter the mass density of the fluid: "))
        s2 = float(int("Enter the mass density of the standard fluid: "))
        sg = s1/s2 
        print('The Specific gravity is '+str(sg))
    else:
        m = float(input('Enter the mass in kg: '))
        v = float(input('Enter the Volume in m^3: '))
        md = v/m
        print('The Mass density is '+ str(md)+ ' kg/m^3')  
except ValueError:
        print("Please choose a number from the option given.")
     
    
    