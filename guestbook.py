def add_note(note):
    with open("guestbook.txt", "a") as f:
        f.write(note + "\n")
    print("The given content is written to the file successfully!")

def list_notes():
    print("List of notes in the file:")
    with open("guestbook.txt", "r") as f:
        for line in f:
            print(line.strip())

def edit_note():
    line_num = int(input("Enter the line number of the note to be edited: "))
    new_note = input("Enter the new content of the note: ")
    with open("guestbook.txt", "r") as f:
        notes = f.readlines()
    if line_num <= len(notes):
        notes[line_num-1] = new_note + "\n"
        with open("guestbook.txt", "w") as f:
            for note in notes:
                f.write(note)
        print("The note has been edited successfully!")
    else:
        print(f"There is no note at line number {line_num}.")

def delete_note():
    line_num = int(input("Enter the line number of the note to be deleted: "))
    with open("guestbook.txt", "r") as f:
        notes = f.readlines()
    if line_num <= len(notes):
        del notes[line_num-1]
        with open("guestbook.txt", "w") as f:
            for note in notes:
                f.write(note)
        print("The note has been deleted successfully!")
    else:
        print(f"There is no note at line number {line_num}.")

def main():
    while True:
        command = input("Enter command (new, list, edit, delete, or exit): ")
        if command == 'new':
            note = input("Enter the content of the new note: ")
            add_note(note)
        elif command == 'list':
            list_notes()
        elif command == 'edit':
            edit_note()
        elif command == 'delete':
            delete_note()
        elif command == 'exit':
            print("Exiting the guestbook...")
            break
        else:
            print("Invalid command.")

if __name__ == '__main__':
    main()
