# Define the list of filenames
filenames = ["document", "report", "presentation"]

# Iterate over the filenames using enumerate to get both the index and the name
for index, name in enumerate(filenames):
    # Capitalize the first letter, add a number and dash, and append '.txt'
    modified_name = f"{index}-{name.capitalize()}.txt"
    # Print the modified name
    print(modified_name)
