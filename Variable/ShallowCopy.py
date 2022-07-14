'''
참고한 곳:https://wikidocs.net/16038
리스트 얕은 복사 구현 방법
1. 대입 연산자 활용(=)
2. 슬라이싱 활용([:])
3. 파이썬 라이브러리 중 copy.copy() 메소드 활용 >> 간단히 구현만
4. 얕은 복사의 단점 >> Mutable In Mutable
'''
from copy import copy

# 1. 대입 연산자 활용
def equal_operator():
    # 대입 연산자를 통한 복사는 원본 변수가 저장하고 있는 값을 그대로 복사한다.
    # 원본 변수는 객체의 주솟값을 저장하므로 그 주솟값을 그대로 복사하게 된다.
    a = [1, 2, 3]
    # [1, 2, 3] 리스트 객체를 a라는 변수가 바인딩하고 있고 리스트의 각 정수형 Immutable 객체를 인덱스가 다시 바인딩하고 있음
    b = a
    # b 변수도 [1, 2, 3] 리스트 객체를 동시에 바인딩 하고 있음
    # 리스트 객체 [1, 2, 3]의 reference count 는 1 증가.
    print(f"address of a: {id(a)}, address of b: {id(b)}")

    for i in range(len(a)):
        print(f"address of a[{i}] : {id(a[i])}, value of a[{i}] : {a[i]}")
    for i in range(len(b)):
        print(f"address of b[{i}] : {id(b[i])}, value of b[{i}] : {b[i]}")

    # a와 b 변수는 같은 객체를 바인딩하고 있기 때문에 복사본 b의 요소 변환이 a에게 영향을 미친다.
    print("------------------after Translation----------------")
    a[0] = 7

    for i in range(len(a)):
        print(f"address of a[{i}] : {id(a[i])}, value of a[{i}] : {a[i]}")
    for i in range(len(b)):
        print(f"address of b[{i}] : {id(b[i])}, value of b[{i}] : {b[i]}")


# equal_operator()

# 2. 슬라이싱 활용
def slicing():
    a = [1, 2, 3]
    # [1, 2, 3] 리스트 객체를 a라는 변수가 바인딩하고 있고 리스트의 각 정수형 Immutable 객체를 인덱스가 다시 바인딩하고 있음
    b = a[:]
    # 슬라이싱을 통해 a가 바인딩하고 있는 객체와 값이 똑같은 객체를 생성후 b 변수가 그 객체를 바인딩.
    # 변수 a와 변수 b가 저장하고 있는 주소값이 다른 것을 확인할 수 있다.
    print(f"address of a: {id(a)}, address of b: {id(b)}")

    for i in range(len(a)):
        print(f"address of a[{i}] : {id(a[i])}, value of a[{i}] : {a[i]}")
    for i in range(len(b)):
        print(f"address of b[{i}] : {id(b[i])}, value of b[{i}] : {b[i]}")

    # a와 b 변수는 다른 객체를 바인딩하고 있기 때문에 복사본 b의 요소 변환이 a에게 영향을 미치지 않는다.
    print("------------------after Translation----------------")
    a[0] = 7

    for i in range(len(a)):
        print(f"address of a[{i}] : {id(a[i])}, value of a[{i}] : {a[i]}")
    for i in range(len(b)):
        print(f"address of b[{i}] : {id(b[i])}, value of b[{i}] : {b[i]}")

# 3. copy() 메소드 활용

def UseCopy():
    a = [1, 2, 3]
    b = copy(a)
    print(id(a) == id(b))
# UseCopy()

# 4. 얕은 복사의 단점 >> Mutable객체 안에 Mutable 객체를 담고 있는 경우
def MutableInMutable():
    a = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    '''
    이차원 리스트의 메모리 할당 상황
    1. a라는 변수가 2개의 mutable객체를 담고 있는 리스트 객체를 바인딩하고 있다.
    2. a[0] 가 3개의 Immutable객체(정수)를 담고 있는 리스트 객체를 바인딩하고 있다.
       a[1] 이 3개의 Immutable객체(정수)를 담고 있는 리스트 객체를 바인딩하고 있다.
    3. a[0][0], a[0][1], a[0][2] 가 각각의 Immutable 객체 1, 2, 3 을 바인딩하고 있다.
       a[1][0], a[1][1], a[1][2] 가 각각의 Immutable 객체 4, 5, 6 을 바인딩하고 있다.
    
    '''
    # Slicing을 통한 Shallow Copy는 리스트 객체의 요소들을 그대로 복사한다.

    b = a[:]
    # 1. 변수 a가 바인딩하고 있는 리스트 객체의 요소를 그대로 복사하여 또 다른 객체를 만든다.
    # 2. 새로 만든 객체를 변수 b가 바인딩한다.
    # 이차원 리스트 객체의 각 요소는 Mutable 객체의 주소값을 저장하고 있었다.
    # 따라서 복사해 만든 새로운 객체의 요소값들도 동일한 주소값들을 저장한다.
    # 따라서 복사해 만든 리스트의 요소값 b[0] 와 원본 리스트의 요소값 a[0]는 동일한 주소값을 저장하고 있다. >> 동일한 객체를 바인딩하고 있다.
    # a[0]와 b[0]가 동시에 바인딩하고 있는 객체는 Immutale 객체를 요소로 갖고 있는 Mutable 리스트 객체이다.
    # 즉 변수 a 와 변수 b는 다른 객체를 바인딩 하고 있지만
    # a[0]와 b[0] 는 같은 객체를 바인딩하고 있다!
    # a[1]과 b[1] 도 같은 객체를 바인딩하고 있다!

    print(f"Address of a : {id(a)}, Address of b : {id(b)}")
    print(f"Address of a[0] : {id(a[0])}, Address of b[0] : {id(b[0])}")
    print(f"Address of a[1] : {id(a[1])}, Address of b[1] : {id(b[1])}")

    # 이제 복사본의 데이터를 변경해보자.
    b[0][0] = 7
    # b[0](Mutable 객체)의 요소 1(Immutable 객체)를 변경하였다.
    # b[0]와 a[0] 변수는 동일한 객체를 바인딩하고 있기 때문에 a[0][0] 값도 변경되게 된다.
    print("--------------After translation--------------------")
    print(f"value of a: {a}")
    print(f"value of b: {b}")

MutableInMutable()









