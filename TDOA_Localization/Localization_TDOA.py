'''
This is the program that takes mics coordination and TDOA and V(sound speed) as input and
return sound source coordinates(x,y,z) as output

author: sadden
'''

import numpy as np
import re
# it let user input mics' coordinations
def mic_coordinations_input():
    pattern = re.compile(r'\d+$') # make sure all input are numbers
    while True:
        mics_number = input('Please input microphone number:')
        if pattern.match(mics_number):
            break
        else:
            print('Invalid Input!')
            
    mics_number = int(mics_number)
    
    if mics_number <4:
        print('Invalid Number!')
    else:
        mic_coordinations = []
        i = 0
        while True:
            try:
                x,y,z = input('Coordination(x,y,z) for #'+str(i)+' microphone:').split(',')
                if pattern.match(x) and pattern.match(y) and pattern.match(z):
                    mic_coordinations.append([int(x),int(y),int(z)])
                    i += 1
                else:
                    print('Wrong Input!')
            except:
                print('Invalid Input!')
                
            if i >= mics_number: break
                
        return mic_coordinations

def sound_speed_input():
    pattern = re.compile(r'\d+$') # make sure all input are numbers
    
    while True:
        sound_speed = input('sound speed for this detection:')
        if pattern.match(sound_speed):
            break
        else:
            print('Invalid Input!')
    
    
    return int(sound_speed)
# the number of time difference of arrival should = mics_number - 1
# TDOA should be [t2, t3, ..., tm]
def TDOA_input(mics_number):
    # pattern = re.compile(r'\d+$') # make sure all input are numbers
    TDOA = []
    i = 0
    while True:
        try:
            t = input('Time difference between mic #1 and mic #'+str(i+2)+':')
            if t == str(0):
                TDOA.append(float(0.000001))
                print('ok')
            else:
                TDOA.append(float(t))
            i += 1
            '''
            if pattern.match(t):
                TDOA.append(int(t))
                i += 1
            else:
                print('Invalid Input')
            '''
        except:
            print('Invalid Input!')
            
        if i >= mics_number-1: break
    
    return TDOA

# calculate sound source location based on input
def Localization(TDOA, sound_speed, mic_coordinations):
    v = sound_speed
    t2 = TDOA[0] # the time difference between mic1 and mic2
    x1 = mic_coordinations[0][0]
    y1 = mic_coordinations[0][1]
    z1 = mic_coordinations[0][2]
    
    x2 = mic_coordinations[1][0]
    y2 = mic_coordinations[1][1]
    z2 = mic_coordinations[1][2]
    
    equation_number = len(mic_coordinations)-2
    # AX=B is our equations set, so initialize them
    A = np.zeros((equation_number,3))
    B = np.zeros((equation_number,1))
    # calculate Am, Bm and Cm
    for i in range(equation_number):
        tm = TDOA[i+1] # the time difference between mic1 and micm
        xm = mic_coordinations[i+2][0]
        ym = mic_coordinations[i+2][1]
        zm = mic_coordinations[i+2][2]
        A[i][0] = 2*(xm-x1)/(tm*v)-2*(x2-x1)/(t2*v)
        A[i][1] = 2*(ym-y1)/(tm*v)-2*(y2-y1)/(t2*v)
        A[i][2] = 2*(zm-z1)/(tm*v)-2*(z2-z1)/(t2*v)
        
        B[i][0] = -(tm*v-t2*v+(x1**2+y1**2+z1**2-xm**2-ym**2-zm**2)/(tm*v)-(x1**2+y1**2+z1**2-x2**2-y2**2-z2**2)/(t2*v))
        
    X = np.dot(np.linalg.pinv(A),B)
    
    return X


def main():
    # input needed values
    mic_coordinations = mic_coordinations_input() # [['31', '432', '53'], ['31', '43', '53'], ['2143', '53', '53'], ['13', '42', '53']]
    sound_speed = sound_speed_input() # 340
    mics_number = len(mic_coordinations) #
    TDOA = TDOA_input(mics_number) # [21, 32, 42]
    
    # calculate sound location
    while True:
        x,y,z = Localization(TDOA, sound_speed, mic_coordinations)
        
        print(x,y,z)
        # new one
        print('new TDOA:\n')
        TDOA = TDOA_input(mics_number)

if __name__ == "__main__":
    main()
    '''
    tmp = TDOA_input(4)
    print(tmp)
    print(tmp[0])
    '''
    
    
    
    
    
    