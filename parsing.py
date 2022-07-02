word = open('C:/Users/ASUS/Desktop/word.txt', 'r', encoding="ANSI")
new_word = open('new_word.txt', 'w', encoding="ANSI")
while True:
    flag = False
    line = word.readline()
    for i in range(len(line)):
        if 'a' <= line[i] <= "z" or 'A' <= line[i] <= 'Z':
            print(line[i], file=new_word, end='')
            flag = True
    if flag:
        print(file=new_word)
    if line == '':
        break
word.close()
new_word.close()
