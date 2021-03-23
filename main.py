from tkinter import *
import pandas as pd

def isnan(str) : 
    return str != str

def out() : 
    
    for i in symptoms : 
        if var[i].get() == 1 :
            user.append(i)
            
    freq = dict()
    maxfreq = 0
    
    for x in user:
        for i in range (1, m) :
            if isnan(graph[idx[x]][i]) == 1:
                break
            val = freq.setdefault( graph[idx[x]][i], 0)
            freq[ graph[idx[x]][i]] = val + 1
            maxfreq = max(maxfreq, val + 1)

    mostProbable = []
    lessProbable = []
    
    for key,val in freq.items() :
        if val == maxfreq :
            mostProbable.append(key)
        elif val == maxfreq - 1 :
            lessProbable.append(key)
        
    print(mostProbable)
    print(lessProbable)

#graph reading
graph = pd.read_csv("datacsv.csv").values
n = len(graph) #no. of rows
m = len(graph[0]) #no of cols

symptoms = [ graph[i][0] for i in range(n) ]
idx = dict()

for i in range(n) :
    idx[symptoms[i]] = i

user = []
root = Tk()
root.title("Disease Predictor")
var = dict()

for i in symptoms :
    var[i] = IntVar()
    chk = Checkbutton(root, text = i, variable = var[i], width = 20)
    chk.pack()
    
sub = Button(root, text = "submit", command = out)
sub.pack()
root.mainloop()
