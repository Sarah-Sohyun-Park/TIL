# python2

## 1. 조건문

- 조건문 기초

    if 조건 == True:

        실행코드

    else:

        실행코드

순차적 진행으로 가지치기 진행

**만약 첫번째 if 조건이 참으로 나온다면 다음 조건까지 가지 않는다.**



- 중첩 조건문

    if 조건:

        if 조건:

            실행코드

        elif 조건:

        실행코드

    else:

        실행코드



- 삼항연산자 (조건식 표현)

조건식 표현__true인 경우의 값__ if 조건 else __flase인 경우 값

```python
result = '홀수' if num % 2 else '짝수'
```

- 왼쪽참 오른쪽거짓
  
  

## 2. 반복문

- while문

```python
while 조건:
    코드실행
```

1. 무한루프 안되도록 종료 가능 조건인지 꼭 확인

2. 복합연산자 n += 1 - 연산과 저장을 함께하고싶을 때

   

- for문

``` python
for i in range: 
for idx in range(len(chars)): 
    print(chars[idx])
    실행코드
```

1. 순회가능하므로 별도의 종료조건 필요하지 않음

2. 순회가능 string tuple list range 사용 가능

3. 순회 시 마지막 값까지 접근해야함



- 딕셔너리 순회

```python
grade = {'john': 80, 'eric': 90}

for student in grades:
    print(student)

john
eric


for student in grades:
    print(student, grades[student])

john 80
eric 90
```

두개의 변수를 저장한다면 변수도 두개로

grades.keys()

grades.values()

grade.items()

```python
for student, grade in grades.items():
    print(student, grade)

john 80
eric 90
```



- enumerate 순회

```python
member = ['민수', '영희', '철수']

for idx, number in enumerate(members):
    print(idx, number)

list((enumerate(members)))

=> [(0, '민수'), (1, '영희'), (2, '철수')] - 튜플

list((enumerate(members, **start = 1**)))

=> [(1, '민수'), (2, '영희'), (3, '철수')] - 튜
```



- list comprehensive

    code for 변수 in iterable

    code for 변수 in iterable if 조건식

```python
cubic_list = []
for number in range(1, 4):
    cubic_list. append(numer ** 3)

print(cubic_list)



cubic_ list = [number ** 3 for number in range(1, 4) if 조건]
print(cubic_list)
=> [1, 8, 27]
```



- dictionary comprehensive

```python
for number in range(1, 4):
    cubic_dict[number] = number ** 3

print(cubic_dict)


cubic_dict = {number: number ** 3 for number in range(1, 4) if 조건}

print(cubic_list)
```



- 반복 제어

    break

    반복문을 종료

    continue

    지나가유

    else

    끝까지 실행하는 경우에만 else문 실행

    break 시에 else 문은 실행하지 않음

    pass

    거의 쓸 일 없지만 자리 채우기 용으로 쓸 수도



## 3. 함수

추상화와 분해를 위해 사용

내장함수, 외장함수, 사용자 정의 함수

선언(생성)과 호출(사용)

- 함수 기초

```python
def funtion_name((parameter ex) x, y):
    return returning_value
```

    일반적으로 함수 생성시 print 가 아닌 **return**값을 자주 쓴다.

    이 때 return 은 한번만 사용 가능하며 return a, b 형태의 튜플로 사용 가능하다.



    positional arguments - def add(x, y) 일때 add(2, 3) 을 하면 자동으로 x = 2, y = 3

    keyword arguments - def add(x, y) 일때 add(x = 2, y = 3) 으로 값을 지정해주는     것 , add(2, y = 3도 가능)

    단, add(x =2, 5)는 오류

    defult argument values- 기본값 설정 def add(x, y=0): return x + y

    add(2)는 2

    단, y를 다른 값으로 변경 가능



(parameter 과 argument 구분)

print는 쉼표로 여러 값 출력 가능 print('you', 'need', 'python')

패킹, 언패킹(튜플도 가능)



- 가변인자

    def add(*args) 또는 def add(a, b, *args)

    *args 가변인자 여러값 튜플로 생성



- 가변 키워드 인자

    **kwargs은 딕셔너리로 묶어 처리

    def family(**kwargs):

       for key, values in **kwargs.items()**:

            print(f'{key} : {values}')



    family(**father** = '아부지', **mother**: '어무니')

    father : 아부지
    mother : 어무니



    def print_family_name(father, mother, **pets)

    def print_family_name(*parents, **pets)

    family('아부지',  '어무니', dog = '멍멍이', cat = '냥냥이')



- scope

![](C:\Users\lifew\Desktop\ssafy8\TIL\img\scoop.png)

- 함수 응용

local에서 global **변수**로 global 변수 변환 가능



map(int, input().split()) =map(funtion, iterable)

fliter(odd, numbers) =filter(funtion, iterable)

zip(*iterables) => 리스트화로 결과 확인 => (list[(tuple), (tuple)])

모두 리스트화 가능

- lambda 
  
  lambda b, h : 0.5 * b * h 

- 재귀함수,,팩토리얼,,(for문 바꾸기 연습)

- 모듈 < 패키지 < 라이브러리
  
  ![](C:\Users\lifew\Desktop\ssafy8\TIL\img\moduel.png)
* 패키지 관리자(django)
  
  pip install
  
  pip uninstall
  
  pip list
  
  pip show
  
  pip freeze > requirments.txt
  
  pip install -r requirements.txt
  
  venv
