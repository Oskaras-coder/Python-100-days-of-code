#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Names/invited_names.txt", "r") as invited_people:
    inv_people_list = invited_people.read().splitlines()

for names in inv_people_list:
    with open("./Input/Letters/starting_letter.txt", "r") as start_letter:
        final_letter = start_letter.read().replace("[name]", str(names))
        with open(f"./Output/ReadyToSend/letter_for_{names}.txt", "w") as new_letter:
            new_letter.write(final_letter)
        