# Website Connectivity Checker
Have you ever gone to a website and found that it was not able to be connected to? It's happened to me quite a few times. When this happens, I usually
go to websites that are dedicated to finding out if the connection problem lies with the website or your own internet. However, it's possible to 
check using your own local computer, and to even check multiple websites at once!

## Site checker module
This module, which has been encapsulated in a folder called "site_checker" contains several files that make up the site checker and allow the user to use
the command line to check the status of any website.

### __init__.py
This file is what allows the "site_checker" folder to act as a module, and enables it as a python package.

### __main__.py
This file contains the functions that activate the url reading and checking of the given websites. These functions include: 

- main(): This function runs the site checker
- _get_websites_urls(user_args): This function extracts the urls given by the user and makes sure it is returned in a readable format.
- _read_urls_from_file(file): This function extracts the urls from a file is a file is given instead of a list of urls.
- _asynchronous_check(urls): This function checks the urls asynchronously.
- _synchronous_check(urls): This function checks the urls synchronously.

### checker.py
This file houses the actual 'checker' functions 'site_is_online' and 'site_is_online_async'. Both of these functions take in a url and attempts to establish a 
connection to the given url. If a connection is established, they return True, meaning the website at the given url is online. Otherwise, 
it will return False and establish that the website is not online.

### cli.py
Finally, this file is what makes the module able to function on the command line. It houses the functions 'read_user_cli_args' and 'display_check_result'.
The function 'read_user_cli_args' uses an argument parser to set up the flags and arguments that can be used with this function. The function 'display_check_result'
displays the result of whether a website is online or offline.

## How to use the website checker
First, using the command line, go to the directory that houses the folder 'site_checker'. From there, you can use the function 'python -m site_checker' in 
conjunction with the -u, -f, and -a flags. Use the -u flag like so to check urls entered after the flag: 

 - 'python -m site_checker -u python.org google.com pypi.org'

Or, you can use the -f flag to input a text file instead, allowing the program to check all urls stored inside the text file:

-  'python -m site_checker -f input_file.txt'

Lastly, put the -a flag AFTER entering the url(s)/file name to have the program check the websites asynchronously:

-  'python -m site_checker -u python.org -a' or 'python -m site_checker -f text.txt -a'

You can also use the command 'python -m site_checker -h' to get some help deciphering the flags.
