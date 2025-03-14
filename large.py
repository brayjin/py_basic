def find_large(int_list: list) -> int:
    """Finds the largest integer in a list."""
    return max(int_list)

def main():
    while True:
        in_int = input("Enter some integers (separated by spaces): ")
        if not in_int:
            print("Please enter at least one integer.")
            continue
        try:
            int_list = [int(i) for i in in_int.split()]
            print(f"Input List: {int_list}")
            max_value = find_large(int_list)
            print(f"Largest Number: {max_value}")
            break
        except ValueError:
            print("Invalid input. Please enter integers only.")

if __name__ == "__main__":
    main()