import re
def is_palindrome():
    """Check if a given string is a palindrome, ignoring spaces and special characters."""
    input_string = input("Enter a string: ")
    print(f"Original string: {input_string}")

    cleaned_string = re.sub(r'[^A-Za-z0-9]',"",input_string).lower()
    
    reversed_string = cleaned_string[::-1] 

    print(f"Processed string (ignoring spaces & special characters): {cleaned_string}")   
    print(f"Reversed string : {reversed_string}")

    if reversed_string == cleaned_string:
        print("✅The string is a palindrome")
    else:
        print("❌The string is NOT a palindrome")

if __name__ == "__main__":
    is_palindrome()