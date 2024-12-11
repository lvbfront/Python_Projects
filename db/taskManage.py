import sqlite3
from pathlib import Path
import time

msg = (
    "Welcome to the tasks program, choose from the options\n"
    "'a' => Add New Task\n"
    "'d' => Delete A Task\n"
    "'s' => Show All Tasks\n"
    "'u' => Update A Task\n"
    "'q' => Quit"
)



options = ['a', 's', 'u', 'q', 'd']


try:
    sqlconnect = sqlite3.connect(Path.home() / Path(r"C:\Users\abdu4\OneDrive\سطح المكتب", 'toDo.db'))
    crsr = sqlconnect.cursor()

except:
    print("faild to connect")

finally:
    if(sqlconnect):

        command = """ CREATE TABLE if not exists tasks(
        id INTEGER,
        task_name VARCHAR(20),
        description TEXT)"""

        crsr.execute(command)
                
        def show_task():
            crsr.execute(f" select * from tasks where id = '{id}'")
            result = crsr.fetchall()
            print("---------------------------")
            print(f"you have '{len(result)}' tasks: ")

            if len(result) > 0:
                for task in result:
                    print(f"Task name: {task[1]} ")
                    print(f"Task Description: {task[2]}")
                    print("-----------------")
            sqlconnect.commit()




        def del_task():
            task_name = input("write the tsk name that you want to delete: ")
            crsr.execute(f" delete from tasks where task_name = '{task_name}' and id = '{id}' ")
            sqlconnect.commit()

        def add_new():
            task_name = input("write task: ").strip()
            des = input('description the task: ').strip()
            crsr.execute(f"INSERT INTO tasks (id, task_name, description) VALUES({id}, '{task_name}', '{des}')")
            sqlconnect.commit()



        def update_task():

            task_name = input("write the task name that you want to change: ").strip()
            crsr.execute("SELECT * FROM tasks WHERE task_name = ? AND id = ?", (task_name, id))
            result = crsr.fetchall()
            #print(result)

            if not result:
                print("there is no task with this name.")

            else:
                des = input("write the new description: ").strip()
                crsr.execute(
                    f"update tasks set description = '{des}' where task_name = '{task_name}' and id = '{id}'  "
                
                )
            sqlconnect.commit()
            print("the task has been updated :)")
        
        
        

        run = True
        id = int(input("enter you id (must be a number!)").strip())
        count = 0
        while(run):
            if count == 0:

                print(msg)
                count =+ 1
            else:
                print("'a' => Add New Task\n"
                        "'d' => Delete A Task\n"
                        "'s' => Show All Tasks\n"
                        "'u' => Update A Task\n"
                        "'q' => Quit")

            user_input = input('Please choose an option : ').strip().lower()


            if user_input in options:

                if user_input == 'a':
                    add_new()
                if user_input == 's':
                    show_task()
                if user_input == 'u':
                    update_task()
                if user_input == 'q':
                    run = False
                if user_input == 'd':
                    del_task()
                    
    else:
        print("not found")
    sqlconnect.close()
                



