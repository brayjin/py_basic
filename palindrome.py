import re
def main():
    in_string = input("Enter a string: ")
    print(f"Input string: {in_string}")
    new_string = re.sub(r'[^A-Za-z0-9]',"",in_string).lower()
    rev_string = new_string[::-1]
    print(f"Reversed string (ignored spaces): {rev_string}")
    if rev_string == new_string:
        print("palindrome")
    else:
        print("not a palindrome")

main()