dict1 = {"Alice": 85, "Bob": 90, "Charlie": 95}
x = input("Enter the student's name: ")
if x in dict1:
    print(f"{x}'s marks: {dict1[x]}") 
else:
    print("Student not found.")