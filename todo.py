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
     return print("Failed to save .")
    
    
    
    
def save_task(tasks):
    try:
      with open(file_name, "w") as file:
         return json.dump(tasks, file)
    except:
     return {"tasks": []}
def view_task():
    pass
def create_task():
    pass
def mark_task_complet():
    pass

def main():
    save_task({"taska": ["what is saved"]})
    tasks = load_task()
    print(tasks)
    
    while True:
        print("\nTo-Do List Manager")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Print Task")
        choice = input("Enter Your Choice: ").strip()
        
        if choice == "1":
            view_task()
        elif choice == "2":
            create_task()
        elif choice == "3":
            mark_task_complet()
        elif choice == "4":
            print("Welcome Again!!")
        else:
            print("Please Enter avalid number. Try again!.")
    
        
    

main()
