import random








# 직접하기

# 방 만들기
doors = [ "goat", "goat", "car" ]
random.shuffle( doors )


print( 0, 0 ,0 )

choice = int( input("문 선택 ") )
gootDoor = -1

for i in range(3):
    
    if i != choice - 1 and doors[i] != "car" and gootDoor == -1:

        print( doors[i], end=" " )
        gootDoor = i + 1

    else:

        print( 0, end=" ")

# 문 바꾸기
print()
change = str( input("바꾸시겠습니까? ") )

print(doors)

# 결과
if change == "y" and doors[ 5 - ( choice + gootDoor ) ] == "car":
    print("성공")
elif change == "n" and doors[ choice - 1 ] == "car":
    print("성공")
else:
    print("실패")










# 시뮬(앎)

# 시뮬 변수
execution = int( input("실행 횟수") )
winCount = 0


for c in range( execution ):
    # 방 만들기
    doors = [ "goat", "goat", "car" ]
    random.shuffle( doors )


    print( 0, 0 ,0 )

    choice = random.randint(1, 3)
    gootDoor = -1

    for i in range(3):
    
        if i != choice - 1 and doors[i] != "car" and gootDoor == -1:

            print( doors[i], end=" " )
            gootDoor = i + 1

        else:

            print( 0, end=" ")

    # 문 바꾸기
    print()

    print(doors)

    # 결과
    if doors[ 5 - ( choice + gootDoor ) ] == "car":
        print("성공")
        winCount += 1

    else:
        print("실패")

print("총 실행 횟수 :", execution)
print("성공 횟수 :", winCount)
print("성공 확률 :", winCount / execution)










# 시뮬(모름)

# 시뮬 변수
execution = int( input("실행 횟수") )
copyExecution = execution
winCount = 0

while copyExecution > 0:

    reset = False

    # 방 만들기
    doors = [ "goat", "goat", "car" ]
    random.shuffle( doors )


    print( 0, 0 ,0 )

    choice = random.randint(1, 3)
    print(choice)
    gootDoor = -1

    for i in range(3):
    
        if i != choice - 1 and gootDoor == -1:

            print( doors[i], end=" " )
            gootDoor = i + 1

            if doors[i] != "car":

                reset = True

        else:

            print( 0, end=" ")

    if reset:

        # 문 바꾸기
        print()

        print(doors)

        # 결과
        if doors[ 5 - ( choice + gootDoor ) ] == "car":
            print("성공")
            winCount += 1

        else:
            print("실패")

        copyExecution -= 1
    
    else:

        print("reset")

print("총 실행 횟수 :", execution)
print("성공 횟수 :", winCount)
print("성공 확률 :", winCount / execution)