# 파이썬 문자열 처리
# 문자열 정의 시 내부적으로 문자 하나 하나에 인덱스라고 불리는 숫자를 맵핑함
# 문자열 위쪽에는 시작 부분에서 0부터 1씩 순차 증가하는 인덱스, 아래에는 끝쪽에서 -1 부터 1씩 감소하는 인덱스가 존재함.
# 음수 인덱스 : 앞에서부터 글자를 셀 때 사용함

# 인덱싱 : 인덱스로 하나의 값을 선택하는것.
# 한 글자만 가져올 수 있음.
lang = "PYTHON"
print (lang[0]) # P
print (lang[-6]) # P

# 문자열 슬라이싱 : 문자열에서 범위를 지정하여 문자열의 일부를 가져오는 것.
# 한 글자 이상을 가져올 수 있음.
# 슬라이싱 : 시작 인덱스와 끝 인덱스가 필요하며, 대괄호 안에서 콜론(:) 으로 둘을 구분한다.
lang = "python3"
print(lang[0:8]) # python3
print(lang[0:7]) # python3
print(lang[0:6]) # python
print(lang[0:5]) # pytho
# !! 인덱스 번호 부여하는 방법 인덱싱과 슬라이싱이 다름!
# 인덱싱 : 문자 위에 번호가 존재한다고 생각
# 슬라이싱 : 문자 사이에 번호가 존재한다고 생각. 범위를 가져오는 것이기 때문에.

# 시작 인덱스 부분을 생략하면 처음부터 시작한 것으로 치고
# 끝 인덱스 부분을 생략하면 마지막까지 얻어오는 것으로 간주한다.

print (lang[:3]) # pyt
print (lang[3:]) # hon3

# 슬라이싱에서 세 번쨰 값을 지정하면 증감 폭을 설정함
# 두 개씩 건너뛰면서 데이터 가져오기
print (lang[::2]) # pto3
print (lang[1 : 5 : 2]) # yh

# 전체 데이터 역순으로 가져오기
print(lang[::-1]) # 3nohtyp

# 연습문제
# 주민등록번호 951026-1111111 에서 연월일(yyyyMMdd) 부분만 출력하기
reg_num = "990101-2234567"  # 예시 주민등록번호
gender = reg_num[7]
print(gender)

# 형변환
int_gender = int(gender)

# 남녀 구분
gender_bool = int_gender % 2
if gender_bool == 0:
    print("여성입니다.")
else:
    print("남성입니다.")

# 차량 번호에서 끝의 네자리 를 출력하기
car_num = "12가 1234"

print(car_num[4:])

# 실행 결과 예측하기
data = "ABC"
print(data[:] [:] [:] [-1]) # ABC ABC ABC C인줄 알았는데 C만 나오네 왜지?
print(data [:]) # ABC가 나온다..
print(data[:], data[:]) # ABC ABC가 나온다.
# 여러 번 슬라이싱 하는 것이 결과에 영향을 미치지 않고 마지막에 [-1]만 적용된다.
# 슬라이싱을 여러 번 해도 원본 문자열이 그대로 유지된다.. 그런데 왜 출력은 안되는 걸까?

# 최종 슬라이싱 결과만 적용되기 때문이다!
data = "0123456789"
print (data[:]) # 0123456789
print (data[:] [0:8]) # 01234567
print (data [:] [0:8] [2:]) # 234567
print (data[:] [0:8] [2:] [0]) # 2

# 따라서 ABC ABC ABC ABC가 나오게 하려면
data = "ABC"
print(data[:], data, data[:], data) # 전부니까 [:]를 써도 되고, 안써도 된다.

# 재밌다.


# -------------- 문자열 주요 함수 --------------

# 1. 문자열 합치기
# 문자열과 문자열을 더하면 두 문자열을 이어 붙인 새로운 문자열이 생성된다.
year = "2024"
month = "10"
day = "14"
seg = "-"
date = year + seg + month + seg + day
print(date)

# 2. 문자열 반복
# 문자열에 대해서 뺄셈, 나눗셈 연산자는 없다. 에러가 발생한다.
# 문자열에 대한 곱셈 연산은 문자열의 반복을 의미한다.
print(year * 3)
print(seg * 20)

# 3. 대문자와 소문자
# upper() : 대문자로 변경 / lower() : 소문자로 변경
abc = "xyz"
print(abc.upper()) # XYZ
xyz = "ABC"
print(xyz.lower()) # abc

# 4. 문자열 분리
# 문자열에 구분자가 있을 경우, 해당 구분자를 이용해서 문자열을 분리할 수 있음.
# split() : 구분자로 문자열 분리하기
date = "2021-10-14"
print(date.split("-")) # ['2021', '10', '14']

# 5. 문자열 변경
# 정수, 실수, 문자열은 값을 변경할 수 없는 타입.
# 문자열은 한 번 생성되면 변경 불가능함. 
# 슬라이싱이나 replace 함수를 사용하여 기존 문자열은 그대로 두고 새로운 문자열을 생성해야 함.
lang = "UTF-16"
lang2 = lang.replace("16", "8")
print (lang2) # UTF-8
# 슬라이싱 하기
lang3 = lang[:4] + "8"
print (lang3) # UTF-8

# 문자열에서 콤마 제거하기
price = "1,000,000"
price = price.replace(",", "")
print (price) # 1000000

# 6. 문자열 길이와 공백 제거
