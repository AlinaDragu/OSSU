# OSSU

PYTHON FOR EVERYBODY

This course has been created by Professor Charles Severance from the University of Michigan.

Learn to Program and Analyze Data with Python. Develop programs to gather, clean, analyze, and visualize data.

Link: https://www.py4e.com/lessons

Note: This course is also offered on Coursera, Edx. Those versions require you to pay to get the full version of the course. 

Instructions
You need to sign in to the course website using your Google account to access the assignments.

Watch all the videos of a lesson and then do its assignments.

If you prefer reading books, you can read the HTML version of the chapter related to the lesson linked on the lesson's page, or you can download the whole book in different formats from this page.

If you face any problems, feel free to ask questions. You can join the OSSU chat for this course here: https://discord.gg/syA242Z.

You only need to complete the course up to the Regular Expressions lesson. The rest of the course is optional.

COURSE MATERIALS

1.Installing Python

2.Why Program?

3.Variables, expressions and statements

4.Conditional Execution

5.Functions

6.Loops and Iterations

7.Strings

8.Files

9.Lists

10.Dictionaries

11.Tuples

12.Regular Expressions

13.Network Programming (Optional)

14.Using Web Services (Optional)

15.Object-Oriented Programming (Optional)

16.Databases (Optional)

17.Data Visualization (Optional)

Fixes
If you're doing the BeautifulSoup4 lesson, there is an issue with Python 3.10+ that will give you an error referencing the Collections library. We have a fix for you. We don't expect you to understand it, just put this in front of your code in the imports block:

import collections
collections.Callable = collections.abc.Callable

from bs4 import BeautifulSoup 

Doing this should fix the compatibility issue and allow your code to run.
