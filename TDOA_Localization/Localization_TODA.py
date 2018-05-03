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
                    mic_coordinations.append([x,y,z])
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
    
    
    return sound_speed
# the number of time difference of arrival should = mics_number - 1
# TDOA should be [t2, t3, ..., tm]
def TDOA_input(mics_number):
    pattern = re.compile(r'\d+$') # make sure all input are numbers
    TDOA = []
    i = 0
    while True:
        try:
            t = input('Time difference between mic #1 and mic #'+str(i+2)+':')
            if pattern.match(t):
                TDOA.append(t)
                i += 1
            else:
                print('Invalid Input')
        except:
            print('Invalid Input!')
            
        if i >= mics_number-1: break
    
    return TDOA


def Localization(TDOA, sound_speed, mic_coordinations):
    
    
    return x,y,z


def main():
    # input needed values
    mic_coordinations = mic_coordinations_input()
    sound_speed = sound_speed_input()
    mics_number = len(mic_coordinations)
    TDOA = TDOA_input(mics_number)
    
    # calculate sound location
    x,y,z = Localization(TDOA, sound_speed, mic_coordinations)
    print(x,y,z)

if __name__ == "__main__":
    #main()

    tmp = mic_coordinations_input()
    print(tmp)
    
    
    
    
    
    