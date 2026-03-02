# load existing items 
# list items
# mark items as complete
# save remaining items

def load_task():
    pass
def save_task():
    pass
def view_task():
    pass
def create_task():
    pass
def mark_task_complet():
    pass

def main():
    tasks = load_task()
    
    while True:
        print("\nTo-Do List Manager")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Print Task")
        choice = int(input("Enter Your Choice")).strip()
        
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
    
        
    


