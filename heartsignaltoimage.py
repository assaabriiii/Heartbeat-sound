import wave
import numpy as np
import matplotlib.pyplot as plt
import os
from playsound import playsound

normal_files    = os.listdir('Normal')
abnormal_files  = os.listdir('Abnormal')



for file in normal_files:
    playsound("Normal/" + file)
    
    wave_file = wave.open('Normal/' + file, 'r')

    frames = wave_file.readframes(-1)
    frames = np.frombuffer(frames, dtype=np.int16)
    wave_file.close()
    plt.plot(frames)
    
    plt.gcf().set_size_inches(2, 2)
    plt.show()



print('Abnormal Heart Beats')


for file in abnormal_files:
    playsound("Abormal/" + file)
    
    wave_file = wave.open('Abnormal/' + file, 'r')
    frames = wave_file.readframes(-1)

    frames = np.frombuffer(frames, dtype=np.int16)    
    wave_file.close()

    
    plt.plot(frames)
    plt.gcf().set_size_inches(2, 2)
    plt.show()
