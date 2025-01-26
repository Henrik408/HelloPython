#-----------------------------------

""" file = open("file.txt","w")
number_of_characters_written = file.write("snail")
file.close()
print("number_of_characters_written", number_of_characters_written) """

#-----------------------------------

""" countries = ["Albania", "Belgium", "Canada", "Denmark", "Ethiopia", "France"]
filenames = ['a.txt', 'b.txt', 'c.txt', 'd.txt', 'e.txt', 'f.txt']



for file_name, country_name in zip(filenames, countries):
    
    file = open(file_name,"w")
    num_chars_written = file.write(country_name)
    file.close()

    print(f"Written '{country_name}' to {file_name} with {num_chars_written} characters.")
    
    #print(file_name, country_name) """

