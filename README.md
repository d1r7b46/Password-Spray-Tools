# Password Spray Tools
A growing collection of tools around email idenfitication, creation, & verification. 

## DomainExtractor
From user input of a domain name, extract email addresses into a new file. 

The 'DomainExtractor' script is a Python tool designed to extract values associated with a specified domain from an input file containing email addresses and their corresponding values. The user provides a domain name, and the script scans the input file, identifying email addresses belonging to the specified domain. It then extracts the values associated with these email addresses and writes them, along with the respective email addresses, to an output file. This tool is useful for quickly organizing and isolating data related to a specific domain from a large dataset.


## DomainAddendum
Add a domain name onto a list of usernames, creating a new file. 

This Python script facilitates the process of appending a domain name to a list of usernames stored in a line-separated text file. Upon receiving the file path and domain name from the user, it reads the usernames, appends the domain to each username, and writes the updated list to a new text file named after the provided domain followed by "_newUsernames.txt".


## Gmail Verification (Google Sheet)
A Google Sheet template to verify gmail email accounts (with instructions). 

WARNING: To work properly, you must open this as a Google Sheet. 
1. Input the emails in Column A that you would like to verify.
2. Copy and paste the same list from Column A to Column B.
3. Select column B and modify the row by choosing Insert > Smart Chips > Convert to people chip

This form will have worked as expected if the People chip causes the True/False to 
trigger in columnn C and if a verified list outputs into column D. 

If this helped you get going on your webapp pentesting journey, I want to know! Please feel free to add or tag me - [My LinkedIn](https://www.linkedin.com/in/angsec/) <br>
If you got a ton out of this and want to buy me a coffee, I won't say no :D [Kofi](https://ko-fi.com/d1r7b46)
