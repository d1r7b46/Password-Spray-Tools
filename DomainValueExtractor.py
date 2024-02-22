def separate_domain_values(domain, input_file_path):
    domain_values = []

    # Convert domain to lowercase
    domain = domain.lower()

    # Read the input file
    with open(input_file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            parts = line.strip().split('@')
            if len(parts) >= 2:
                email_domain = parts[-1].lower()
                if domain in email_domain:
                    value = parts[0] if len(parts) > 1 else None
                    if value:
                        domain_values.append(value + '@' + email_domain)

    # Write domain values to the output file
    if domain_values:
        output_file_path = f"{domain.replace('.', '_')}_values.txt"
        with open(output_file_path, 'w') as file:
            for value in domain_values:
                file.write(value + '\n')

        print(f"Values associated with the domain '{domain}' have been saved to {output_file_path}")
    else:
        print(f"No values found for the domain '{domain}' in the input file.")

if __name__ == "__main__":
    domain = input("Enter domain name (e.g., domainname.com): ")
    input_file_path = input("Enter path to the input file: ")

    separate_domain_values(domain, input_file_path)
