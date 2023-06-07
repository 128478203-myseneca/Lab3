
# A function that will write a text file to your PC with your name
def write_text_file_with_name():
    name = input("Enter your name: ")
    filename = "output.txt"
    
    with open(filename, "w") as file:
        file.write(name)
    
    print("File was created with the following name", filename)

write_text_file_with_name()

def helloWorld():
    print(‘Hello World’)

helloWorld()