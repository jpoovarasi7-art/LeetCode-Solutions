with open("Paragraph.txt", "w") as f:
    string = input("Enter the paragraph as Input: ")
    f.write(string)
with open("Paragraph.txt", "r") as f:
    para = f.read()
array = []
word = ""
for char in para:
    if char == " " or char == "\n" or char == "\t":
        if word != "":
            array.append(word)
            word = ""
    else:
        word += char
if word != "":
    array.append(word)
repeat = {}
for i in array:
    clean_word = ""
    for j in i:
        if 'A' <= j <= 'Z':
            clean_word += chr(ord(j) + 32)
        else:
            clean_word += j
    if clean_word in repeat:
        repeat[clean_word] += 1
    else:
        repeat[clean_word] = 1
while True:
    print("\n" + "*"*30, "MENU DRIVEN", "*"*30)
    print("1. Find the number of words repeated in the paragraph")
    print("2. Find the number of letters in the word")
    print("3. Find the reverse for the largest word in the paragraph")
    print("4. Exit")
    try:
        ch = int(input("Enter the choice: "))
    except ValueError:
       print("Invalid input! Please enter a number:")
       continue
    if ch == 1:
        print("\nRepeated words and their counts:")
        for key in repeat:
            if repeat[key] > 1:
                print(key, ":", repeat[key])
    elif ch == 2:
        words_of={}
        print("\nLength of words:")
        char_count=1
        for key in array:
           if key not in words_of:
                words_of[key] = char_count
           else:
                char_count += 1
        for key,values in words_of.items():
           print(key,":",values)
    elif ch == 3:
        largest_word = ""
        max_len = 0
        for w in array:
            current_len = 0
            for char in w:
                current_len += 1
            if current_len > max_len:
                max_len = current_len
                largest_word = w
        reversed_str = ""
        for i in range(max_len - 1, -1, -1):
            reversed_str += largest_word[i]
        print("Largest Word:", largest_word)
        print("Reversed:", reversed_str)
    elif ch == 4:
        break
    else:
        print("Invalid choice, please try again.")
