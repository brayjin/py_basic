# Python Basics Repository

Welcome to the **Python Basics** repository! 🚀 This repository contains Python programs covering fundamental concepts such as lists, tuples, dictionaries, and more. It is designed for beginners who want to practice Python and improve their problem-solving skills.

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

## 🤝 Contributing

Contributions are welcome! If you’d like to add new Python programs or improve existing ones, follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b new-feature`.
3. Make your changes and commit them: `git commit -m 'Add new feature'`.
4. Push the branch: `git push origin new-feature`.
5. Open a Pull Request for review.

## 📜 License

This repository is open-source and available under the [MIT License](LICENSE). Feel free to use and modify the code as needed.

