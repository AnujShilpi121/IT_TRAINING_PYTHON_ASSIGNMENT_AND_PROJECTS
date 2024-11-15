'''
a = 0.1
b = 0.2
c = 0.3
print(True) if 0.1 + 0.2 == 0.3 else print(False)

a = []
# a.append(1)
# a.append(1)
# a.append(1)
# a.append(1)
# a.append(1)
# a.append(1)
print(a)



b = {1:2}
b.update({4:6})
b.update({44:1})
b.update({48:22})
b.update({46:3})
print(b)

a = input("enter the number")
print(type(a))
temp = int(a)
print(type(temp))
if temp == 2:
    print("yes")


'''
# l1 = []
# with open("just.txt","w+") as f:
#     l = f.read().split()
#     for i in l:
#         l1.append(i)
#
#     print(l1)
#     for j in l1:
#         if "anurag" == j:
#             print("Yes")

#
# email = "anujshilpi@gmail.com"
# if email.endswith("@gmail.com"):
#     print("Yes")


# with open("Answers.txt", 'r') as q:
#     lines = q.readlines()
#     print(type(lines))
# i = 0
# j = 1
# while i<len(lines):
#     print(lines[i+j])
#     i += 2


# l = [(0,[1,2,3]),(11,[11,22,33])]
# print(l[0][1][1])

import random
# import mysql.connector as con
# connection = con.connect(host='localhost',user='root',password='Anuj@123s',database='python_questions')
#
# cursor = connection.cursor()
# cursor.execute("SELECT * FROM questions")
# print(cursor.fetchall())
# ques = cursor.fetchall()
# random_ques = random.sample(ques,5)
# print(random_ques)
# print(cursor.fetchone())
# cursor.close()
# connection.close()

def pangrams(s):
    s = s.lower()

    alphabet_set = set('abcdefghijklmnopqrstuvwxyz')
    found_letters = set(c for c in s if c.isalpha())

    if found_letters == alphabet_set:
        return "pangram"

    else:
        return "not pangram"





if __name__ == "__main__":
    s = input()
    print(pangrams(s))


















