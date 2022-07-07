import random


def show_word(): # 단어 보여주기
    print(answer_list)


def get_answer_input(): # 사용자 입력
    choice = int(input("1: 알파벳 입력\n2: 단어 입력\n번호를 입력해 주세요 : "))
    if choice == 1: # 알파벳 입력
        alpha = input("알파벳을 입력해 주세요: ")
        for i in range(len(random_word)): # 똑같은 알파벳 찾기
            if random_word[i] == alpha:
                answer_list[i] = alpha
    else:
        word = input("단어를 입력해 주세요 : ")
        if word == random_word:  # 입력한 단어와 생성된 단어가 같을 떄 -> 게임 종료
            print(f"단어를 맞추셨습니다\n남은 목숨 : {life}")
            exit(0)


new_word = open('new_word.txt', 'r')
random_word = random.choice(new_word.readlines()).splitlines()[0]
# print(len(random_word))
life = 6
print(random_word)
answer_list = []  # 정답칸 리스트
for i in range(len(random_word)):  # 게임 시작 : 생성된 단어 길이, 빈칸 보여주기
    answer_list.append('_')

while True:  # 게임 진행 반복문
    get_answer_input()  # 사용자 입력
    show_word()  # 현재 단어 길이 보여주기
