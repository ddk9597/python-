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
# len() : 문자열의 길이 측정
date = "2024-10-14"
print(len(date)) # 10

# strip() : 문자열 공백 지우기
# 기존 문자열에서 공백이 제거되는 것이 아니라 공백이 제거된 새로운 문자열이 생성,
# 변수가 다시 바인딩함
lang = "     python    3.    "
lang = lang.strip()
print (lang) # python    3.
# 문자와 문자 사이 공백은 제거되지 않는구나!
# 이렇게 해보면 될까?
lang = "     python    3.    "
lang =lang.replace(" ", "")
print (lang) # python3. // 잘 된다.

# 문자열 포매팅
# 복잡한 문자열 출력을 위해 c 언어 스타일의 포매팅을 지원함.
# %d : 정수, %s : 문자열, %f : 실수
# % 기호로 시작하는 형식 지정 문자열에 지정된 타입의 값이 전달되어
# 하나의 문자열이 된다.
name = "찬혁" # 문자열 %S 
score = 1000000 # 정수 %d
average = 300/7 # 실수 %f
print ("%s 님의 총점은 %d, 평균은 %f 입니다." % (name, score, average)) # 찬혁 님의 총점은 1000000, 평균은 42.857143 입니다.

# 문자열의 format 메서드를 사용하여 복잡한 문자열을 표현 가능함.
# 문자열 내로 값이 전달될 위치를 지정하기 위해 {} 기호를 사용한다.
# 데이터 타입과 상관 없이 사용 할 수 있어서 편리하다.
print("{} 님의 총점은 {}, 평균은 {} 입니다.".format(name, score, average)) # 찬혁 님의 총점은 1000000, 평균은 42.857142857142854 입니다.
# 더 많은 자릿수가 표시되는 이유 : format 메서드가 자동으로 실수의 정밀도를 최대한 표시하려고 하기 때문.

# 소수점 자리수 제한하기
# :.2f 같은 방식으로 형식을 지정 할 수 있음
print("{} 님의 총점은 {}, 평균은 {:.2f} 입니다.".format(name, score, average)) # 찬혁 님의 총점은 1000000, 평균은 42.86 입니다.

# f-string (파이썬 3.6.0 부터 지원함)
# 문자열 앞에 f를 붙인 문자열임
# f-string을 사용하는 경우 { } 안에 변수를 바로 사용 가능함
# 변수의 개수가 많은 경우 기존 foramt 메서드에 비해 가독성이 좋음
name = "찬혁"
age = "30"
점수 = 1000
평균 = 1000/7
print(f"{name}님의 총점은 {점수}점, 평균 점수는 {평균}, 나이는 {age}세 입니다.") # 찬혁님의 총점은 1000점, 평균 점수는 142.85714285714286, 나이는 30세 입니다.
# 변수명을 한글로 해도 되는구나(당연하지만 알아둬서 나쁠 건 없지)

# f-string 
btc_symbol = 'BTC/KRW'
btc_price = 28300000

doge_symbol = "DOGE/KRW"
doge_price = 193
print(f"암호화폐 : {btc_symbol}, 현재가 : {btc_price}") # 암호화폐 : BTC/KRW, 현재가 : 28300000
print(f"암호화폐 : {doge_symbol}, 현재가 : {doge_price}") # 암호화폐 : DOGE/KRW, 현재가 : 193
# 값을 정렬하여 출력하기
# 기본 자릿수 10칸으로 지정 후 우측 정렬 {변수 : >10}
# 천 단위에서 쉼표를 표시하려면 {변수:, } 라고 적어두면 된다.

print(f"암호화폐 : {btc_symbol:>10}, 현재가 : {btc_price:>10,}")   # 암호화폐 :    BTC/KRW, 현재가 : 28,300,000
print(f"암호화폐 : {doge_symbol:>10}, 현재가 : {doge_price:>10,}") # 암호화폐 :   DOGE/KRW, 현재가 :        193

# 실수를 다루는 경우 소수점 아래는 정해진 자릿수로 끊어서 표시하는 경우가 많음.
# 전체 자릿수 및 소수점 아래 자릿수를 지정하면 된다.
pi = 3.141592653589793
myStr = f"{pi:6.5f}"
print(myStr) # 3.14159
myStr2 = f"{pi:6.7f}" # 3.14159 반올림 처리 되는 것을 확인함.

# 타입 변환 
# 정수, 실수, 문자열 각 타입은 서로 다른 타입으로 변경될 수 있음(타입 변환)

# 정수를 실수로 변경하기
year = "2024"
year2 = int(year)
print (year2) # 2024
print (type(year2)) # <class 'int'>

# 쉼표가 있는 숫자를 정수로 형변환하기
price = "1,000,000"
# 콤마 제거 후 형변환
price2 = price.replace(",", "")
price3 = int(price2)
print (price3) # 1000000
print(type(price3)) # <class 'int'>

# 정수형을 문자형으로 변환하기
year = 2024
ymd = str(year) + "-10-15"
print (ymd) # 2024-10-15

# 정수를 실수로 변환하기 : float(정수)
integer = 10000
float = float(integer)
print (float) # 10000.0

# 실수를 정수로 변환하기 : int(실수)
# 소수점 아래 숫자는 버려지고 정수로 변환됨에 주의해야 한다.
num =10.5
int2 = int(num)
print(int2) # 10