#Function to get menu

def get_menu():
        display_menu = """
To-Do List Manager
1. Add a task
2. View tasks
3. Mark task as complete
4. Delete a task
5. Exit
    Enter our choice: 
    Enter the task:
                            """
        return display_menu

#Driver class for to-do list manager
print(get_menu())
user_selection = int(input("Enter a selection: "))

list = []
todo = True
while todo:
        match user_selection:
                case 1:
                        proceed = True       
                        while proceed:
                                user_choice = input("Add a task: ")
                                list.append(user_choice)
                                print(list)
                                reenter_option = int(input("Enter 1 to add another task or 2 to quit: "))
                                if reenter_option == 1:
                                        proceed = True
                                elif reenter_option == 2:
                                        proceed = False

                case 2:
                        print("View Tasks")
                        print(list)

                case 3:
                        print("Mark Task as complete")


                case 4:
                        print("Delete a task")

                case 5:
                        todo = False


#print(list)




 

