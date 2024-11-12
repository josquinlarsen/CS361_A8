Microservice A - Artist Wikipedia Search

This program is written in Python3 and you will need Python3 to run the microservice.
This can be verfied with the command:
```
Python3 --version
```
or 
```
Python --version
```
If this results in an error, or 'command not found'. Download Python from:
https://www.python.org/downloads/

For Windows, terminal refers to the Command Prompt

# Note: if you have Python installed and Python3 does not work, use Python in the terminal.

To begin:
- download msa_client.py and msa_server.py
- for ease of use, save them in the same directory (these direction assume they are saved in the same directory)

Open two separate terminals
In each terminal, navigate (cd) to the directory where the files are located
Run this command in the first terminal:
```
Python3 msa_server.py
```

Run this command in the second terminal:

```
Python3 msa_client.py
```

In the msa_client.py terminal enter the name of the artist to search for, enter 'QUIT' to stop the microservice.
