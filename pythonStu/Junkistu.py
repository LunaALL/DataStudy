num=input("숫자 첫번째 입력")
num2=input("숫자 두번째 입력")
print("%s" % num)
print("%s" % num2)


######################

print('\n[Problem #3]\n')

string1 = 'hong gil dong   '
string2 = '   hong gil dong   '
string3 = '   hong gil dong'

def chagneString(input_string) :
    #---> Start Your Code
    temp=input_string.strip()
    temp=temp.split()
    str1=temp[0].capitalize()
    str2=temp[1].capitalize()
    str3=temp[2].capitalize()

    return str1+ " " +str2 + " " + str3

#---> Finish Your Code
result1 = chagneString(string1)
result2 = chagneString(string2)
result3 = chagneString(string3)

print(result1)
print(result2)
print(result3)


# 과제 4) 사용자로부터 이름을 입력받은 후, 모두 대문자로 바꾸고,
#        앞에 Hi를 붙여서 반환(return)하는 함수를 작성하세요.
# 조건 1) 이름을 모두 대문자로 바꾸는 문자열함수 사용
#     2) 이름과 인사말을 연결하는 문자열연산 사용

print('\n[Problem #4]\n')

# 이름을 입력받아서 대문자로 바꿔주는 함수 작성
#
def greet(name) :
#---> Start Your Code
    name=name.upper()
    return "Hi!!"+name
#---> Finish Your Code


# 사용자로부터 출력할 이름 입력받아서 변수 n에 할당
# input함수는 문자열 타입을 리턴

name = input("좋은 말할때 이름 적어라")

# 입력받은 이름 출력하기
print(greet(name))




########################################################
#
# 과제 5) 더하기(Addition)함수를 만드시오.
#
########################################################

print('\n[Problem #5]\n')


# 더하기함수 정의
# hint: 형변환함수 사용 (숫자더하기)
def Addition(num1, num2):
#---> Start Your Code

    return int(num1)+int(num2)
#---> Finish Your Code




# 사용자로부터 2개의 숫자 입력 받기
first_number = input('Input 1st Number:')
second_number = input('Input 2nd Number:')


# Add함수를 이용하여 더하기한 후, 결과 출력하기
print('Answer = ', Addition(first_number, second_number))



########################################################
#
#  수고하셨습니다.
#
########################################################

