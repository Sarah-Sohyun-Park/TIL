# python 4.md

## 객체지향 프로그램(OOP)이란?

컴퓨터 프로그래밍의 패러다임으로 **객체**들의 **상호작용**에 초점을 둔다.

각 개체는 정보와 기능(행동)이 분리되어 있어 있으며, 이 내용은 추상화 되어 있다.

장점- 필요한 부분만 수정하면 된다. 대규모 소프트웨어 개발에 적합하다.

단점- 설계시 오랜 시간이 걸리며, 실행 속도가 절차지행보다 느리다.

## OOP 기초

- 객체
  
  객체는 타입(어떤 연산자, 조작 가능?), 변수(속성, 정보)와 함수(메서드, 행동)으로 이루어진다

- 클래스,  인스턴스
  
  1. 클래스 - 설계도
  
  2. 인스턴스 - 객체에 포함된 개념으로 개별화된 실체가 클래스의 인스턴스라고 본다. 
  
  클래스는 우리가 알고 있는 dict, list, str, int, float 등을 포함한다.
  
  a = [1, 2, 3]일 때 a는 list의 인스턴스 라고 불린다.

- 기본 문법
  
  1. 클래스 정의 - pascal case로 MyClass와 같이 첫문자 대문자로 삽입
  
  2. 인스턴스 생성 - sneak case로 my_instance = MyClass()
  
  3. 매서드 호출 - my_instance. my_method()
  
  4. 속성 - my_instance.My_attribute

- 객체 비교
  
  1. == 쌍둥이와 같이 같아보이면 True
  
  2. is 완전히 동일한 객체(id 가 같음)일 때 True
  
  a = [1, 2, 3] b = [1, 2, 3] 일 때 a==b성립
  
  a = [1, 2, 3] a = b일 때 a is b성립

## OOP 속성

- 속성(return 안쓰네,,함수만,,)
  
  1. 클래스의 객체들이 가질 데이터
  
  2. 클래스 변수/인스턴스 변수가 존재

- 인스턴스 변수
  
  1. 인스턴스의 고유한 변수
  
  ```python
  def __init__(self, name):
      self.name = name
  ```
  
  생성자 \_\__init\_\__ 메서드에 의해서  인스턴스.name = '' 으로 할당 및 접근
  
  <mark>**인스턴스는 인스턴스 변수와 클래스 변수 모두 사용가능</mark>**
  
  <mark>인스턴스와 클래스 모두 이름 공간이 있으며 인스턴스에서 접근했을 때는 인스턴스 </mark>클래스 순으로 탐색

- 클래스 변수
  
  1. 한 클래스가 공유하는 값
  
  ```python
  class Person:
      blood_color = 'red'
      population = 100
      count = 0
  
      def __init__(self, name):
          self.name = name
          Person.count += 1
  ```

      print(Circle.blood_color) # 'red'
      person1 = Person(**'지민'**)일 때

      person1.blood_color #'red' => c1에 없기 때문에 class의 것을 가져온다.

      **단, person1.blood_color = 'blue'로 설정하면 객체의 변수가 생성되어 #bule가       출력한다.**

      인스턴스 생성마다 count 값이 올라가고 print(Person.count)값을 얻을 수 있다.

## OOP 메서드

클래스는 인스턴스 메서드 호출 불가, 인스턴스는 모두 접근 가능

- 인스턴스 메서드

호출시 첫 인자로 (self)를 받음

- **매직 매서드**

- 클래스 메서드

@classmethod 데코레이터를 활용함

글로벌 값으로 함수 생성시 사용

호출시 첫 인자로 (cls)를 받음

- 스태틱 메서드

인스턴스 변수, 클래스 변수를 전혀 다루지 않는 메서드

**하지만 인스턴스 클래스 모두 접근가능**

@staticmethod 데코레이터를 사용함

  ![](python%204_assets/2022-07-27-20-11-10-image.png)

- **?데코레이터에 새로운 기능 부여?**

## 객체 지향의 핵심

- 추상화

복잡한 것은 숨기고 필요한 것만 드러냄

- 상속

객체를 상속받음

코드 재사용성이 높아짐

**인스턴스 자식클래스 부모클래스 순으로 탐색**

다중상속의 경우 앞에 언급된 객체로 처리(object.mro()로 상속 관계 순서 확인 가능)

![](python%204_assets/2022-07-27-20-26-24-image.png)

![](python%204_assets/2022-07-27-20-25-09-image.png)

isinstance(object, classinfo)

**issubclass(class, classinfo)**

- 다형성

**인스턴스 자식클래스 부모클래스 순으로 탐색**

인스턴스에 부모클래스에 있는 함수를 재정의 해서 설정하면 재정의 한 것으로 도출 가능(super후 재추출도 가능)

- 캡슐화
1. public access modifier(언더바 없음)

2. protect access modifier(언더바 한개)

3. private access modifier(언더바 두개 호출, 상속 불가)

      ![](python%204_assets/2022-07-27-20-38-34-image.png)

      **getter에는 @property (변수 값 읽기)**

     **setter에는 @변수.setter 사용 (변수 값 설정)**

--> protect private 둘 다 사용가능

## 디버깅

- 조건문 반복문

print로 자주 확인하는 습관

- syntax error - 문법 오류

assign to literal -할당 오류

eol/eof - 괄호 오류

name error - 선언 안됨

type error - 타입 오류

zero dividision error - 0으로 나눔

value error - 타입은 맞으나 값이 틀림

index error - 인덱스가 없음

key error - 키가 없음

model not found error - 모듈 못찾을 때

import error- import '____' - 빈칸 잘못 썼을 때

keyboard interrupt - 내부 무한반복 및 오류로 임의 종료

indentation error - tab 및 위치 오류

- 예외 처리

![](python%204_assets/2022-07-27-20-53-12-image.png)
