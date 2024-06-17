import json

def add_todo_item(todo_list):
    new_item = input("Enter a new item: ")
    todo_list.append(new_item)
    print(f"{new_item} has been added to your todo list.")

    return todo_list

def show_todo_list(todo_list):
    if not todo_list:
        print("\nYour list is empty.")
    else:
        print("\nYour todo list:")
        for i, item in enumerate(todo_list, 1):
            print(f"{i}. {item}\n")

def del_todo_item(todo_list):
    if not todo_list:
        print("Your list is empty.")
    else:
        show_todo_list(todo_list)
        try:
            del_item = int(input("Choose item number to remove: "))
            if 1 <= del_item <= len(todo_list):
                removed_item = todo_list.pop(del_item - 1)
                print(f"{removed_item} has been successfully deleted.")
            else:
                print("Invalid item number.")
        except ValueError:
            print("Enter a valid number.")

def save_todo_list(todo_list, output_file):
    try:
        with open(output_file, 'w') as file:
            json.dump(todo_list, file)
        print(f"Todo list has been saved to {output_file}.")

    except IOError as e:
        print(f"Error has occurred while saving the file: {e}")
    
def load_todo_list(file_path):
    try:
        with open(file_path, 'r') as file:
            todo_list = json.load(file)
        print(f"Todo list has been loaded from {file_path}.")
    except FileNotFoundError:
        print(f"Cannot find file: {file_path}. Starting with an empty todo list.")
        todo_list = []
    except json.JSONDecodeError:
        print(f"Error decoding JSON from {file_path}. Starting with an empty todo list.")
        todo_list = []
    except IOError as e:
        print(f"Error occurred while loading the file: {e}")
        todo_list = []
        
    return todo_list



file_path = 'todo_file.json'
todo_list = load_todo_list(file_path)

while True:
    print("\nTodo List Menu:")
    print("1. Add a new todo item")
    print("2. Show todo list")
    print("3. Delete a todo item")
    print("4. Save and exit")

    user_choice = input("Choose an option: ")

    if user_choice == '1':
        add_todo_item(todo_list)
    elif user_choice == '2':
        show_todo_list(todo_list)
    elif user_choice == '3':
        del_todo_item(todo_list)
    elif user_choice == '4':
        save_todo_list(todo_list, file_path)
        break
    else:
        print("Wrong input. Choose valid option.")

