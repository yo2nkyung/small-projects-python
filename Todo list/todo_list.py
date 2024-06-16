todo_list = []

def add_todo_item(todo_list):
    new_item = input("Enter a new item: ")
    todo_list.append(new_item)
    print(f"{new_item} has been added to your todo list.")

    return todo_list

def show_todo_item(todo_list):
    if not todo_list:
        print("Your list is empty.")
    else:
        print("Your todo list:")
        for i, item in enumerate(todo_list, 1):
            print(f"{i}. {item}\n")

def del_todo_item(todo_list):
    if not todo_list:
        print("Your list is empty.")
    else:
        show_todo_item(todo_list)
        try:
            del_item = int(input("Choose item number to remove: "))
            if 1 <= del_item <= len(todo_list):
                removed_item = todo_list.pop(del_item - 1)
                print(f"{removed_item} has been successfully deleted.")
            else:
                print("Invalid item number.")
        except ValueError:
            print("Enter a valid number.")

    return


add_todo_item(todo_list)
show_todo_item(todo_list)
del_todo_item(todo_list)
