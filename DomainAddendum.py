def add_domain_to_usernames(filename, domain):
    try:
        # Read the usernames from the file
        with open(filename, 'r') as file:
            usernames = file.readlines()

        # Append the domain to each username
        usernames_with_domain = [username.strip() + '@' + domain for username in usernames]

        # Extract the domain name without '.' to use in the output file name
        domain_name = domain.replace('.', '_')

        # Write the updated usernames to a new file
        output_filename = f"{domain_name}_newUsernames.txt"
        with open(output_filename, 'w') as file:
            for username in usernames_with_domain:
                file.write(username + '\n')

        print(f"Usernames with domain '{domain}' added successfully. Output file: {output_filename}")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    filename = input("Enter the path to the text file containing usernames: ")
    domain = input("Enter the domain name to append to the usernames: ")

    add_domain_to_usernames(filename, domain)

if __name__ == "__main__":
    main()
