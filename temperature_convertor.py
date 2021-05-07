# importing tkinter
import tkinter as tk
# By using the "*" we import all tools from tkinter for available instead if multiple separate tools
from tkinter import LabelFrame, Button, Entry, END, messagebox

# creating the Root gui/window by using tkinter
root = tk.Tk()

# Adding a title and setting the size
root.title("Temperature Convertor")
root.geometry("1000x700")

# Creating the Label Frames
celsius_label_frame = LabelFrame(root, text="Celsius to Fahrenheit")
fahrenheit_label_frame = LabelFrame(root, text="Fahrenheit to Celsius")

# Setting the sizes and positions of label frames
celsius_label_frame.place(x=50, y=10, height=300, width=400)
fahrenheit_label_frame.place(x=550, y=10, height=300, width=400)

# Creating celsius entry field and positioning it using place
celsius_entry = Entry(celsius_label_frame, width=20, state="readonly")
celsius_entry.place(x=120, y=120)

# Creating fahrenheit entry field and positioning it using place
fahrenheit_entry = Entry(fahrenheit_label_frame, width=20, state="readonly")
fahrenheit_entry.place(x=120, y=120)


# Defining functions

# Function linked to button that clears all entry fields
# It is used as the command that causes the clear button to function
def clear_entry():
    # Clear celsius entry field
    celsius_entry.delete(0, END)
    # Clear fahrenheit entry field
    fahrenheit_entry.delete(0, END)
    # Clear results field
    results_entry.delete(0, END)


# Function that deals with the conversion of inputted values
# It is used as the command that causes the covert button to function
def temperature_conversion():
    # Attempts to covert any input used in the entry fields
    try:
        # Used to convert celsius to fahrenheit
        if celsius_entry['state'] == "normal" and celsius_entry.get() != "":
            to_fahrenheit = float(celsius_entry.get()) * 9/5 + 32
            results_entry.delete(0, END)
            results_entry.insert(0, to_fahrenheit)
            # Used to convert fahrenheit to celsius
        elif fahrenheit_entry['state'] == "normal" and fahrenheit_entry.get() != "":
            to_celsius = (float(fahrenheit_entry.get()) - 32) * 5/9
            results_entry.delete(0, END)
            results_entry.insert(0, to_celsius)
    # When nothing is entered in the two entry fields display nothing
        else:
            return None
    # If a string is inserted into the entry fields instead of an int an Error will display
    except ValueError:
        messagebox.showerror("Error!", "Please use a number when inserting the temperature!", icon="warning")


# Function to activate the celsius entry field
# It is used as the command that causes the celsius button to function
def activate_celsius():  # ensures that when the button is clicked celsius entry activates
    if celsius_entry['state'] == "normal":
        celsius_entry.config(state="disabled")
    else:  # Disables fahrenheit entry when celsius entry is activated
        celsius_entry.config(state="normal")
        fahrenheit_entry.config(state="disabled")


# Function to activates the fahrenheit entry field.
# It is used as the command that causes the fahrenheit button to function
def activate_fahrenheit():  # ensures that when the button is clicked fahrenheit entry activates
    if fahrenheit_entry['state'] == "normal":
        fahrenheit_entry.config(state="disabled")
    else:  # Disables fahrenheit entry when fahrenheit entry is activated
        fahrenheit_entry.config(state="normal")
        celsius_entry.config(state="disabled")


# Button that activates celsius field
activate_celsius_btn = Button(root, text="Activate", command=activate_celsius)
activate_celsius_btn.place(x=200, y=350)

# Button that activates fahrenheit field
activate_fahrenheit_btn = Button(root, text="Activate", command=activate_fahrenheit)
activate_fahrenheit_btn.place(x=700, y=350)

# Convert Button. positioned using place
convert_button = Button(root, text="Convert", command=temperature_conversion)
convert_button.place(x=300, y=450)

# The Results field. colored using bg="". Positioned using place.
results_entry = Entry(root, bg="green", width=25)
results_entry.place(x=400, y=450, height=50)

# Creating the clear button and positioning it using place
clear_button = Button(root, text="Clear", command=clear_entry)
clear_button.place(x=630, y=450)

# an exit button that uses the command .destroy to exit the wind. it is positioned using place
exit_button = Button(root, text="Exit", command=root.destroy)
exit_button.place(x=475, y=520)

# Ensures that the Window/GUI(root) stays open until the user exits/closes the program
root.mainloop()
