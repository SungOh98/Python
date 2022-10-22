'''
파이썬의 함수에서 매개변수 전달 방식

컴퓨터 언어에서 함수의 매개변수를 통해 변수의 값을 전달하는 방식은 크게 두가지로 나누어 진다.
1. call - by - value
> 함수 호출 시 인수의 '값'을 매개변수에 전달하는 방식
> 매개변수는 전달 받은 값을 복사한다.
> 함수 내부에서 매개변수를 변경하더라도 원본 데이터에 영향을 미치지 않는다.

2. call - by - reference
> 객체의 메모리 주소를 인수로 매개변수에 전달하는 방식
> 함수 내부에서 매개변수의 값을 변경하면 원본 데이터에 영향을 미친다.

c나 c++ 에서는 함수 선언시 매개변수로 변수의 주소를 받을 것인지, 값을 받을 것인지 개발자가 직접 정해야한다
python의 매개변수 전달 방식은 java와 마찬가지로 모두 Call By Value이다.
Java와 다른 점은 원시타입도 모두 객체임.
'''

def funcInt(x:int):
    print(f"Address of x(parameter): {id(x)}, value of x(parameter): {x}")
    # 정수는 Immutable 객체이므로 변수의 값을 변경할 시 새로운 객체를 생성한 후 새로운 바인딩을 함 >> 주솟값 변경됨.
    x = 100
    print(f"Address of x(parameter): {id(x)}, value of x(parameter): {x}")

x = 10
print(f"Address of x: {id(x)}, value of x: {x}")
funcInt(x)
print(f"Address of x: {id(x)}, value of x: {x}")
print("정수 객체는 Immutable 객체이므로 값이 변경되면 객체 자체가 바뀌기 때문에 주소값도 변경된다. 위 예제에서는 함수 호출 이후 주솟값이 변경되지 않았으므로 원본 객체에 영향을 미치지 않았다는 것을 확인할 수 있다.\n")


def funcStr(x:str):
    print(f"Address of x(parameter): {id(x)}, value of x(parameter): {x}")
    # 문자열은 Immutable 객체이므로 변수의 값을 변경할 시 새로운 객체를 생성한 후 새로운 바인딩을 함 >> 주솟값 변경됨.
    x = "흥부"
    print(f"Address of x(parameter): {id(x)}, value of x(parameter): {x}")

x = "홍길동"
print(f"Address of x: {id(x)}, value of x: {x}")
funcStr(x)
print(f"Address of x: {id(x)}, value of x: {x}")
print("문자열 객체는 Immutable 객체이므로 값이 변경되면 객체 자체가 바뀌기 때문에 주소값도 변경된다. 위 예제에서는 함수 호출 이후 주솟값이 변경되지 않았으므로 원본 객체에 영향을 미치지 않았다는 것을 확인할 수 있다.\n")

def funcTuple(x:tuple):
    print(f"Address of x(parameter): {id(x)}, value of x(parameter): {x}")
    # 튜플은 Immutable 객체이므로 변수의 값을 변경할 시 새로운 객체를 생성한 후 새로운 바인딩을 함 >> 주솟값 변경됨.
    x = (3, 4)
    print(f"Address of x(parameter): {id(x)}, value of x(parameter): {x}")

x = (1, 2)
print(f"Address of x: {id(x)}, value of x: {x}")
funcTuple(x)
print(f"Address of x: {id(x)}, value of x: {x}")
print("튜플 객체는 Immutable 객체이므로 값이 변경되면 객체 자체가 바뀌기 때문에 주소값도 변경된다. 위 예제에서는 함수 호출 이후 주솟값이 변경되지 않았으므로 원본 객체에 영향을 미치지 않았다는 것을 확인할 수 있다.\n")

def funcFloat(x:float):
    print(f"Address of x(parameter): {id(x)}, value of x(parameter): {x}")
    # 실수은 Immutable 객체이므로 변수의 값을 변경할 시 새로운 객체를 생성한 후 새로운 바인딩을 함 >> 주솟값 변경됨.
    x = 4.5
    print(f"Address of x(parameter): {id(x)}, value of x(parameter): {x}")

x = 3.7
print(f"Address of x: {id(x)}, value of x: {x}")
funcFloat(x)
print(f"Address of x: {id(x)}, value of x: {x}")
print("실수 객체는 Immutable 객체이므로 값이 변경되면 객체 자체가 바뀌기 때문에 주소값도 변경된다. 위 예제에서는 함수 호출 이후 주솟값이 변경되지 않았으므로 원본 객체에 영향을 미치지 않았다는 것을 확인할 수 있다.\n")

def funcList(x:list):
    print("함수 호출 후 매개변수로 전달된 리스트 객체의 정보")
    print(f"Address of x : {id(x)}, value of x: {x}\n")
    print("함수 호출 후 전역 변수 리스트 객체의 정보")
    print(f"Address of a : {id(a)}, value of a: {a}\n")
    # 일차원 리스트 객체이므로 Immutable 객체를 포함하고 있는 Mutable 객체이다.
    # 요소 변환
    x[0] = 7
    print("요소 변환 후 매개변수로 전달된 리스트 객체의 정보")
    print(f"Address of x : {id(x)}, value of x: {x}\n")
    print("요소 변환 후 전역 변수 리스트 객체의 정보")
    print(f"Address of a : {id(a)}, value of a: {a}\n")


a = [1, 2, 3]
print(f"함수 호출 전 리스트 객체의 정보")
print(f"Address of a : {id(a)}, value of a: {a}\n")
funcList(a)
# funcList(a[:])
print(f"함수 실행 후 리스트 객체의 정보")
print(f"Address of a : {id(a)}, value of a: {a}\n")
print("일차원 리스트 객체는 Immutable 객체를 포함하고 있는 Mutable 객체이므로 리스트의 요소 (Immutable) 을 변환 하더라도 리스트 객체 자체가 바뀌지 않으므로 리스트를 바인딩 하고 있는 변수의 값(주소값)에 변동이 없다.")
print("함수에 주솟값을 인수로 넘겨주었으므로 함수 내부에서 객체의 데이터를 바꿀 경우 당연히 원본 객체에도 영향을 미친다.")

print("매개변수로 Immutable 객체를 넘겨주었을 때 call by value 처럼 보이고 Mutable 객체를 넘겨주었을 때 call by reference 처럼 보이는 이유는 단지 파이썬의 데이터 타입 특징과 함수 내부에서 동작 과정의 차이에 있었다.")
print("아래의 예제처럼 함수 내부에서 리스트 객체 자체를 바꾼다면 원본 객체에 영향을 주지 않으므로 call by value 처럼 보인다.")


def funcList2(x:list):
    print("함수 호출 후 매개변수로 전달된 리스트 객체의 정보")
    print(f"Address of x : {id(x)}, value of x: {x}\n")
    print("함수 호출 후 전역 변수 리스트 객체의 정보")
    print(f"Address of a : {id(a)}, value of a: {a}\n")
    # 일차원 리스트 객체이므로 Immutable 객체를 포함하고 있는 Mutable 객체이다.
    # 객체 바꾸기.
    x = [4, 5, 6]
    print("객체 변경 후 매개변수로 전달된 리스트 객체의 정보")
    print(f"Address of x : {id(x)}, value of x: {x}\n")
    print("객체 변경 후 전역 변수 리스트 객체의 정보")
    print(f"Address of a : {id(a)}, value of a: {a}\n")

a = [1, 2, 3]
print(f"\n\n함수 호출 전 리스트 객체의 정보")
print(f"Address of a : {id(a)}, value of a: {a}\n")
funcList2(a)
print(f"함수 실행 후 리스트 객체의 정보")
print(f"Address of a : {id(a)}, value of a: {a}\n")

