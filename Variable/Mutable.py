'''
참고한 곳 :https://wikidocs.net/91520
파이썬의 객체는 수정이 가능한 Mutable 객체, 수정이 불가능한 Immutable 객체가 있다.
Mutable 객체: 수정이 가능한 타입의 객체
>> list, dictionary, set객체가 대표적인 Mutable 객체이다.

리스트 객체는 리스트의 각 인덱스가 리스트의 각각의 인덱스값의 요소들을 바인딩하는 구조를 띕니다.
일차원 리스트의 경우 리스트안에는 Immutable 객체가 담기게 됩니다.
또한 Immutable 객체는 값을 변경할 경우 새로운 객체를 참조하게 됩니다.
따라서 리스트의 요소를 변환할 경우 리스트 객체의 주소(객체를 참조하는 변수의 값)은 변하지 않고
변환된 인덱스의 주소만 변하게 됩니다.
'''

a = [1, 2, 3]

def get_Address(a: list):
    print(f"Address of a : {id(a)}")
    for i in range(len(a)):
        print(f"Address of a[{i}] : {id(a[i])}, value of a[{i}] : {a[i]}")
    print("a라는 변수가 리스트 객체를 바인딩 하고 있고 리스트의 각 인덱스가 리스트의 각 인덱스 요소 객체들을 바인딩하고 있습니다.")
    a[0] = 7
    print(f"Address of a : {id(a)}")
    for i in range(len(a)):
        print(f"Address of a[{i}] : {id(a[i])}, value of a[{i}] : {a[i]}")
    print("a라는 변수가 리스트 객체를 바인딩 하고 있고 리스트의 각 인덱스가 리스트의 각 인덱스 요소 객체들을 바인딩하고 있습니다.")

get_Address(a)

