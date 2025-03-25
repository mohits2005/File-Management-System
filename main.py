import os

def create_file(filename):
    try:
        with open(filename, 'x') as f:
            print(f"File name {filename} created successlly !")
    except FileExistsError:
        print(f"File {filename} already exisits !")
    except Exception as e:
        print("An error occured !")
    
def view_All_files():
    files = os.listdir()
    if not files:
        print("No files Found")
    else:
        print("Files Found in directory !")
        for file in files:
            print(file)
        
def delete_files(filename):
    try:
        file = os.remove(filename)
        print(f"file named {filename} has been removed succesully !")
    except FileNotFoundError:
        print("File not found !")
        
    except Exception as e:
        print("An error occured !")
        
def read_file(filename):
    try:
        with open(filename, "r") as f:
            content = f.read()
            print(f"Content of the file {filename} is : \n{content}")
    except FileNotFoundError:
        print(f"File name {filename} does not exist")
        
    except Exception as e:
        print("An error occured !")
        
def edit_file(filename):
    try:
        with open(filename, "a") as f:  
            content = input("Enter the data to add !")
            edit = f.write(content + "\n")
            print(edit)
            print(f'Content added to file {filename} Successfully !')
    except FileNotFoundError:
        print(f"File {filename} does not exist !")
        
    except Exception as e:
        print("An error occured !")
        
def main():
    while True:
        print("WELCOME TO FILE MANAGEMENT APP")
        print('1:  Create file')
        print('2:  View file')
        print('3:  Delete file')
        print('4:  Readfile')
        print('5:  Edit file')
        print('6: EXIT')
        
        choice = input("Enter the choice: ")
        
        if choice == "1":
            filename = input("Enter the flename to create: ")
            create_file(filename)
        elif choice == "2":
            view_All_files(filename)
        elif choice == "3":
            filename = input("Enter the filename to delete: ")
            delete_files(filename)
        elif choice == "4":
            filename = input("Enter the filename to Read: ")
            read_file(filename)
        elif choice == "5":
            filename = input("Enter the name of the file to edit")
        elif choice == "6":
            print('Closing the program')
            break
        else:
            print("Invalid synstax!")      
            
main()     
            