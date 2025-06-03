filename = 'output.txt'
try:
    f1 = open(filename, 'w')
    x = input("Enter text to write to the file: ")
    f1.write(x + '\n')
    print(f"Data successfully written to '{filename}'")
    f1.close()
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")

try:
    f1 = open(filename , 'a')
    y = input("\nEnter additional text to append: ")
    f1.write(y + '\n')
    print(f"Data successfully appended to '{filename}'\n")
    f1.close()
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
try:
    f1 = open(filename, 'r')
    # print(f"Reading content of {filename}:")
    read_lines = f1.readlines()
    # print(read_lines)
    print(f"Final content of {filename}:")
    for line in read_lines:
        print(line.strip())
    f1.close()
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
    
