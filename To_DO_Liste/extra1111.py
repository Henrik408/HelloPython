""" products = ['table', 'chair', 'door']
for i, item in enumerate(products):
    print("Product: ", item)
 """

""" seconds = [1.23, 1.45, 1.02, 1.11]
seconds.pop(1)
print(seconds) """


""" mystring = "hello world" 
mystring = mystring.capitalize()
print(mystring)
mylist =  [1,2,3,4,5,6,7,8,9]
print(len(mystring))
print(len(mylist)) """

""" mylist = ['a', 'b', 'c', 'd']
for item in mylist:
    print(len(mylist)) """

""" waiting_lsit = ["sen", "ben","john"]
waiting_lsit.sort()
for i,item in enumerate(waiting_lsit):
    print(f"{i + 1}. {item.capitalize()}") """

""" measurements = [177.8, 175.8, 166.9, 182.5]
measurements.sort()
for item in measurements:
    print(item) """

menu = ["pasta", "pizza", "salad"]
 
# for i, j in enumerate(menu):
#     print(i,j)
#     print(f"{i}.{j}")

""" buttons = [('John', 'Sen', 'Morro'), ('Lin', 'Ajay', 'Filip')]
for first, second, third in buttons:
    print(first, second, third) """

""" file = open("whatever.txt","w")
# file.write("Das ist ein Test")
file.writelines(["LINE1\n", "Line2\n"])
file.close() """

# Bonus Example

""" a = [1,2,3]
b = [10,20,30]
x = list(zip(a,b))

# print(list(x))

for item1, item2 in x:
    print(item1, item2)
    print("HuHu")    

print(list(x)) """
#----------------------------
""" contents = ["abcd11","defg11","hijk11"]
filenames = ["erster.txt","zweiter.txt", "dritter.txt"]

for content, filename in zip(contents,filenames):
    file = open(rf"files\{filename}","+w")
    file.write(content) """

#-----------------------------------

""" file = open("bear.txt","r")
file_contents = file.readlines()
file.close()

for lines in file_contents:
    print(lines)

print("huHu") """


#-----------------------------------

""" File essay.txt
The true meaning of obscurity lies underneath the most delicate structures 
of viscosity. The idea of changing that balance is obscure by itself. """

""" file = open("essay.txt","r")
file_contents = file.readlines()
file.close()

for line in file_contents:
    print(f"The file contains {len(line)} characters")
   
   # print(line.title())

# Corrected

# Open the file in read mode
file = open("essay.txt", "r")
file_contents = file.read()  # Read the entire content as a single string
file.close()

# Calculate the total number of characters
num_characters = len(file_contents)

# Print the result
print(f"The file contains {num_characters} characters.") """


#-----------------------------------

""" countries = ["Albania", "Belgium", "Canada", "Denmark", "Ethiopia", "France"]

for item in countries:
    filename = item + ".txt"

    file = open(filename,"w")
    

    num1 = file.write(item)
    
    file.close()

    print(f"{num1} charracters written in file {filename}") """

#-----------------------------------



""" while True:

    print("what do want: ")
    print("1 - show list")
    print("2 - add new member")
    print("7 - exit")

    menue_nr = int(input("Input Selection: "))

    print(menue_nr)

    match menue_nr :
        case 1 :

            file = open("members.txt","r")
            contents_file = file.readlines()
            file.close()

            for item in contents_file:
                print(item.strip())
                
            print(1)
 

        case 2 :
            new_member = input("New Member: ")
            file = open("members.txt","r")
            contents_file = file.readlines()
            file.close()
            contents_file.append(new_member)

            file = open("members.txt","w")
            file.writelines(contents_file)
        
            print(2)

        case 7:
            break

print("bye")
          """


#-----------------------------------

""" filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for filename in filenames:
    
    filename_dir =rf"files\{filename}" 

    file =open(filename_dir,"w")
    file.write("Hello!!")
    file.close()

    print(filename_dir)
 """
#-----------------------------------

""" import os

# Ensure the directory exists
os.makedirs('files', exist_ok=True)

filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for filename in filenames:
    filename_dir = rf"files\{filename}"
    
    # Open and close the file properly
    with open(filename_dir, "w") as file:
        print(file, filename_dir) """

#------------------------------------------------    



