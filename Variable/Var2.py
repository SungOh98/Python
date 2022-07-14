'''

참고한 곳: https://ahracho.github.io/posts/python/2017-05-01-everything-in-python-is-object-integer/
정수, 실수, 문자열등의 클래스는 어떻게 생겼을까?
파이썬의 변수는 특정 값을 가지는 객체의 참조이다. 그렇다면 그 객체는 어떤 정보를 가지고 있을까?
1. value : 5라는 값 2.0이라는 실수 값 "홍길동" 이라는 문자열 값등 객체가 나타내는 값을 지니고 있다.
2. object type: 파이썬은 변수를 선언할 시 데이터 타입을 명시하지 않는다. 또한 피연산자의 데이터 타입에 따라 연산 결과가 달라진다 (3 + 4 = 7 Vs '3' + '4' = '34')
따라서 파이썬의 객체는 데이터 타입을 알려주는 정보가 필요하다.
3. reference count: 몇개의 변수가 나(객체)를 참조하고 있는지에 대한 정보가 필요하다. 아무도 나를 참조하지 않는다면 굳이 메모리를 차지하면서 있을 필요가 없기 때문이다.
>> 파이썬에서는 같은 값을 나태내는 변수가 생성되면 새로운 값을 가진 객체를 또 만들어 내는 것이 아니라 singleton으로 이미 있는 객체를 리턴하고
reference count 를 하나 증가 시킨다

'''
import sys
a = 1_000_000_000
print(f"reference count of a: {sys.getrefcount(a)}")
print(f'Address of variable a: {id(a)}')
b = a
print(f"reference count of a: {sys.getrefcount(a)}")
print(f'Address of variable b: {id(a)}')

c = [1, 2, 3, "4"]
print(f"reference count of a: {sys.getrefcount(c)}")
print(f'Address of variable a: {id(c)}')
d = c
print(f"reference count of a: {sys.getrefcount(c)}")
print(f'Address of variable b: {id(d)}')

