import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt1
import sys
import sqlite3



def viewg(g1, picname, name):
    

    height=[]
    bars = ()
    bars= tuple(g1.keys())
    print(type(g1.values()))
    height= list(g1.values())
    print(bars, height)
    
    y_pos = np.arange(len(bars))
    plt.bar(bars,height, color=['blue', 'cyan', 'orange','red','yellow'])
    plt.xlabel('')
    plt.ylabel('')
    plt.title(str(name)+' Graph')
    plt.savefig('D:\\Django\\EMS\\webapp\\static\\assets\\images\\'+str(picname))
    plt.clf()


if __name__ == "__main__":
    d={'jan':2,'feb':23}
    viewg(d)



