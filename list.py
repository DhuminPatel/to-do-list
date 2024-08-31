from tkinter import *

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

# Use messagebox to show error warning

with open('list.txt', 'r') as file:
    list_contents = file.read()

window = Tk()
window.title("To-Do List")
window.geometry("900x900")

# Create a frame for the Text widget and scrollbar
text_frame = Frame(window)
text_frame.grid(row=0, column=0, rowspan=2, sticky="nsew", padx=20, pady=20)

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


# Configure the horizontal scrollbar to control the Text widget's horizontal view
h_scrollbar.config(command=text_widget.xview)

# Create an input box on the top right
input_frame = Frame(window)
input_frame.grid(row=0, column=1, sticky="ne", padx=10, pady=10)

task_label = Label(input_frame, text="Enter the task:", font=("Arial", 14))
task_label.pack(pady=5)

task_entry = Text(input_frame, font=("Arial", 14), width=30, height=5)
task_entry.pack(pady=5)  # Increase the height of the input box

button_width = 20  # Set a fixed width for all buttons

add_button = Button(input_frame, text="Add Task", font=("Arial", 14), width=button_width)
add_button.pack(pady=5)

# Add buttons to the input_frame, stacking them vertically
clear_button = Button(input_frame, text="Clear Tasks", font=("Arial", 14), width=button_width)
clear_button.pack(pady=5)

delete_button = Button(input_frame, text="Delete Task", font=("Arial", 14), width=button_width)
delete_button.pack(pady=5)

edit_button = Button(input_frame, text="Edit Task", font=("Arial", 14), width=button_width)
edit_button.pack(pady=5)

exit_button = Button(input_frame, text="Exit", font=("Arial", 14), width=button_width, command=window.quit)
exit_button.pack(pady=5)
# Configure grid weights
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=0)
window.grid_columnconfigure(0, weight=3)
window.grid_columnconfigure(1, weight=1)

window.mainloop()

#Slice the first index which is the number
#Then add 1 to the number for the next line

with open('list.txt', 'r') as file:
    lines = file.readlines()
    if lines:
        num = int(lines[-1].split('.')[0])  # Get the number from the last line
    else:
        num = 0  # Start from 0 if the file is empty

choice_true = True
while choice_true:
    choice = input("What would you like to do? (add, view, clear, delete, edit, exit): ").lower()
    if choice == 'add':
        append = input("Enter the task you wish to add: ")
        num += 1  # Increment the number for the new task
        var = f"{num}. {append}\n"
        with open('list.txt', 'a') as file:
            file.write(var)
    elif choice == 'view':
        with open('list.txt', 'r') as file:
            lines = file.readlines()
            if lines == []:
                print("Empty list")
            for line in lines:
                print(line, end='')
    elif choice == 'clear':
        file_name = 'list.txt'
        with open(file_name, 'w') as file:
            file.write('')
    elif choice == 'delete':
        file_name = 'list.txt'
        line_number = int(input("Enter the line number you wish to delete: ")) - 1
        delete_line_from_file(file_name, line_number)
    elif choice == 'edit':
        edit_number = int(input("Enter the line number you wish to edit: ")) - 1
        new_content = input("Enter the new content for the task: ")
        edit_line_from_file('list.txt', edit_number, new_content) 
    elif choice == 'exit':
        choice_true = False