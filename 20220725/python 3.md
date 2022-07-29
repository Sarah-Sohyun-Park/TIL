# python 3

# 메서드

- 함수의 연장선이다.

- 데이터구조. 메서드의 형식으로 자료를 정리할 수 있다.

## 1. str(불변)

word = 'ssafy' 일 때 word의 id. 즉, 주소가 생긴다.

문자열은 불가변형이므로

word = 'word' 를 추가하였을 때 word는 새로운 주소를 얻게 되고 'word'로 완전히 대체된다.

- str에 쓰는 메서드
  
  s.find(x) - 첫번째로 발견된 x를 반환, 없으면 -1 반환
  
  s.index(x) - 첫번째로 발견된 x를 반환, 없으면 error
  
  s.isalpha() - 알파벳 여부를 확인하며, 알파벳과 유사한 문자들을 포함한다(한글, 동그라미 안의 문자)
  
  s.islower() - 소문자 여부 확인
  
  s.isupper() - 대문자 여부 확인
  
  s.istitle() - 첫번째 문자만 대문자, 나머지는 소문자임을 확인
  
  s.replace(old, new, [count]) - old를 모두  new로 바꾸며 count를 부가적으로 추가시에 처음 n번째까지만 변환
  
  **s.strip([chars])** - 공백 또는 특정 문자 제거하기
  
  s.rstrip(), s.lstrip()은 각각 오른쪽 왼쪽 공백만 없애줌
  
  s.split([chars]) - [chars]를 기준으로 나눔
  
  **'seperator'.join([iterable]) **- seperator로 구분자 합침
  
  s.capitalize() - 문장의 첫문자 대문자로, 나머지 소문자로
  
  s.title() -첫문자 대문자로 나머지 소문자로
  
  s.upper() - 모두 대문자로 변경
  
  s.lower() - 모두 소문자로 변경
  
  s.swapcase() -대문자 소문자 반대로

- 숫자
  
  isdecimal() - 숫자 여부 확인
  
  isdigit() - 숫자, 소수 등 포함한 수
  
  isnumeric() - 로마숫자, 동그라미안의 숫자 포함

## 2. list(가변)

- list에 쓰는 메서드

    l.append(x) - x를 리스트 마지막 항목에 추가

    **l.insert(i, x)** - 인덱스 i 에 x를 넣으면 된다.

    l.remove(x) - 리스트의 가장 왼쪽에 있는 x를 제거()없을 경우 error

    l.pop() -오른쪽에 있는 항목부터 반환 후 x를 제거

    l.pop(i) - 인덱스 i에 있는 항목을 반환 후에 제거

    l.extend(m) - +=와 같은 기능으로 리스트 끝에 추가(m은 순회형)

    **l.index(x, start, end)** - 가장 왼쪽에 있는

    l.reverse() - 리스트 거꾸로 정렬

    l.sort - 숫자 정렬

    sorted(l)와 구분

    **l.count(x)** - 리스트에 x항목이 몇개 존재하는지 갯수 반환(없으면 0 반환)

    l.clear() - 내부의 모든 값 삭제

    del은 리스트 자체 삭제

## 3. tuple(불변)

- tuple에 쓰는 메서드
  
  대부분 list와 유사하나 , 변경 불가능 
  
  **tuple[i]로 값을 추출하고 값을 추가할 때 +=, * 2 사용(확장연산자로 값을 병합해서 재할당 , append, extend 불가)**
  
  (같은 자료형만 할당?)

## 4. set( 순서없음, 가변)

- 중복되는 함수는 하나만 저장
  
  s.copy() - 얕은 복사 반환
  
  s.add(x) - x가 set에 없다면 추가(랜덤 추가)
  
  s.pop() - 랜덤하게 항목 반환하고 비어있는 경우 error
  
  s.remove(x) - x에서 set을 삭제, 항목이 없는 경우 error
  
  s.discard(x) - x가 set에 있는 경우 삭제, 아니어도 에러 안남
  
  s. clear() - 모든 항목 제거
  
  s.isdisjoint(t) - 서로 같은 항목 없을 경우 true
  
  s.issubset(t) - set이 t의 하위 셋인 경우 true
  
   s.issuperset(t) - t가 set의 하위 셋인 경우 true

## 5. dict(key불변, value가변)

- dict 메서드
  
  d.clear() - 모든 항목 제거
  
  d.copy() - 얕은 복사
  
  d.keys -
  
  d.values - 
  
  d.items -
  
  d.get(k) -키의 벨류를 반환 없으면 None
  
  d.get(k, v) - 키의 벨류 반환 없으면 v 반환
  
  d.pop(k) - 키의 벨류를 반환 없으면 error
  
  d.pop(k, v) - 키의 벨류 반환 후 삭제, 없으면 v 반환
  
  d.update

## 6. 복사

- 할당
  
  리스트와 같은 사물함 사용

- 얕은 복사
  
  새로 이스트 만들어 id(주소)가 다름

    단 2차원 부터는 불가능함

- 깊은 복사
  
  import copy
  
  copy.deepcopy(2차원 이상의 리스트)

## EXTRA

a in 'apple'(리스트, 스트링 가능)

vscode의 terminal에서 잘못 들어갔을 때 exit()치고 enter
