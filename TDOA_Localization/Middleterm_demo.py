import Localization_TDOA as LT
import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time  

random.seed(time.time())
# assume the for mics are placed at the following locations
mic_coordinations = [[0, 0, 0], [1000, 0, 0], [1000, 1000, 0], [0, 1000, 0]]
sound_speed = 340

# generate random sound location within the ROI
num_of_samples = 50
real_sound_locations = []
for i in range(num_of_samples):
    x = random.randint(0,1000)
    y = random.randint(0,1000)
    z = 0
    real_sound_locations.append([x,y,z])
print(real_sound_locations)
# TDOAs of the sound sources based on sound_speed
real_TDOAs = []
mics_number = len(mic_coordinations) # it determines how many TDOAs based on number of mics
for location in real_sound_locations:
    # real sound location
    x,y,z = location
    # calculate the distances from sound source to the mics
    distances = []
    # TDOA for one sample
    real_TDOA = []
    for j in range(mics_number):
        xj = mic_coordinations[j][0]
        yj = mic_coordinations[j][1]
        zj = mic_coordinations[j][2]
        Rj = np.sqrt(np.square(xj-x)+np.square(yj-y)+np.square(zj-z))
        Rj = np.asscalar(Rj)
        distances.append(Rj)
    # its time difference between each of them
    R1 = distances[0]
    for j in range(mics_number-1):
        tm = (R1-distances[j+1])/sound_speed
        real_TDOA.append(tm)
    real_TDOAs.append(real_TDOA)
    # reset to empty
    real_TDOA = []

# add disturbance as Gaussian distribution
disturbed_TDOAs = []
for real_TDOA in real_TDOAs:
    disturbed_TDOA = []
    for time_difference in real_TDOA:
        # assume most of the disturbed measured TDOAs is within 10%
        tolenrance = 0.05
        time_difference_tolenrance = time_difference*tolenrance
        time_difference = time_difference + (random.random()*2-1)*time_difference_tolenrance
        disturbed_TDOA.append(time_difference)
        
    disturbed_TDOAs.append(disturbed_TDOA)
# calculate sound location based on TDOA and display, record how much bias
plt.figure(1)
display = plt.subplot(projection='3d')
error = 0
errors = []
for i in range(num_of_samples):
    x,y,z = LT.Localization(disturbed_TDOAs[i], sound_speed, mic_coordinations)
    tmp = [np.asscalar(x),np.asscalar(y),np.asscalar(z)]
    
    print('real location'+str(i)+':', real_sound_locations[i])
    print('estimated location'+str(i)+':', tmp)
    display.scatter(real_sound_locations[i][0], real_sound_locations[i][1], real_sound_locations[i][2], c='r')
    display.scatter(tmp[0], tmp[1], tmp[2], c='g')
    error = pow(real_sound_locations[i][0]-tmp[0],2)+pow(real_sound_locations[i][1]-tmp[1],2)+pow(real_sound_locations[i][2]-tmp[2],2)
    error_distance = pow(error,0.5)
    errors.append(error_distance)


display.set_zlabel('Z')
display.set_ylabel('Y')
display.set_xlabel('X')

plt.draw()
#plt.pause(3)

plt.figure(2)
plt.plot(range(num_of_samples),errors,'r--')
plt.show()

plt.close()