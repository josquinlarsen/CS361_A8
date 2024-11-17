# Microservice A - Artist Wikipedia Search

For Windows, terminal refers to the Command Prompt

This program is written in Python3 and you will need Python3 to run the microservice.
This can be verified in the terminal with the command:
```
Python3 --version
```
or 
```
Python --version
```
If this results in an error, or 'command not found', download Python from:
https://www.python.org/downloads/


<b>Note: if you have Python installed and Python3 does not work, try Python in the terminal.</b>

To begin:
- make sure that the dependencies, ZeroMQ and Wikipedia-API, are installed:
-  ```
   # install ZeroMQ for Python
   pip3 install pyzmq
   ```
   ```
   # install WikipediaAPI for Python, this package requires at least Python3.8
   pip3 install wikipedia-api
   ```
- download msa_client.py and msa_server.py from the github repository https://github.com/josquinlarsen/CS361_A8
- for ease of use, save them in the same directory (these directions assume they are saved in the same directory)

Open two separate terminals.
In each terminal, navigate (cd) to the directory where the files are located
Run this command in the first terminal:
```
Python3 msa_server.py
```

Run this command in the second terminal:

```
Python3 msa_client.py
```
<b>To request a URL:</b>

In the msa_client.py terminal, follow the prompts and enter the name of the artist to search for.

<b>To receive a URL:</b>
If the search is successful, a URL will appear; copy the resultant URL from the command line to search. 
Otherwise an error message will appear. 

The server will run indefinitely until exited by typing control+C in the command line or exiting out of the terminal.

## UML Diagram
<p>
   <image src='a8_uml.png' width=500><br>
</p>

## GIF Walkthrough
<p>
  <image src='msa_a8.gif' width=500><br>
</p>
