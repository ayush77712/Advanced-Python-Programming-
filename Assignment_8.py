file1 = open("Hello1.txt", "r")

lines = file1.readlines()
print("Number of lines:", len(lines))
print("First two lines:")
print(lines[0], end="")
print(lines[1], end="")
file1.close()

file2 = open("Hello2.txt", "w")
file2.writelines(lines[:2])
file2.close()

print("\nData written into new file.")
