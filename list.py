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