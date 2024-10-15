import string

def create_usernames(names, format_choice):
    usernames = []

    for name in names:
        for letter in string.ascii_lowercase:  # Loop through letters a to z
            if format_choice == '1':  # flast
                usernames.append(f"{letter}{name}")
            elif format_choice == '2':  # f.last
                usernames.append(f"{letter}.{name}")
            elif format_choice == '3':  # lastf
                usernames.append(f"{name}{letter}")
            elif format_choice == '4':  # last.f
                usernames.append(f"{name}.{letter}")

    return usernames

def main():
    # Read names from a file
    filename = input("Enter the filename with names (one name per line): ")
    try:
        with open(filename, 'r') as file:
            names = [line.strip() for line in file if line.strip()]

        # Check if the file has names
        if not names:
            print("The file is empty or does not contain valid names.")
            return

        print("Choose the naming convention:")
        print("1. flast")
        print("2. f.last")
        print("3. lastf")
        print("4. last.f")

        format_choice = input("Enter the option number (1-4): ")
        
        # Create usernames based on user choice
        usernames = create_usernames(names, format_choice)
        
        # Output to a file (appending)
        output_filename = "generated_usernames.txt"
        with open(output_filename, 'a') as output_file:  # Open in append mode
            for username in usernames:
                output_file.write(username + '\n')
        
        print(f"\nGenerated Usernames have been appended to '{output_filename}'.")

    except FileNotFoundError:
        print("File not found. Please check the filename and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
