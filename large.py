def find_large(int_list: list) -> int:
    
    return max(int_list)
def main():
    in_int = input("Enter some integers: ")
    int_list = [int(i) for i in in_int.split()]
    print(f"Input List: {int_list}")
    max_value = find_large(int_list)
    print(f"Largest Number: {max_value}")
    
main()

