try:
    filename = 'sample1.txt'
    file_1 = open(filename,'r+')
    read_line = file_1.readlines()
    print("Reading file content:")
    count = 1
    for line in read_line:
        print(f"Line {count}: ", end='')
        count += 1
        print(line.strip())
    # print(read_line)
    file_1.close()
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")