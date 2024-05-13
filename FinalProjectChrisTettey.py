#program by Chris Tettey. This is a table tennis ranking calculator.
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
root.geometry("1250x900")
root.title("Table Tennis Ranking Calculator")

#opening notebook so Tabs can be used
notebook = ttk.Notebook(root)
tab1 = Frame(notebook) #first tab
tab2 = Frame(notebook) #second tab

#placing and naming the tabs
notebook.add(tab1, text= "Rating Calculator") #name of first tab
notebook.add(tab2, text= "Tutorial") #name of second tab
notebook.pack(expand=True, fill= "both")

#reset everything 
def reset():
    ratingEntry.delete(0, END)  #deletes everything in entry box
    wonEntry.delete(0, END)     #deletes everything in won entry box
    lostEntry.delete(0, END)    #deletes everything in lost entry box
    newRatingLabel.config(text = "Your new rating is: ") #deletes new rating
    

#confirm if exit
def confirmExit():
    response = messagebox.askyesno("Confirm Exit", "Are you sure you want to exit?") #shows message box
    if response is True:
        root.destroy() #closes program if user clicks yes
    elif response:
        return  #resumes program if user clicks no

def onClick(): #used to call other methods on click
    Submit()


#checks if valid entries are placed in entry boxes
def Submit(): 

    while True: #continues program if no errors reading user entries
        try:
            rating = int(ratingEntry.get())
            won = (wonEntry.get())
            lost = (lostEntry.get())
            ratingCalculation()    
            break
        except ValueError:  #shows error popup if any issues reading user entries
            messagebox.showerror(message= "Make sure rating box isn't empty and do not enter letters or decimals in any boxes")
            break

#full rating calculator
def ratingCalculation():    
    #update lists with entries from user input
    rating = int(ratingEntry.get())
    won = (wonEntry.get())
    lost = (lostEntry.get())

    #initializing variables used to compute final rating
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
            #no change in rating if opponent has no rating
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
                elif i == 0:
                    addPoints += 0  #if won against someone with no points it doesnt affect rating

#check if there is nothing entered in the losses section
    if lost == "":
        losePoints = 0
    else:
        #place ratings of people lost against in an array
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
                elif j == 0:
                    losePoints += 0           

    #calculating new rating           
    pointsGained = addPoints - losePoints
#doing the official point calculatoins
    if lost == "":  #checking if lost box is empty
        if (pointsGained >= 75) or (rating == 0):     #reevaluate rating if user gains more then 75 points or has a rating of 0       
            rating = (min(wonList) + max(wonList))/2
            newRating = (rating) + pointsGained
        else:
            newRating = (rating) + pointsGained
    elif won == "":     #checking if won box is empty
        if rating == 0: #checking if raiting is 0
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
            
            newRating = (rating - (pointsGained/2))

        else:
            newRating = (rating) + pointsGained


    newRatingLabel.config(text = "Your new rating is: " + str(int(newRating))) #changing what the user sees in the new rating section


#asks for rating
ratingLabel = Label(tab1, text="Enter your current rating")
ratingLabel.grid(row=0, column=0, padx=10, pady=10)
ratingEntry = Entry(tab1, width=35, borderwidth=5) #place where user enters ranking
ratingEntry.grid(row=0, column=1, padx=10, pady=10) 

#asks for ratings of people you won against
wonLabel = Label(tab1, text="Enter the ratings of everyone you won against with a space in between entries", wraplength=150)
wonLabel.grid(row=1, column=0, padx=10, pady=10)
wonEntry = Entry(tab1, width=50, borderwidth=5) #place where user enters ratings of people won against
wonEntry.grid(row=1, column=1, padx=10, pady=10)

#asks for ratings of people you lost against
lostLabel = Label(tab1, text="Enter the ratings of everyone you lost against with a space in between entries", wraplength=150)
lostLabel.grid(row=2, column=0, padx=10, pady=10)
lostEntry = Entry(tab1, width=50, borderwidth=5) #place where user enters ratings of people lost against
lostEntry.grid(row=2, column=1, padx=10, pady=10)

#buttons
calculateButton = Button(tab1, text="Calculate", fg="blue", command= onClick) #calculate button
resetButton = Button(tab1, text="Reset", fg="green", command=reset) #reset button
exitButton = Button(tab1, text="Exit", fg="red", command=confirmExit) #exit button
calculateButton.grid(row=3, column=1, padx=10, pady=10)
resetButton.grid(row=4, column=0, padx=10, pady=10)
exitButton.grid(row=4, column= 2, padx=10, pady=10)

#shows new rating
newRatingLabel= Label(tab1, text="Your new rating is: " ) #starts out empty because nothing has been entered in
newRatingLabel.grid(row=4, column=1, padx=10, pady=10)

#opens the image
paddleImage = Image.open(r'C:\Users\chris\Documents\Final project table tennis calc\Paddle2.png')
paddleImage = ImageTk.PhotoImage(paddleImage)
paddleLabel = Label(tab1, image=paddleImage)
paddleLabel.grid(row = 5, column = 0, sticky = N+S+W+E)

#image alt text
paddleText = Label(tab1, text="Image of my current Table Tennis paddle above")
paddleText.grid(row = 6, column = 0)

#opens the Image
coolImage = Image.open(r'C:\Users\chris\Documents\Final project table tennis calc\cool.png')
coolImage = ImageTk.PhotoImage(coolImage)
#edits the Image
coolLabel = Label(tab1, image=coolImage)
coolLabel.grid(row = 5, column = 4, sticky = N+S+W+E)
#image alt text
coolText = Label(tab1, text="Cool image of people about to play table tennis with dark lighting above ")
coolText.grid(row = 6, column= 4)

#Tutorial tab text
tutorialStart= Label(tab2, text="Welcome to the table tennis ranking calculator by Chris Tettey! " ,justify= LEFT, font='Helvetica 18 bold')
tutorialStart.grid(row= 0, column= 0, padx= 20, pady= 20)

tutorialBody = Label(tab2, text=" To use the calculator, all you have to do is enter your current rating in the top text box. As you win and lose matches add the ratings of those people in their corresponding areas. If you don't win any matches, leave its corresponting box empty. If you don't lose any matches leave its box empty. For example, if you lose a match against someone with a rating of 1200, write their rating in the third box.  After entering the results, click the Calculate button! This will calculate your projected ranking and show you right under. If this is your first tournament, enter 0 as your current rating The program will automatically give a projected first rating based on your tournament performance! If you perform well enough, your rating may jump multiple hundreds of points after a tournament! If you gain more than 75 points in a single tournament then your rating will be readjusted to the average of your best win and your worst lost."
                     , justify= LEFT, font='Helvetica 14', wraplength= 650)
tutorialBody.grid(row= 1, column= 0, padx= 20, pady= 20)


tutorialDisc = Label(tab2, text=" Remember that these are projections and may not be exactly what your official USATT rating will be. For more information on how your table tennis ranking is calculated, visit \
                     \n https://www.usatt.org/events-and-results/rating-systems-explained ", justify= LEFT, font='Helvetica 11 italic', wraplength= 650)
tutorialDisc.grid(row=2, column=0, padx= 20, pady= 20)
tutorialDisc.config(background= "darkgoldenrod") #adds highlight to this statement

root.mainloop()
