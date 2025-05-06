n = input()


ls = list( reversed( range( int(n) ) ) ) + list( range( 1, int(n) ) )


for i in ls:  

    for y in range(i):      #띄어쓰기

        print(" ",end="")

    for x in range( (int(n) - i) * 2 - 1 ):    #글자 출력

        print("*",end="")


    print()


# list(); 값을 리스트로 변환
# reversed : 리스트를 뒤집음
