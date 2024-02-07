with open("./Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter = letter_file.read()

for name in names:
    name = name.strip("\n")
    main_letter = letter.replace("[name]", name)
    with open(f"./Output/ReadyToSend/{name}.txt", "w") as completed_file:
        completed_file.write(main_letter)

