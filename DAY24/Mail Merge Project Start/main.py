#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
from typing import final

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("./Input/Names/invited_names.txt") as name_list_file:
    name_list = name_list_file.readlines()

# print(name_list)

with open("./Input/Letters/starting_letter.txt") as starting_letter_file:
    starting_letter = starting_letter_file.read()
    for name in name_list:
        stripped_name = name.strip('\n')
        new_letter = starting_letter.replace("[name]",stripped_name)
        with open(f"./Output/ReadyToSend/letter_to_{stripped_name}",mode='w') as final_letter:
            final_letter.write(new_letter)
