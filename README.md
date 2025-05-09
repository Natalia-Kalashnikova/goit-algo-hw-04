# Python Mini Tasks

This repository contains small but practical Python tasks designed to improve your skills in file parsing, data manipulation, and real-world problem solving. Each task includes a clearly defined function and its use case in a business or practical scenario.

---

## Task 01 – Total and Average Salary Calculator

**Function:** `total_salary(path)`

You have a text file that contains the monthly salaries of developers in your company. Each line in the file contains the developer's last name and salary, separated by a comma without spaces.  
The task is to create a function that reads this file, parses the data, and returns the **total** and **average salaries** of all developers.  
This can be helpful for generating salary reports or payroll calculations.

---

## Task 02 – Cat Information Parser

**Function:** `get_cats_info(path)`

You have a text file that contains information about cats. Each line in the file contains a unique cat ID, its name, and its age, separated by commas.  
Your task is to develop a function that reads this file and returns a **list of dictionaries** with information about each cat.  
This can be useful for managing pet databases, adoption systems, or animal shelters.

---

## Task 03 – Directory Structure Visualizer

**Function:** `print_directory_tree(path: Path, prefix: str = "")`

Developed a function that takes a directory path as an argument and prints its structure, including all subdirectories and files, with colored names for better visual differentiation. The implementation ensures smooth traversal, even when some directories are inaccessible due to permission restrictions.

---

## Task 04 – CLI Contact Assistant Bot

**Function:** `main(), parse_input(), add_contact(), change_contact(), show_phone(), show_all_contacts()`

Developed a command-line interface (CLI) assistant bot that processes text commands entered via keyboard and responds accordingly. The assistant stores contact names and phone numbers, allows updating and retrieving contacts, and displays all saved entries. A Python dictionary is used to manage the contacts, with names as keys and phone numbers as values. The bot continuously processes user input until the **"exit"** or **"close"** command is received. Input is case-insensitive, and the program handles incorrect commands with appropriate messages.

---
