import json

priority_map = {'low': 1, 'medium': 2, 'high': 3}

def sort_todo_list(todo_list):
    return sorted(todo_list, key = lambda x: priority_map[x["priority"]])

def add_todo_item(todo_list):
    new_item = input("Enter a new item: ")
    priority = input("Enter the priority: (low, medium, high): ").lower()
    todo_list.append({"item": new_item, "completed": False, "priority": priority})
    print(f"{new_item} with priority {priority} has been added to your todo list.")    
    
    return sort_todo_list(todo_list)

def show_todo_list(todo_list):
    if not todo_list:
        print("\nYour list is empty.")
    else:
        print("\nYour todo list:")
        for i, item in enumerate(todo_list, 1):
            status = "✔️" if item["completed"] else "❌"
            print(f"{i}. {item['item']} [priority: {item['priority']}] {status}\n")

def mark_todo_as_completed(todo_list):
    if not todo_list:
        print("Your todo list is empty.")
    else:
        show_todo_list(todo_list)
        try:
            item_number = int(input("Choose a number to mark as completed: "))
            if 1<= item_number <= len(todo_list):
                todo_list[item_number - 1]["completed"] = True
                print(f"{todo_list[item_number - 1]['item']} has been marked as completed.")
            else:
                print("Invalid item number.")
        except ValueError:
            print("Enter a valid number.")

    return sort_todo_list(todo_list)

def del_todo_item(todo_list):
    if not todo_list:
        print("Your list is empty.")
    else:
        show_todo_list(todo_list)
        try:
            del_item = int(input("Choose item number to remove: "))
            if 1 <= del_item <= len(todo_list):
                removed_item = todo_list.pop(del_item - 1)
                print(f"{removed_item['item']} has been successfully deleted.")
            else:
                print("Invalid item number.")
        except ValueError:
            print("Enter a valid number.")

    return sort_todo_list(todo_list)

def edit_todo_item(todo_list):
    if not todo_list:
        print("Your todo list is empty.")
    else:
        show_todo_list(todo_list)
        try:
            item = int(input("Enter the number of the item to edit: "))
            if 1 <= item <= len(todo_list):
                new_item = input("Enter the new description: ")
                todo_list[item-1]['item'] = new_item
                print(f"Item {item} has been updated to {new_item}.")
            else:
                print("Invalid item number.")
        except:
            print("Enter a valid number.")
    return sort_todo_list(todo_list)

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

def search_todo_items(todo_list):
    if not todo_list:
        print("Your todo list is empty.")
    else:
        search_keyword = input("Enter keyword to search: ").lower()
        '''
        search_result = []        
        for item in todo_list:
            if search_keyword in item["item"]:
                search_result.append(item)
                '''
        search_result = [item for item in todo_list if search_keyword in item["item"]]


        if not search_result:
            print("No result.")
        else:
            print("\nSearch result:")
            for i, item in enumerate(search_result, 1):
                status = "✔️" if item["completed"] else "❌"
                print(f"{i}. {item['item']} [priority: {item['priority']}] {status}\n")


file_path = 'todo_file.json'
todo_list = load_todo_list(file_path)

while True:
    print("\nTodo List Menu:")
    print("1. Add a new todo item")
    print("2. Show todo list")
    print("3. Mark as completed")
    print("4. Delete a todo item")
    print("5. Change item description")
    print("6. Search item")
    print("7. Save and exit")

    user_choice = input("Choose an option: ")

    if user_choice == '1':
        todo_list = add_todo_item(todo_list)
    elif user_choice == '2':
        show_todo_list(todo_list)
    elif user_choice == '3':
        todo_list = mark_todo_as_completed(todo_list)
    elif user_choice == '4':
        todo_list = del_todo_item(todo_list)
    elif user_choice == '5':
        todo_list = edit_todo_item(todo_list)
    elif user_choice == '6':
        search_todo_items(todo_list)
    elif user_choice == '7':
        save_todo_list(todo_list, file_path)
        break
    else:
        print("Wrong input. Choose valid option.")

