#program by Chris Tettey
from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import tkinter
from array import array
import numpy as np
import sys
import os
os.getcwd()
from PIL import Image, ImageTk
#from breezypythongui import EasyFrame


#creating the window
root = tkinter.Tk()
root.geometry("1200x700")
root.title("Table Tennis Ranking Calculator")

#opening notebook so Tabs can be used
notebook = ttk.Notebook(root)
tab1 = Frame(notebook)
tab2 = Frame(notebook)

#placing and naming the tabs
notebook.add(tab1, text= "Rating Calculator")
notebook.add(tab2, text= "Tutorial")
notebook.pack(expand=True, fill= "both")

#reset everything 
def reset():
    ratingEntry.delete(0, END)
    wonEntry.delete(0, END)
    lostEntry.delete(0, END)
    newRatingLabel.config(text = "Your new rating is: ")
    

#confirm if exit
def confirmExit():
    response = messagebox.askyesno("Confirm Exit", "Are you sure you want to exit?")
    if response is True:
        root.destroy()
    elif response:
        return

def onClick():
    Submit()



def Submit():

    while True:
        try:
            rating = int(ratingEntry.get())
            won = (wonEntry.get())
            lost = (lostEntry.get())
            ratingCalculation()    
            break
        except ValueError:
            messagebox.showerror(message= "Make sure rating box isn't empty and do not enter letters or decimals in any boxes")
            break
    #if rating == "":
        #messagebox.showerror(message= "Make sure rating box isnt empty")
    #elif rating or won or lost 
#full rating calculator
def ratingCalculation():
    #get user entered rating wins and losses 
    rating = int(ratingEntry.get())
    won = (wonEntry.get())
    lost = (lostEntry.get())

    #initializing variables used to find final rating
    addPoints = 0
    losePoints = 0
    newRating = 0

#check if there is nothing entered in the wins section
    if won == "":
        addPoints = 0
    else: 
        #place ratings of people won against in an array
        wonList = [int(i) for i in won.split(" ")]
        #loop through array
        for i in wonList:
            #if won against someone with no rating it doesnt affect points added
            if rating == 0:
                addPoints += 0
                #different thresholds for adding points
            else:
                if ((i - rating) >= 238):
                    addPoints += 50  
                elif ((i - rating) >= 213):
                    addPoints += 45
                elif ((i - rating) >= 188):
                    addPoints += 40
                elif ((i - rating) >= 163):
                    addPoints += 35                                             
                elif ((i - rating) >= 138):
                    addPoints += 30
                elif ((i - rating) >= 113):
                    addPoints += 25
                elif ((i - rating) >= 88):
                    addPoints += 20
                elif ((i - rating) >= 63):
                    addPoints += 16
                elif ((i - rating) >= 38):
                    addPoints += 13         
                elif ((i - rating) >= 13):
                    addPoints += 10
                elif ((i - rating) >= -50):
                    addPoints += 8
                elif ((i - rating) <= -51):
                    addPoints += 0  

#check if there is nothing entered in the wins section
    if lost == "":
        losePoints = 0
    else:
        #place ratings of people won against in an array
        lostList = [int(j) for j in  lost.split(" ")]
        #loop through array
        for j in lostList:
            if rating == 0:
                losePoints += 0
                #if lost against someone with no rating doesn't affect points lost
            else:
                #different threshholds for points lost
                if ((rating - j) >= 238):
                    losePoints += 50
                elif ((rating - j) >= 213):
                    losePoints += 45
                elif ((rating - j) >= 188):
                    losePoints += 40
                elif ((rating - j) >= 163):
                    losePoints += 35
                elif ((rating - j) >= 138):
                    losePoints += 30
                elif ((rating - j) >= 113):
                    losePoints += 25
                elif ((rating - j) >= 88):
                    losePoints += 20
                elif ((rating - j) >= 63):
                    losePoints += 16
                elif ((rating - j) >= 38):
                    losePoints += 13                
                elif ((rating - j) >= 13):
                    losePoints += 10
                elif ((rating - j) >= -50):
                    losePoints += 8
                elif ((rating - j) >= -187):
                    losePoints += 2
                elif ((rating - j) <= -238):
                   losePoints += 0           

    #calculating new rating           
    pointsGained = addPoints - losePoints
    if lost == "":
        if (pointsGained >= 75) or (rating == 0):
            rating = (min(wonList) + max(wonList))/2
        #avgWin = sum(wonList)/len(wonList)
        #rating = avgWin
            newRating = (rating) + pointsGained
        else:
            newRating = (rating) + pointsGained
    elif won == "":
        if rating == 0:
            rating = min(lostList)
            newRating = (rating) + pointsGained
        else:
            newRating = (rating) + pointsGained
    else:
        matchesList = wonList + lostList
        if (pointsGained >= 75) or (rating == 0):
            #rating = (min(matchesList) + max(matchesList))/2
            rating = (min(lostList) + max(wonList))/2
            #rating = sum(matchesList)/len(matchesList)
            
            newRating = (rating) - pointsGained

        else:
            newRating = (rating) + pointsGained


    newRatingLabel.config(text = "Your new rating is: " + str(newRating))


#asks for rating
ratingLabel = Label(tab1, text="Enter your current rating")
ratingLabel.grid(row=0, column=0, padx=10, pady=10)
ratingEntry = Entry(tab1, width=35, borderwidth=5)
ratingEntry.grid(row=0, column=1, padx=10, pady=10) 

#asks for ratings of people you won against
wonLabel = Label(tab1, text="Enter the ratings of everyone you won against with a space in between entries", wraplength=150)
wonLabel.grid(row=1, column=0, padx=10, pady=10)
wonEntry = Entry(tab1, width=50, borderwidth=5)
wonEntry.grid(row=1, column=1, padx=10, pady=10)

#asks for ratings of people you lost against
lostLabel = Label(tab1, text="Enter the ratings of everyone you lost against with a space in between entries", wraplength=150)
lostLabel.grid(row=2, column=0, padx=10, pady=10)
lostEntry = Entry(tab1, width=50, borderwidth=5)
lostEntry.grid(row=2, column=1, padx=10, pady=10)

#buttons
calculateButton = Button(tab1, text="Calculate", fg="blue", command= onClick)
resetButton = Button(tab1, text="Reset", fg="green", command=reset)
exitButton = Button(tab1, text="Exit", fg="red", command=confirmExit)
calculateButton.grid(row=3, column=1, padx=10, pady=10)
resetButton.grid(row=4, column=0, padx=10, pady=10)
exitButton.grid(row=4, column= 2, padx=10, pady=10)

#shows new rating
newRatingLabel= Label(tab1, text="Your new rating is: " )
newRatingLabel.grid(row=4, column=1, padx=10, pady=10)

#opens the Image
paddleImage = Image.open(r'C:\Users\chris\Documents\Final project table tennis calc\Paddle2.png')
paddleImage = ImageTk.PhotoImage(paddleImage)
#edits the Image
paddleLabel = Label(tab1, image=paddleImage)
paddleLabel.grid(row = 5, column = 0, sticky = N+S+W+E)

#opens the Image
coolImage = Image.open(r'C:\Users\chris\Documents\Final project table tennis calc\cool.png')
coolImage = ImageTk.PhotoImage(coolImage)
#edits the Image
coolLabel = Label(tab1, image=coolImage)
coolLabel.grid(row = 5, column = 4, sticky = N+S+W+E)

#Tutorial tab text
tutorialStart= Label(tab2, text="Welcome to the table tennis ranking calculator by Chris Tettey! " ,justify= LEFT, font='Helvetica 18 bold')
tutorialStart.grid(row= 0, column= 0, padx= 20, pady= 20)

tutorialBody = Label(tab2, text=" To use the calculator, all you have to do is enter your current rating in the top text box. As you win and lose matches add the ratings of those people in their corresponding areas. If you don't win any matches, leave its corresponting box empty. If you don't lose any matches leave its box empty. For example, if you lose a match against someone with a rating of 1200, write their rating in the third box.  After entering the results, click the Calculate button! This will calculate your projected ranking and show you right under. If this is your first tournament, enter 0 as your current rating The program will automatically give a projected first rating based on your tournament performance! If you perform well enough, your rating may jump multiple hundreds of points after a tournament! If you gain more than 75 points in a single tournament then your rating will be readjusted to the average of your best win and your worst lost."
                     , justify= LEFT, font='Helvetica 14', wraplength= 650)
tutorialBody.grid(row= 1, column= 0, padx= 20, pady= 20)


tutorialDisc = Label(tab2, text=" Remember that these are projections and may not be exactly what your official USATT rating will be. For more information on how your table tennis ranking is calculated, visit \
                     \n https://www.usatt.org/events-and-results/rating-systems-explained ", justify= LEFT, font='Helvetica 11 italic', wraplength= 650)
tutorialDisc.grid(row=2, column=0, padx= 20, pady= 20)
tutorialDisc.config(background= "darkgoldenrod")




root.mainloop()
