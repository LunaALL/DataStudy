###########################################
#
# while-loop으로 구현
# - user로부터 [학번, 이름] 입력받아서 2d list로 입력
# - 계속 입력할 것인지 물어보고 종료
# - 종료된 후에 학번과 이름 기준으로 sort하여 2d list print하기
#   (* key, lambda function에 대하여 조사한 후, 주석으로 설명 추가)
#
# - 프로그램 실행결과: (5명 입력한 결과를 shell에서 copy하여 주석으로 추가)
#    (1) 학번으로 sort한 결과
#    (2) 이름으로 sort한 결과
#
###########################################

print('\n[Problem]\n')

student = []  # 학번, 이름을 저장할 2D 리스트


# Start Code Here --------------------------------------
i=0
while True:
    student.append(input(" ex) 2014210020,김준기 으로 입력. ").split(','))
    print(student[i])
    i=i+1
    a = input(" 계속 진행? 엔터 or n :")
    if a.lower() == 'n':
        break


student_id = sorted(student, key=lambda x: x[0])
student_name = sorted(student, key=lambda x: x[1])

# key:리스크의 내부 원소의 크기 비교를 하는것
# lambda function :이름이 없는 함수(1회용 함수)

print(f'Before Sort: {student}')  # 정렬전 리스트
print(f'After Sort by ID: {student_id}')  # <- 학번으로 정렬,필요한 경우, 변수를 바꾸세요.
print(f'After Sort by Name: {student_name}')  # <- 이름으로 정렬,필요한 경우, 변수를 바꾸세요.

# 실행결과(shell에서 copy해서 추가)


"""
실행결과를 copy해서 넣어주세요.






"""

# End Code Here --------------------------------------
