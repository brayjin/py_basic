import os

print("This program is used to read a file and diplay the content inside it");
try:
	f_path = input("Enter your file path: ")
	f_path = os.path.expanduser(f_path)
	with open  (f_path,"r") as file:
		print(file.read())
except FileNotFoundError:
	print("ERROR: File Not Found")
except Exception as e:
	print(f"Error: {e}")
