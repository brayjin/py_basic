# Python Basics Repository

Welcome to the **Python Basics** repository! 🚀 This repository contains Python programs covering fundamental concepts such as lists, tuples, dictionaries, and more. It is designed for beginners who want to practice Python and improve their problem-solving skills.

Is Updated daily

## 📌 Table of Contents

- [Introduction](#introduction)
- [Getting Started](#getting-started)
- [Programs List](#programs-list)
- [Explanation](#explanation)
- [Contributing](#contributing)
- [License](#license)

## 📖 Introduction

This repository aims to provide a solid foundation in Python programming by offering simple yet effective programs. Each script focuses on a specific fundamental concept and encourages logical thinking and structured problem-solving.

## ⚡ Getting Started

To use this repository, follow these steps:

1. Ensure you have Python 3 installed on your system.
2. Clone the repository:
   ```bash
   git clone https://github.com/brayjin/py_basic.git
   ```
3. Navigate to the directory:
   ```bash
   cd py_basic
   ```
4. Run any Python program:
   ```bash
   python3 program_name.py
   ```

## 📝 Programs List

| #  | Program Name             | Description                               |
| -- | ------------------------ | ----------------------------------------- |
| 1  | `palindrome.py`          | Check if a given string is a palindrome   |
| 2  | `unique.py`              | Remove duplicate words from a list        |
| 3  | `large.py`               | Find the largest number in a list         |
| 4  | `sum_of_list.py`         | Compute the sum of all elements in a list |
| 5  | `tuple_operations.py`    | Perform basic tuple operations            |
| 6  | `dictionary_basics.py`   | Demonstrate dictionary operations         |
| 7  | `string_manipulation.py` | Various string manipulation techniques    |
| 8  | `factorial.py`           | Calculate the factorial of a number       |
| 9  | `fibonacci.py`           | Generate Fibonacci series up to n terms   |
| 10 | `file.py`                | Display contents from a text file         |

## 📚 Explanation

### `palindrome.py`
In this program, the `re` package is imported to handle regular expressions. The `is_palindrome` function is a user-defined function that checks whether a given string is a palindrome while ignoring spaces and special characters.

#### **How the program works:**
1. The program prompts the user to enter a string.
2. It prints the original input string.
3. Using `re.sub(r'[^A-Za-z0-9]', "", input_string).lower()`, the program removes all non-alphanumeric characters and converts the string to lowercase for uniform comparison.
4. The cleaned string is reversed using `[::-1]`.
5. Both the cleaned and reversed strings are printed.
6. An `if-else` statement checks whether the cleaned string and its reversed version are the same. If they match, it prints that the string is a palindrome; otherwise, it states that it is not.
7. The condition `if __name__ == "__main__": is_palindrome()` ensures that the function runs only when the script is executed directly, not when imported as a module.

This approach ensures that punctuation, spaces, and case differences do not affect the palindrome check.

### `large.py`
The `find_large` function is responsible for finding the maximum integer in a given list using Python's built-in `max()` function.

In the `main` function:

- The program continuously prompts the user to enter a list of integers separated by spaces.
- If the user does not enter any input, it asks them to provide at least one integer.
- The input string is split into a list, and each element is converted to an integer using list comprehension.
- If a non-integer value is entered, the program handles the `ValueError` exception and prompts the user to enter valid integers.
- Finally, the largest number in the list is displayed.

The `if __name__ == "__main__":` block ensures that the script runs only when executed directly, not when imported as a module.

### `unique.py`
The `remove_duplicate` function removes duplicate words from a given list by converting it into a set (which stores only unique values) and then sorting it in ascending order.

#### **How the program works:**
- The user is prompted to enter a list of words separated by spaces.
- Non-alphanumeric characters are removed using the `re.sub()` function, ensuring that only letters, numbers, and spaces remain.
- The cleaned input is split into a list of words.
- The program prints the original list before and after removing duplicates.
- The unique words are sorted alphabetically and displayed.

The `if __name__ == "__main__":` block ensures that the script runs only when executed directly, not when imported as a module.

## 🤝 Contributing

Contributions are welcome! If you’d like to add new Python programs or improve existing ones, follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b new-feature`.
3. Make your changes and commit them: `git commit -m 'Add new feature'`.
4. Push the branch: `git push origin new-feature`.
5. Open a Pull Request for review.

## 📜 License

This repository is open-source and available under the [MIT License](LICENSE). Feel free to use and modify the code as needed.