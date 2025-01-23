# Searching & Sorting Explorer v1.0.0
#### Format: GUI Application
#### Technologies & Frameworks: Python, tkinter
## How to Use
1. Visit the [Releases]() page of this repository
2. Download and extract the **_main.app.zip_** file
3. Double-click the **_main.app_** file to run the application
## Description
This project was part of my coursework at the University of Nebraska at Omaha, submitted as a final project for my Intro to Computer Science II course. Developed completely in Python with the tkinter framework, this GUI aims to educate users on the following five searching and sorting algorithms: 
1. Linear Search
2. Binary Search
3. Bubble Sort
4. Selection Sort
5. Insertion Sort

To accomplish this, when an algorithm is selected, an interactive process allows a user to:
* View the definition of the algorithm
* View details on the algorithm (runtimes, pros, cons)
* Input a sample array
* View each step (or pass) of the searching or sorting process on the inputted array (tracing table for searches, step-by-step array for sorts)

## Directory Structure
* **_main.py_** - Launches the GUI application
* **_gui.py_** - Contains all of the logic for the GUI to function using a class. Displays information, handles input, stores variables, and calls functions from the modules.py file. 
* **_modules.py_** - Contains five functions, one for each algorithm, that appends each step of an algorithm's process to a list.
## References & Attribution
* [tkinter Documentation](https://docs.python.org/3/library/tk.html)
##### Additional documentation and commentary are included directly within the code files. 
