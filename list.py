from tkinter import *
from tkinter import messagebox

def delete_line_from_file(file_name, line_number):
    # Read all lines from the file
    with open(file_name, 'r') as file:
        lines = file.readlines()

    # Check if the line number is valid
    if 0 <= line_number < len(lines):
        # Remove the specified line
        del lines[line_number]

    # Write the modified list back to the file
    with open(file_name, 'w') as file:
        file.writelines(lines)

def edit_line_from_file(file_name, line_number, new_content):
    # Read all lines from the file
    with open(file_name, 'r') as file:
        lines = file.readlines()

    # Check if the line number is valid
    if 0 <= line_number < len(lines):
        # Replace the specified line with new content
        lines[line_number] = new_content + '\n'

    # Write the modified list back to the file
    with open(file_name, 'w') as file:
        file.writelines(lines)

# Read the contents of the list.txt file
with open('list.txt', 'r') as file:
    lines = file.readlines()
    list_contents = ''.join(lines)
    if lines:
        num = int(lines[-1].split('.')[0])  # Get the number from the last line
    else:
        num = 0  # Start from 0 if the file is empty

def add_task():
    task = task_entry.get().strip()
    if task:
        global num
        num += 1  # Increment the number for the new task
        task = f"{num}. {task}\n"
        text_widget.config(state=NORMAL)
        text_widget.insert(END, task)
        text_widget.config(state=DISABLED)
        task_entry.delete(0, END)  # Clear the input box
        with open('list.txt', 'a') as file:
            file.write(task)

def clear_list():
    global num
    text_widget.config(state=NORMAL)
    text_widget.delete("1.0", END)
    text_widget.config(state=DISABLED)
    num = 0  # Reset the task number
    with open('list.txt', 'w') as file:
        file.write('')

def instructions():
    messagebox.showinfo('Instructions', 'Right here')

def center_window(window, width=1100, height=900):
    # Get the screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calculate the position to center the window
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    # Set the window's size and position
    window.geometry(f'{width}x{height}+{x}+{y}')

# Create the main window
window = Tk()
window.title("To-Do List")

# Center the window
center_window(window)

# Create a frame for the Text widget and scrollbar
text_frame = Frame(window)
text_frame.grid(row=0, column=0, rowspan=2, sticky="nsew", padx=(10, 0))  # Remove right padding

scrollbar = Scrollbar(text_frame)
scrollbar.pack(side=RIGHT, fill=Y)

# Create a horizontal scrollbar
h_scrollbar = Scrollbar(text_frame, orient=HORIZONTAL)
h_scrollbar.pack(side=BOTTOM, fill=X)

text_widget = Text(text_frame, font=("Arial", 20), wrap=NONE, yscrollcommand=scrollbar.set, xscrollcommand=h_scrollbar.set)
text_widget.insert(END, list_contents)
text_widget.config(state=DISABLED)  # Make the Text widget read-only
text_widget.pack(side=LEFT, expand=True, fill=BOTH)

scrollbar.config(command=text_widget.yview)
h_scrollbar.config(command=text_widget.xview)

# Create an input box on the top right
input_frame = Frame(window)
input_frame.grid(row=0, column=1, sticky="ne", padx=10, pady=10)

task_entry = Entry(input_frame, font=("Arial", 14), width=30)
task_entry.pack(pady=5)  # Single-line input box

button_width = 20  # Set a fixed width for all buttons

add_button = Button(input_frame, text="Add Task", font=("Arial", 14), width=button_width, command=add_task)
add_button.pack(pady=5)

# Add buttons to the input_frame, stacking them vertically
clear_button = Button(input_frame, text="Clear Tasks", font=("Arial", 14), width=button_width, command=clear_list)
clear_button.pack(pady=5)

delete_button = Button(input_frame, text="Delete Task", font=("Arial", 14), width=button_width)
delete_button.pack(pady=5)

edit_button = Button(input_frame, text="Edit Task", font=("Arial", 14), width=button_width)
edit_button.pack(pady=5)

# Add a frame for the exit button at the bottom
exit_frame = Frame(window)
exit_frame.grid(row=1, column=1, sticky="s", padx=10, pady=10)

instructions_button = Button(exit_frame, text="Instructions", font=("Arial", 14), width=button_width, command=instructions)
instructions_button.pack(pady=5)

exit_button = Button(exit_frame, text="Exit", bg='#ffcccc', font=("Arial", 14, "bold"), width=18, command=window.quit)
exit_button.pack()

# Configure grid weights to allocate 60% width to column 0 and 40% to column 1
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=0)
window.grid_rowconfigure(2, weight=1)  # Ensure the exit button stays at the bottom
window.grid_columnconfigure(0, weight=1)  # 60% of the width
window.grid_columnconfigure(1, weight=0)  # 40% of the width

window.mainloop()

#Slice the first index which is the number
#Then add 1 to the number for the next line
"""
    elif choice == 'delete':
        file_name = 'list.txt'
        line_number = int(input("Enter the line number you wish to delete: ")) - 1
        delete_line_from_file(file_name, line_number)
    elif choice == 'edit':
        edit_number = int(input("Enter the line number you wish to edit: ")) - 1
        new_content = input("Enter the new content for the task: ")
        edit_line_from_file('list.txt', edit_number, new_content) 
"""