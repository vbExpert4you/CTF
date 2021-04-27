filename = "ascii.txt"

file = open(filename, 'r')
letters = file.readlines()

print(letters)
flag = ""

for letter in letters:
    cleaned_letter = letter.replace('\n', '')
    flag = flag + chr(int(cleaned_letter))
    
print (flag)
