# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 15:18:58 2017

@author: christian
"""

import sys
from tkinter import *
from tkinter import messagebox
realNumberValues = []
main = Tk()
main.geometry("810x810")
canvas = Canvas(main,width=810,height=810)

entries = []
for i in range(9):
    for j in range(9):
            entries.append(Text(main,height=2,width=4,font=("Helvetica", 20)))
            
            entries[i*9+j].place(x=85*j,y=i*85)
canvas.pack()
canvas.create_rectangle(0,240,747,255,fill="black")
canvas.create_rectangle(240,0,255,747,fill="black")
canvas.create_rectangle(495,0,510,747,fill="black")
canvas.create_rectangle(0,495,747,510,fill="black")

def countNotZeros(possibilities):
    counter = 0
    position = 0
    for i in range(len(possibilities)):
        if possibilities[i] != 0:
            counter += 1
            position = i
    if counter == 1:
        return counter,position
    return counter,-1

def countZeros(possibilities):
    counter = 0
    position = 0
    for i in range(len(possibilities)):
        if possibilities[i] == 0:
            counter += 1
            position = i
    if counter == 1:
        return counter,position
    return counter,-1


def initialise(sudokuField):
    possibilities = []
    rows = []
    columns = []
    blocks = []
    for i in range(81):
        if sudokuField[i] == 0 :
            possibilities.append([1,2,3,4,5,6,7,8,9])
        else :
            possibilities.append([0])
    
    realNumberValues = sudokuField
    for i in range(9):
        rows.append([realNumberValues[i*9],realNumberValues[(i*9)+1],realNumberValues[(i*9)+2],realNumberValues[(i*9)+3],realNumberValues[(i*9)+4],realNumberValues[(i*9)+5],realNumberValues[(i*9)+6],realNumberValues[(i*9)+7],realNumberValues[(i*9)+8]])
    
    for i in range(9):
        columns.append([realNumberValues[i],realNumberValues[i+9],realNumberValues[i+18],realNumberValues[i+27],realNumberValues[i+36],realNumberValues[i+45],realNumberValues[i+54],realNumberValues[i+63],realNumberValues[i+72]])
    
    for i in range(3):
        for j in range(3):
            blocks.append([realNumberValues[j*3+i*27],realNumberValues[j*3+i*27+1],realNumberValues[j*3+i*27+2],realNumberValues[i*27+j*3+9],realNumberValues[i*27+j*3+10],realNumberValues[i*27+j*3+11],realNumberValues[i*27+j*3+18],realNumberValues[i*27+j*3+19],realNumberValues[i*27+j*3+20]])
    
    print("Row:",rows[8])
    print("Columns:",columns[4])
    print("Blocks:",blocks[7])
    print(realNumberValues[75])
    
    for i in range(9):
        for j in range(9):
            if j+1 in rows[i]:
                for k in range(9):
                    if len(possibilities[i*9+k]) > 1:
                        possibilities[k+i*9][j] = 0
    
    print("2:",possibilities[75])
    
    for i in range(9):
        for j in range(9):
            if j+1 in columns[i]:
                for k in range(9):
                    if len(possibilities[k*9+i]) > 1:
                        possibilities[k*9+i][j] = 0

    print("3:",possibilities[75])
            
    for i in range(3):
        for j in range(3):
            for k in range(9):
                if k+1 in blocks[i*3+j]:
                    for l in range(3):
                        for m in range(3):
                            if len(possibilities[i*27+j*3+l*9+m]) > 1:
                                possibilities[i*27+j*3+l*9+m][k] = 0
    
    print("4:",possibilities[75])
   
    for h in range(9):
        for i in range(3):
            
            for j in range(3):
                tempCache = []
                rowsWithSpace = 0
                rowsFilled = 0;
                
                for k in range(3):
                    for l in range(3):
                        if len(possibilities[i*27+j*3+k*9+l]) > 1:
                            if possibilities[i*27+j*3+k*9+l][h] == h+1:
                                rowsFilled += 1
                    if rowsFilled > 0:
                        rowsWithSpace += 1
                if rowsWithSpace == 1:
                    tempCache = []
                    if len(possibilities[i*27+j*3+k*9]) > 1:
                        tempCache.append(possibilities[i*27+j*3+k*9][h])
                    else:
                        tempCache.append(0)
                    if len(possibilities[i*27+j*3+k*9+1]) > 1:
                        tempCache.append(possibilities[i*27+j*3+k*9+1][h])
                    else:
                        tempCache.append(0)
                    if len(possibilities[i*27+j*3+k*9+2]) > 1:
                        tempCache.append(possibilities[i*27+j*3+k*9+2][h])
                    else:
                        tempCache.append(0)
                    
                    for l in range(9):
                        if len(possibilities[i*27+k*9+l])>1:
                            possibilities[i*27+k*9+l][h] = 0
                    if len(possibilities[i*27+j*3+k*9]) > 1:
                        possibilities[i*27+j*3+k*9][h] = tempCache[0]
                    if len(possibilities[i*27+j*3+k*9+1]) > 1:
                        possibilities[i*27+j*3+k*9+1][h] = tempCache[1]
                    if len(possibilities[i*27+j*3+k*9+2]) > 1:
                        possibilities[i*27+j*3+k*9+2][h] = tempCache[2]

    print("5:",possibilities[75])
    for h in range(9):             
        for i in range(3):
            
            for j in range(3):
                tempCache = []
                columnsWithSpace = 0;
                columnsFilled = 0;
                position = 0
            
                for k in range(3):
                    for l in range(3):
                        if len(possibilities[i*27+j*3+l*9+k]) > 1:
                            if possibilities[i*27+j*3+l*9+k][h] == h+1:
                                position = k
                                columnsFilled += 1;
                    if columnsFilled > 0:
                        columnsWithSpace += 1
                if columnsWithSpace == 1:
                    tempCache = []
                    if len(possibilities[i*27+j*3+position]) > 1:
                        tempCache.append(possibilities[i*27+j*3+position][h])
                    else:
                            tempCache.append(0)
                    if len(possibilities[i*27+j*3+position+9]) > 1:
                        tempCache.append(possibilities[i*27+j*3+position+9][h])
                    else:
                            tempCache.append(0)
                    if len(possibilities[i*27+j*3+position+18]) > 1:
                        tempCache.append(possibilities[i*27+j*3+position+18][h])
                    else:
                            tempCache.append(0)
                    for l in range(9):
                        if len(possibilities[position+l]) > 1:
                            possibilities[position+l][h] = 0
                        else:
                            possibilities[position+l] = [0]
                    if len(possibilities[i*27+j*3+position]) > 1:
                        possibilities[i*27+j*3+position][h] = tempCache[0]
                    if len(possibilities[i*27+j*3+position+9]) > 1:
                        possibilities[i*27+j*3+position+9][h] = tempCache[1]
                    if len(possibilities[i*27+j*3+position+18]) > 1:
                        possibilities[i*27+j*3+position+18][h] = tempCache[2]
    
    print("6:",possibilities[75])
    
    return rows,columns,blocks,possibilities,realNumberValues

def main1(sudokuField):
    rows,columns,blocks,possibilities,realNumberValues = initialise(sudokuField)
    for i in range(81):
        
        if countNotZeros(possibilities[i])[0] == 1:
            realNumberValues[i] = possibilities[i][countNotZeros(possibilities[i])[1]]
            possibilities[i] = [0]
            
    
    full_length = 0
    for i in range(81):
        full_length += len(possibilities[i])
    return realNumberValues

def start(realNumberValues):
    finished = True
    counter = 0
    while countZeros(realNumberValues)[0] != 0:
        beforeHand = realNumberValues
        realNumberValues = main1(realNumberValues)
        
        if realNumberValues == beforeHand:
            counter += 1
        else:
            counter = 0
            
        if counter == 10:
            messagebox.showinfo("Error","No clear answer possible!")
            for i in range(81):
                if len(entries[i].get("1.0")) == 1:
                    entries[i].delete("1.0")
                entries[i].insert("1.0",str(realNumberValues[i]))
            finished = False
            break 
    if finished:
        for i in range(81):
            if len(entries[i].get("1.0")) == 1:
                entries[i].delete("1.0")
            entries[i].insert("1.0",str(realNumberValues[i]))
        messagebox.showinfo("Solved","The solution was computed!")
    return realNumberValues

def getNumbers():
    realNumberValues = []
    for i in range(81):
        if len(entries[i].get("1.0","end-1c")) == 1:
            realNumberValues.append(int(entries[i].get("1.0","end-1c")))
        elif len(entries[i].get("1.0","end-1c")) == 0:
            realNumberValues.append(0)
        else:
           messagebox.showinfo("Error","The input was wrong!")
           realNumberValues = []
           return 0
    return realNumberValues

def setEverything():
    realNumberValues = getNumbers()

    realNumberValues = start(realNumberValues)

           
readyButton = Button(main,command=setEverything,width=20,height=20,text="Ready",bg="red")

readyButton.place(x=750,y=750)
mainloop()    






    


                    