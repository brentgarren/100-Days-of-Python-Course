#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
        
letter_file_path = "Intermediate_day15-44\Day 24 Read and write\project\input\Letters\starting_letter.txt"   
finished_letter_path = "Intermediate_day15-44\Day 24 Read and write\project\output\{name}_invitation.txt"
names_file_path = "Intermediate_day15-44\Day 24 Read and write\project\input\Names\invited_names.txt"

     
with open(names_file_path) as file:
    content = file.readlines()
    for name in content:
        name = name.strip()
        with open(letter_file_path) as letter:
            draft_letter = letter.read()
            finished_letter = draft_letter.replace("[name]", name)
            with open(finished_letter_path, "w") as file:
                file.write(finished_letter)
                print(f"Finished the letter to {name}")
            
        
