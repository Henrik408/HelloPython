# hallo Hallo 22

todos = []

while True:
    user_action = input("Type add, show, edit, exit: ")
    user_action = user_action.strip()

    match user_action:

        case "add": 
            todo = input("Enter to do: ")
            todos.append(todo)

        case "show":
            for index,item in enumerate(todos):
                print(index, " - ", item)

        case "edit":
            number = int(input("Number of todo to edit: "))
            number = number-1

            new_todo = input("Enter new todo: ")

            todos[number] = new_todo
            
        case "exit":
            break


print("bye")

