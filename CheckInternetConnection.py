from datetime import datetime

import requests

from itertools import  count 

import matplotlib.pyplot as plt # external module

from matplotlib.animation import FuncAnimation



Counter = count()

global Animation

global file


XVals = [next(Counter)]
YVals = [0]


#file = open("ConnectionLog.txt", 'w')

FileName = datetime.now().strftime("%Y-%m-%d %I-%M-%S")

file = open( (FileName+".txt"), 'w')

#file.write(str(datetime.now()) + "\n \n")


plt.style.use("fivethirtyeight") #graph style


'''
def ConnectionTimedOut():
#
    Animation.event_source.stop()
    #file.close()

    print("Connection Timed Out")

    file.write("Connection Timed Out \n \n")
#
'''


def PrintPingResult():
#
    #some way to not make this function run infinitely

    try:   
        Result = requests.get("https://www.google.com/", timeout = 2)

        ResTime = Result.elapsed.microseconds/10000

        #print(ResTime)

        Result.close()

        return ResTime

    
    except requests.ConnectionError:
        print("Connection Error at "+  str(Counter) +". passing ping as -100")

        file.write("Connection Error \n \n")

        next(Counter)

        return -100

        '''
        if(Result.status_code != 200): 
            Result.close()
            return -50
        '''

    except requests.Timeout:
        #ConnectionTimedOut()

        print("Connection Timed Out at "+  str(Counter) +". passing ping as -100")
        
        file.write("Connection Timed Out \n \n")

        next(Counter)

        return -100


def animate(i):
    AverageResTime = 0.0

    ResTime = []
    
    for i in range(0, 4):
        temp = PrintPingResult()

        ResTime.append(temp)
        
        AverageResTime += temp

    AverageResTime = AverageResTime/4.0

    
    file.write(str(Counter) + "\n")

    file.write(str(ResTime) + ", AverageResTime: " + str(AverageResTime) + "\n \n" )
    
        
    XVals.append(next(Counter))
    YVals.append(AverageResTime)

        
    plt.cla() #clears the graph

    plt.plot(XVals, YVals) #plot new graph



Animation = FuncAnimation(plt.gcf(), animate, interval = 1000)


plt.tight_layout() #add automatic padding to plot
plt.show()


file.close()

print("Execution Complete")