# 한줄씩 읽어서 앞에 2칸 지우기
# but 알파벳이 아니면 지우기
#
f = open('C:/Users/ASUS/Desktop/words.txt', 'r', encoding="ANSI")
word = f.read()
while True:
    bowl_line = []
    del_word = '□ '
    line = f.readline()
    for i in range(len(line)):
        if 'a' <= line[i] <= "z" or 'A' <= line[i] <='Z':
            bowl_line.append(line[i])
    line = bowl_line

print(word)
f.close()
