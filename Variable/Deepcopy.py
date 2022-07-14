'''
deepcopy는 Mutable 객체 내부의 모든 Mutable 객체들에 대하여 원본과 값은 같지만 다른 주소값의 객체를 생성하여 복사합니다.

내가 아는 구현법
1. 사용자가 직접 구현
2. deepcopy 표준 라이브러리의 deepcopy() 메소드 활용
'''

# 1. 이차원 리스트 한정 deepcopy 직접 구현
def UserDefineDeepcopy():
    a = [
        [1, 2, 3],
        [4, 5, 6]
    ]

    b = []

    for i in a:
        b.append(i[:])

    print(f"value of a: {a}")
    print(f"value of b: {b}")
    print(f"Address of a[0]: {id(a[0])}, Address of b[0]: {id(b[0])}")
    print()
    # 리스트 컴프리헨션을 통해 더 간단히 구현할 수 있다.
    c = [x[:] for x in a]
    print(f"value of a: {a}")
    print(f"value of c: {c}")

    print(f"Address of a[0]: {id(a[0])}, Address of c[0]: {id(c[0])}")

    # 복사본 데이터를 변경하여도 원본 데이터에 영향을 미치지 않는다.

    c[0][0] = 7
    print("------------After Change--------------")
    print(f"value of a: {a}")
    print(f"value of c: {c}")





# UserDefineDeepcopy()

# 2. deepcopy() 메소드 구현
from copy import deepcopy

def UseDeepcopy():
    # 파이썬의 기본 라이브러리 중 deepcopy() 메소드는
    # Mutable 객체 내부의 모든 Mutable 객체들에 대하여 원본과 값은 같지만 다른 주소값의 객체를 생성하여 복사해준다.
    a = [
        [1, 2, 3],
        [4, 5, 6]
    ]

    b = deepcopy(a)

    print(id(a[0]) == id(b[0]))
    # Immutable 객체는 변경 불가한 객체이므로 값이 같다면 같은 객체를 바인딩하고 있다.
    print(id(a[0][0]) == id(b[0][0]))

UseDeepcopy()