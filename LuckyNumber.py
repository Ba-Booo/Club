import random

print("| 나머지게임\n\n규칙\n\t1. 주사위를 3번 굴려 나온 수를 원하는대로 나열\n\t2. 나열한 수를 연속으로 2번 작성\n\t\t예)369면 369369\n\t3. 작성한 수를 7로 나누었을때 나머지를 기준으로 상금을 지급")
print("\n\n0\t: -30000\n1\t: 10000\n2\t: 20000\n3\t: 30000\n4\t: 40000\n5\t: 50000\n6\t: 60000\n")
myMoney = int( input("당신의 재산 : ") )

print()

while myMoney >= 0:

    for i in range(3):
        print( random.randint(1,6) )

    result = input("\n수 나열 : ")
    
    result += result

    remain = int(result) % 7

    print(result, "/ 7 =", int(result) / 7, "...", remain)

    print("\n나머지 :", remain)

    if remain == 0:
        myMoney -= 30000
    elif remain == 1:
        myMoney += 10000
    elif remain == 2:
        myMoney += 20000
    elif remain == 3:
        myMoney += 30000
    elif remain == 4:
        myMoney += 40000
    elif remain == 5:
        myMoney += 50000
    elif remain == 6:
        myMoney += 60000

    print("남은 자산 :", myMoney)

    print()

    if myMoney <= 0:
        print("파산파산파산파산파산파산파산파산파산파산파산파산파산파산파산파산파산")
        break

    aw = input("다시하시겠습니까? (y or n) ")

    if aw == "n":
        print
        break

# 어마어마한수학