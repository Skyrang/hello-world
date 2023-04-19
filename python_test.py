#INPUT을 사용한 리스트 구조
# list1=[]
# s=input('입력하세요 : ')  
# list1.append(s)

# print(list1)



# list1=[]
# s=int(input('입력하세요 : '))
# list1.append(s)

# print(list1)



# s=list(input().split())

# print(s)



# N=5

# list1=[]

# for i in range(N):
#     list1.append(input())

#     print(list1)



# N=5

# list1=[]

# for i in range(N):
#     list1.append(int(input()))

#     print(list1)



# #리스트 + 딕셔너리를 활용한 예제
# students = []
# student1 = {'name': 'John', 'age': 21}
# student2 = {'name': 'Jane', 'age': 23}
# students.append(student1)
# students.append(student2)
# print(students)



# employee = {'name': 'Alice', 'age': 30, 'skills': ['Python', 'Java', 'C++']}
# print(employee['skills'])



# keys = ['name', 'age', 'gender']
# values = ['Alice', 25, 'Female']
# person = dict(zip(keys, values))
# print(person)



# students = [{'name': 'John', 'age': 21}, {'name': 'Jane', 'age': 23}]
# print(students[0]['name'])



# students = []
# student1 = {'name': 'John', 'age': 21}
# student2 = {'name': 'Jane', 'age': 23}
# student3 = {'name': 'Bob', 'age': 20}
# students.extend([student1, student2, student3])
# print(students)



# #변형된 구구단
# # 2부터 9까지의 숫자 리스트 생성
# numbers = list(range(2, 10))

# # 리스트 컴프리헨션을 활용하여 변형된 구구단 생성
# gugudan = [[i*j for j in numbers] for i in numbers]

# #변형된 구구단 출력
# for row in gugudan:
#     for num in row:
#         print(num, end=' ')
#     print()



# #구구단 가로출력
# for i in range(1, 10):
#     for j in range(2, 10):
#         print(j,'x',i,'=',j*i,end='\t')
#     print()



# #1~3,4~6,7~9
# for i in range(1, 10, 3) :
#     for j in range(1, 10) :
#         for dan in range(i, i + 3) :
#             print(dan, '*', j, "=", dan * j, end=" ")
#         print()
#     print()



# #구구단 세로출력
# num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
 
# for i in num_list:
#     for j in num_list:
 
#         print("{} * {} = {}".format(i, j, i*j))



# # 학생들의 이름과 점수를 dictionary로 정의합니다.
# students = {
#     "Alice": 85,
#     "Bob": 72,
#     "Charlie": 98,
#     "David": 65,
#     "Emily": 77
# }

# # 학생들의 점수를 기준으로 내림차순으로 정렬합니다.
# sorted_students = sorted(students.items(), key=lambda x: x[1], reverse=True)

# # 학생들의 성적과 등수를 출력합니다.
# print("성적순으로 학생들을 나열합니다.")
# for i, (name, score) in enumerate(sorted_students):
#     print(f"{i+1}등: {name} ({score}점)")



# #영어 단어장 만들기
# # 빈 딕셔너리 생성
# word_dict = {}

# while True:
#     # 사용자로부터 영어 단어와 뜻을 입력받음
#     word = input("영어 단어를 입력하세요 (종료하려면 '종료' 입력): ")
    
#     # "종료"를 입력하면 프로그램 종료
#     if word == "종료":
#         break
    
#     meaning = input("뜻을 입력하세요: ")
    
#     # 입력받은 단어와 뜻을 딕셔너리에 추가
#     word_dict[word] = meaning
    
# # 단어장 출력
# print("영어 단어장")
# for word, meaning in word_dict.items():
#     print(f"{word}: {meaning}")



# #가장 빈번하게 등장한 항목 찾기
# # 파이썬 리스트 생성
# my_list = ['apple', 'banana', 'apple', 'orange', 'grape', 'banana', 'apple']

# # 리스트에서 가장 빈번하게 등장한 항목 찾기
# freq_dict = {}
# for item in my_list:
#     if item in freq_dict:
#         freq_dict[item] += 1
#     else:
#         freq_dict[item] = 1

# most_freq_item = max(freq_dict, key=freq_dict.get)

# # 결과 출력
# print(f"리스트에서 가장 빈번하게 등장한 항목: {most_freq_item}")



# #딕셔너리에서 특정 값 찾기
# # 파이썬 딕셔너리 생성
# my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 2, 'e': 1}

# # 찾을 값 입력 받기
# value = int(input("찾을 값을 입력하세요: "))

# # 딕셔너리에서 값이 일치하는 key들을 저장할 리스트 생성
# key_list = []

# # 딕셔너리에서 값이 일치하는 key들을 찾아 리스트에 저장
# for key, val in my_dict.items():
#     if val == value:
#         key_list.append(key)

# # 결과 출력
# print(f"값이 {value}인 key들: {key_list}")



# #리스트에서 딕셔너리 값 찾기
# # 파이썬 리스트 생성
# my_list = [{'a': 1, 'b': 2}, {'c': 3, 'd': 2}, {'e': 1, 'f': 4}, {'g': 2, 'h': 5}]

# # 찾을 값 입력 받기
# value = int(input("찾을 값을 입력하세요: "))

# # 값이 일치하는 요소들의 인덱스를 저장할 리스트 생성
# index_list = []

# # 리스트에서 값이 일치하는 요소들의 인덱스를 찾아 리스트에 저장
# for i in range(len(my_list)):
#     if value in my_list[i].values():
#         index_list.append(i)

# # 결과 출력
# print(f"값이 {value}인 요소들의 인덱스: {index_list}")



# #리스트 안 딕셔너리의 요소 합 구하기
# # 파이썬 리스트 생성
# my_list = [{'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6}]

# # 리스트 안 딕셔너리 value들의 합 계산
# total = 0
# for my_dict in my_list:
#     for value in my_dict.values():
#         total += value

# # 합 출력
# print(f"리스트 안 딕셔너리 value들의 합: {total}")



# #딕셔너리 안 리스트의 요소 합 구하기
# # 파이썬 딕셔너리 생성
# my_dict = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}

# # 딕셔너리 안 리스트 요소들의 합 계산
# total = 0
# for my_list in my_dict.values():
#     for num in my_list:
#         total += num

# # 합 출력
# print(f"딕셔너리 안 리스트 요소들의 합: {total}")



# #딕셔너리에서 value값이 가장 큰 key 찾기
# # 파이썬 딕셔너리 생성
# my_dict = {'a': 1, 'b': 5, 'c': 3, 'd': 2, 'e': 4}

# # value값이 가장 큰 key 찾기
# max_key = max(my_dict, key=my_dict.get)

# # 결과 출력
# print(f"value값이 가장 큰 key: {max_key}")



#학생 성적 관리 프로그램
# 학생들의 이름과 점수를 저장한 딕셔너리 생성
student1 = {'name': 'Alice', 'score': 80}
student2 = {'name': 'Bob', 'score': 90}
student3 = {'name': 'Charlie', 'score': 70}

# 딕셔너리를 리스트에 추가
students = [student1, student2, student3]

# 학생들의 성적 출력
for student in students:
    print(f"{student['name']}의 성적은 {student['score']}점입니다.")
    
# 학생들의 평균 점수 계산
total_score = 0
for student in students:
    total_score += student['score']

average_score = total_score / len(students)
print(f"학생들의 평균 점수는 {average_score}점입니다.")