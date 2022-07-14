'''
파이썬에서 모든 것은 객체로 이루어져 있다.
변수는 객체를 참조하고 있는 주소값이라 생각하면 된다.
a = 5 의 코드를 분석해보면
1. 5라는 값을 가지는 객체가 메모리 공간 어딘가에 생기고
2. 그 객체의 주소값을 a변수에 넘겨준다.

a: Logical address
a 변수에 저장된 실제 데이터 : 5값을 가지는 객체의 주솟값 : physical address
logical address 를 physical address로, 또는 그 반대로 변환 해주는 과정을 Address Binding 이라고 함.

파이썬에서 = 대입연산자는 바인딩을 의미한다.

'''

a = 5
print(f"Logical Address: a, Physical Address : {id(a)}")