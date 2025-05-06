x = input()

for i in range( 1, int(x) + 1 ):

    for r in range(i):

        print("*", end="")

    print()

# range : 특정 구간의 숫자의 범위를 만들어줌, range(a,b) 이런식으로 ( a부터 b-1 까지, a만 있으면 0부터 a까지)
# end="" : print() 함수가 출력된 후 추가할 문자를 지정, 기본값은 \n(줄바꿈)
