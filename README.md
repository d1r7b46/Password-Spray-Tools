# DomainExtractor
From user input of a domain name, extract email addresses into a new file. 

The 'DomainExtractor' script is a Python tool designed to extract values associated with a specified domain from an input file containing email addresses and their corresponding values. The user provides a domain name, and the script scans the input file, identifying email addresses belonging to the specified domain. It then extracts the values associated with these email addresses and writes them, along with the respective email addresses, to an output file. This tool is useful for quickly organizing and isolating data related to a specific domain from a large dataset.

# DomainAddendum
Add a domain name onto a list of usernames, creating a new file. 

This Python script facilitates the process of appending a domain name to a list of usernames stored in a line-separated text file. Upon receiving the file path and domain name from the user, it reads the usernames, appends the domain to each username, and writes the updated list to a new text file named after the provided domain followed by "_newUsernames.txt".

# Upcoming Plans
- prompt for detault list, add domain on end
