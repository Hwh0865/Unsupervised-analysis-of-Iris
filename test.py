import os

# 测试4
with open("test.txt", 'r', encoding='utf-8') as rfile:
    students = rfile.readlines()
    print(students)
print(len(students))



# 测试3
# （1） < （默认）左对齐、 > 右对齐、 ^ 中间对齐、= （只用于数字）在小数点后进行补齐
# （2）取位数"{:4s}"、"{:.2f}"
# 取10位左对齐，取10位右对齐    --->hello     and     world
# print('{:10s}and{:>10s}'.format("hello", "world"))
# print(len("     world"))  # 10
# # 取10位中间对齐  --->  hello   and  world
# print('{:^10s}and{:^10s}'.format('hello', 'world'))

# 测试2
# filename = "test.txt"
# stu_lst = []
# if os.path.exists(filename):
#     with open(filename, 'r', encoding='utf-8') as rfile:
#         # "{'id': '1', 'name': '4', 'English': 4.0, 'Python': 4.0, 'Java': 4.0}\n"
#         # "{'id': '2', 'name': '2', 'English': 2.0, 'Python': 2.0, 'Java': 2.0}\n"
#         # 返回的是列表，每个元素是字符串
#         students = rfile.readlines()
#         for item in students:
#             dit = eval(item)
#             if dit['id'] == '3':
#                 stu_lst.append(dit)
#                 print(dit)
#         print(stu_lst)
#         stu_lst.clear()
#         print(stu_lst)


# 测试1
# stu_lst = [{'id': '1', 'name': '4', 'English': 4.0, 'Python': 4.0, 'Java': 4.0},
#            {'id': '2', 'name': '2', 'English': 2.0, 'Python': 2.0, 'Java': 2.0},
#            {'id': '3', 'name': '2', 'English': 2.0, 'Python': 2.0, 'Java': 90.0},
#            {'id': '4', 'name': '2', 'English': 2.0, 'Python': 2.0, 'Java': 10.0},
#            {'id': '5', 'name': '2', 'English': 2.0, 'Python': 2.0, 'Java': 70.0}
#            ]
# filepath = open(filename, 'w', encoding='utf-8')
# for item in stu_lst:
#     filepath.write(str(item) + '\n')
#
# filepath.close()
