# load existing items 
# list items
# mark items as complete
# save remaining items
import json

file_name = "todo_list.json"




def load_task():
    try:
      with open(file_name, "r") as file:
         return json.load(file)
    except:
        print("Failed to save .")
    
    
    
    
def save_task(tasks):
    try:
      with open(file_name, "w") as file:
         return json.dump(tasks, file)
    except:
     return {"tasks": []}
def view_task(tasks):
    tasks_list = tasks["tasks"]
    if len(tasks_list) == 0:
        print("No Tasks available.")
    else:
        print("Your todo list is: ")
        for idx, task in enumerate(tasks_list):
            status = "[Completed]" if task["completed"] else "[pending]"
            print(f"{idx +1}.  {task['description']} | {status}")
def create_task(tasks):
    description = input("Enter your task: ")
    if description:
        tasks["tasks"].append({"description": description, "completed": False})
        save_task(tasks)
        print("Added Successfully")
    else:
        print("Description Cannot be empty")
def mark_task_complete(tasks):
    view_task(tasks)
   
    try:
         task_number = int(input("Enter the task number to mark as completed: ").strip())
         if 1 <= task_number <= len(tasks):
            tasks["tasks"][task_number - 1]["completed"] = True
            save_task(tasks)
            print("Task marked as completed")
         else:
            print("Enter avalid number")
    except:
        print("Enter a number.")
       

def main():
    tasks = load_task()
    
    while True:
        print("\nTo-Do List Manager")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Exit")
        choice = input("Enter Your Choice: ").strip()
        
        if choice == "1":
            view_task(tasks)
        elif choice == "2":
            create_task(tasks)
        elif choice == "3":
            mark_task_complete(tasks)
        elif choice == "4":
            
            print("Welcome Again!!")
            break
        else:
            print("Please Enter avalid number. Try again!.")
    
        
    

main()
