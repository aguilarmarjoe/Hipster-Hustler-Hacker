import pickle
from tkinter import *
from tkinter.font import Font
from tkinter import filedialog
from tkinter import messagebox


root = Tk()
root.title('To Do List')
root.geometry("500x500")

# My_font
font = Font(
    family="Roboto Slab",
    size=16,
    weight="bold")

my_font = Font(
    family="League Gothic",
    size=16
)
# frame
my_frame = Frame(root, bg="Purple")
my_frame.pack(pady=10)

# Create and set the message text variable
message_text = StringVar()
message_text.set("Enjoy Using To Do List App.")

# Create and pack the message label
message_label = Label(my_frame, textvariable=message_text, justify="center", font=my_font, bg="Purple", fg="#fff")
message_label.pack(padx=20, pady=20)


top_frame = LabelFrame(my_frame, text="My To Do List", font=('Roboto', 10))
top_frame.pack(pady=10, padx=10)

# listBox

my_list = Listbox(top_frame,
                  font=font,
                  width=50,
                  height=10,
                  bg="ForestGreen",
                  bd=1,
                  fg="#fff",
                  highlightthickness=0,
                  selectbackground="DarkBlue",
                  activestyle=UNDERLINE)
my_list.pack(side=LEFT, fill=BOTH)


# create list
# to_do_list = ["walk", "jump", "hide", "run", "sleep"]
# # add list to the box
# for item in to_do_list:
#     my_list.insert(END, item.strip().capitalize())
#     my_list.pack(pady=10, padx=10)


# Create Scrollbar
my_scrollbar = Scrollbar(top_frame)
my_scrollbar.pack(side=RIGHT, fill=BOTH)

# Add Scrollbar
my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list.yview)

#  Create a entry box
my_entry = Entry(my_frame, font=("Roboto", 20), width=50, bd=2)
my_entry.pack(pady=5, padx=10)

# Create a button frame
button_frame = Frame(my_frame, height=100, bg="Grey", width=50, borderwidth=20)
button_frame.pack(pady=10)

# Function
def delete_item():
    response =  messagebox.askyesno("Delete Task", "Are you sure you want to delete this task?")
    if response == 1:
        my_list.delete(ANCHOR)

def add_item():
    response = messagebox.askyesno("Add Task", "Are you sure you want to add this task?")
    if response == 1:
        my_list.insert(END, my_entry.get().strip().capitalize())
        my_entry.delete(0, END)

def cross_off_item():
    # Cross item
    response = messagebox.askyesno("Crossed Task", "Are you sure you want to crossed this task?")
    if response == 1:
        my_list.itemconfig(
            my_list.curselection(),
            fg="Black")
        # Get rid of Selection Bar
        my_list.select_clear(0, END)

def uncross_item():
    # Cross item
    response = messagebox.askyesno("Uncrossed Task", "Are you sure you want to uncross this task?")
    if response == 1:
        my_list.itemconfig(
            my_list.curselection(),
            fg="#fff")
        # Get rid of Selection Bar
        my_list.select_clear(0, END)

def delete_crossed():
    # print(my_list.size())
   response = messagebox.askyesno("Delete All Crossed Task", "Are you sure you want to delete all this crossed task?")
   if response == 1:
        count = 0
        while count < my_list.size():
            if my_list.itemcget(count, "fg") == "Black":
                my_list.delete(my_list.index(count))
            else:
                count += 1

def save_list():
    response = messagebox.askyesno("Save List", "Are you sure you want to save this task?")
    if response == 1:
        file_name = filedialog.asksaveasfilename(
            initialdir="C:/Users/User/PycharmProjects/pythonProject/data",
            title="Save File",
            filetypes=(("Dat Files", "*.dat"),
                       ("All Files", "*.*"))
        )
        if file_name:
            if file_name.endswith(".dat"):
                pass
            else:
                file_name = f'{file_name}.dat'
            # Delete Crossed item
            count = 0
            while count < my_list.size():
                if my_list.itemcget(count, "fg") == "Grey":
                    my_list.delete(my_list.index(count))
                else:
                    count += 1
            #  Grab the stuff from the list
            stuff = my_list.get(0, END)

            # Open the file
            output_file = open(file_name, 'wb')

            # Actually add the stuff to the file
            pickle.dump(stuff, output_file)



def open_list():
    file_name = filedialog.askopenfilename(
        initialdir="C:/Users/User/PycharmProjects/pythonProject/data",
        title="Open File",
        filetypes=(("Dat Files", "*.dat"),
                   ("All Files", "*.*"))
    )

    if file_name:
        # Delete current open list
        my_list.delete(0, END)
        
        # Open File Name
        input_file = open(file_name, 'rb')

        # Load data from the file
        stuff = pickle.load(input_file)

        # Output stuff to the screen
        for item in stuff:
            my_list.insert(END, item)

def clear_list():
    response = messagebox.askyesno("Clear List", "Are you sure you want to clear all task?")
    if response == 1:
        my_list.delete(0, END)

# Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Add items to the menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)

# add dropdown item
file_menu.add_command(label="Save List", command=save_list)
file_menu.add_command(label="Open List", command=open_list)
file_menu.add_separator()
file_menu.add_command(label="Clear List", command=clear_list)



# Add buttons
delete_button = Button(button_frame, text="Delete Item", command=delete_item, bg="Purple", fg="#fff", font=('Roboto Slab', 8))
add_button = Button(button_frame, text="Add Item", command=add_item,  bg="Purple", fg="#fff",  font=('Roboto Slab', 8))
cross_off_button = Button(button_frame, text="Cross Off Item", command=cross_off_item,  bg="Purple", fg="#fff",  font=('Roboto Slab', 8))
uncross_button = Button(button_frame, text="Uncross Item", command=uncross_item,  bg="Purple", fg="#fff",  font=('Roboto Slab', 8))
delete_crossed_button = Button(button_frame, text="Delete Cross Item", command=delete_crossed, bg="Purple", fg="#fff",  font=('Roboto Slab', 8))

delete_button.grid(row=0, column=0)
add_button.grid(row=0, column=1, padx=20)
cross_off_button.grid(row=0, column=2)
uncross_button.grid(row=0, column=3, padx=20)
delete_crossed_button.grid(row=0, column=4)

root.mainloop()
