import re

def remove_dupilicate(str_input: list) -> list:
    """Removes duplicate strings from a list and returns a sorted list of unique strings."""
    return sorted(set(str_input))

def main():
    """Gets user input, removes non-alphanumeric characters, splits into words, removes duplicates, and prints the results."""   
    input_str = input("Enter the list of words (seperated by spaces): ")
    
    # Remove non-alphanumerical characters and extra spaces
    cleaned_input = re.sub(r'[^a-zA-Z0-9 ]', "",input_str)

    duplicate_list = cleaned_input.split()
    
    print(f"Given list: {duplicate_list}")
    
    unique_list = remove_dupilicate(duplicate_list)
    
    print(f"New list: {unique_list}")

if __name__ == "__main__":
    main()