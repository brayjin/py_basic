import re

def rm_dupi(str_input: list) -> list:
    return sorted(set(str_input))

def main():
    in_str = input("Enter the list of words: ")
    in_str = re.sub(r'[^a-zA-Z0-9 ]', "",in_str)
    dp_list = in_str.split()
    print(f"Given list: {dp_list}")
    uniq = rm_dupi(dp_list)
    print(f"New list: {uniq}")

main()