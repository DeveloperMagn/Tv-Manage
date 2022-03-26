# button = you click it, then it does stuff
import tkinter

# Import Module
from tkinter import *
import touggle_button_On_Off as BtnT




# Create Object
root = Tk()

# Add Title
root.title('On/Off Switch!')

# Add Geometry
root.geometry("500x300")

# Keep track of the button state on/off
# global is_on
is_on = True

# Create Label
my_label = Label(root,
                 text="The Switch Is On!",
                 fg="green",
                 font=("Helvetica", 32))

my_label.pack(pady=20)


# Define our switch function
def switch():
    global is_on

    # Determine is on or off
    if is_on:
        #on_button.config(image=off)
        on_button.switchOnOff()
        my_label.config(text="The Switch is Off",
                        fg="grey")
        is_on = False
    else:
        on_button.switchOnOff()
        #on_button.config(image=on)
        my_label.config(text="The Switch is On", fg="green")
        is_on = True



on_button = BtnT.OnOffButton(root)




# Execute Tkinter
root.mainloop()






#grid() = geometry manager that organizes widgets in a table-like structure in a parent widget

window = Tk()

titleLabel = Label(window,text="Enter your info",font=("Arial",25)).grid(row=0,column=0,columnspan=2)

#firstNameLabel = Label(window,text="First name: ",width=20,bg="red").grid(row=1,column=0)
firstNameEntry = Entry(window).grid(row=1,column=1)

#lastNameLabel = Label(window,text="Last name: ",bg="green").grid(row=2,column=0)
lastNameEntry = Entry(window).grid(row=2,column=1)

#emailLabel = Label(window,text="email: ",bg="blue").grid(row=3,column=0)
emailEntry = Entry(window).grid(row=3,column=1)

submitButton = Button(window,text="Submit").grid(row=4,column=0,columnspan=2)

window.mainloop()