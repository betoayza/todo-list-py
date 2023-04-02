from task import Task

print("\nWellcome to TODO list in Python!")

tasks_list = []
# eliminar
# editar

is_running = True
while is_running:
    try:
        option = int(input("""\nWhat yo want to do?
            1. Add task.
            2. Delete task
            3. Complete task
            4. Exit
            Choose: """))

        if option == 4:
            is_running = False

        elif option == 1:
            id_task = len(tasks_list) + 1
            name = input("\nTask name: ")
            description = input("Description: ")

            options = ["low", "medium", "high"]

            is_running_2 = True
            while is_running_2:
                priority = input("Priority (low, medium, high): ")
                if priority in options:
                    is_running_2 = False
                else:
                    print("\tInvalid option! Try again...")

            state = "Incompleted"

            task = Task(id_task, name, description, priority, state)
            tasks_list.append(task)

            print("\nSuccesful!")

        elif option == 2:
            is_running_3 = True
            while is_running_3:
                try:
                    ID = int(input("ID to delete: "))

                    found = list(filter(lambda t: t.ID == ID, tasks_list))

                    if len(found) == 1:
                        tasks_list.remove(found[0])
                        print("\nDeleted successfully!")
                        is_running_3 = False
                    else:
                        print("\tTask not found :(\n\tTry other...\n")
                except:
                    print("\tThat's not an option, ha! Try again...\n")
        else:  # if option == 3
            is_running_4 = True
            while is_running_4:
                try:
                    ID = int(input("ID task: "))

                    found = list(filter(lambda t: t.ID == ID, tasks_list))

                    if len(found) == 1:
                        for task in tasks_list:
                            if task == found[0]:
                                tasks_list[tasks_list.index(
                                    task)].state = "Completed"
                                print("\nUpdated successfully!")
                                is_running_4 = False
                    else:
                        print("\tTask not found :(\n\tTry other...\n")
                except:
                    print("\tThat's not an option, ha! Try again...\n")
        # print result
        print("\nThe updated list is:")
        if len(tasks_list) == 0:
            print("\tList is empty :/")
        else:
            for task in tasks_list:
                print("\t", task)

    except:
        print("That's not an option, ha! Try again...")
print("\nThanks for try TODO LIST PY!")
