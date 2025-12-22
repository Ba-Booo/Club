import matplotlib.pyplot as plt





# 함수 입력
n = int( input("다항함수 차수 입력 ") )
function = []

# 함수 추출
for i in range( n + 1 ):

    function.append( str( input() ) )   # 기호
    function.append( int( input() ) )   # 계수
    input()                             # x
    function.append( int( input() ) )   # 차수

# 함수 확인용
print( function )

#범위지정
functionRange = list( map( int, input().split() ) )

#함수 그리기
x = []
y = []

for i in range( functionRange[0], functionRange[1] + 1):

    # x값
    x.append(i)

    # y값
    value = 0
    
    for j in range( 0, len( function ), 3 ):

        if function[ j ] == "+":
            value += function[ j + 1 ] * ( i ** function[ j + 2 ] )
        else:
            value -= function[ j + 1 ] * ( i ** function[ j + 2 ] )

    y.append(value)





#경사하강법

#도함수 추출
derivative = []
for i in range( 0, len( function ) - 3, 3 ):

    derivative.append( function[ i ] )
    derivative.append( function[ i + 1 ] * function[ i + 2 ] )
    derivative.append( function[ i + 2 ] - 1 )

#경사하강법
positionX = functionRange[0] + 1
for i in range(1000):
    
    GDValue = 0
    for j in range( 0, len( derivative ), 3 ):

        if derivative[ j ] == "+":
            GDValue += derivative[ j + 1 ] * ( positionX ** derivative[ j + 2 ] )
        else:
            GDValue -= derivative[ j + 1 ] * ( positionX ** derivative[ j + 2 ] )


    positionX -= GDValue * 0.01
 


positionY = 0
    
for i in range( 0, len( function ), 3 ):

    if function[ i ] == "+":
        positionY += function[ i + 1 ] * ( positionX ** function[ i + 2 ] )
    else:
        positionY -= function[ i + 1 ] * ( positionX ** function[ i + 2 ] )



plt.figure()
plt.plot(x, y)
plt.scatter(positionX, positionY, color = "red")
plt.show()