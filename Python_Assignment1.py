'''
NAME - ANUJ SHILPI
ENROLLMENT NO. - 0176AL221028
BRANCH - CSE-AIML
BATCH - PYTHON(batch - 6)
'''


#Question 1 - Create a calculator
'''
print("Enter the operation you want to perform on numbers [+, *, -, /]")
op_list = ["+","-","/","*"]
num_list = []
m_num_list = ['y','n']
while(True):
    operation = input()
    if operation not in op_list:
        print("Please enter the correct operation")
        continue

    print("Enter the numbers.Make sure to don't write any string values : ")
    while(True):
        numbers = input()
        if numbers.isdigit():
            numbers = int(numbers)
            num_list.append(numbers)
            if len(num_list)<2:
                continue
            else:
                print("Do you want to enter more numbers.Write 'y' for Yes and 'n' for No")
                while(True):
                    m_num = input()
                    if m_num not in m_num_list:
                        print("Please enter 'y' for Yes and 'n' for No")
                        continue
                    elif m_num in m_num_list and m_num == 'y':
                        print("Enter numbers")
                        break
                    else:
                        break
            if m_num == 'y':
                continue
            else:
                break
        else:
            print("Please enter the integer values")
            continue


    if operation == "+":
        r_add = 0
        for num in num_list:
            r_add = r_add+num
        print("The addition of numbers is :",r_add)
    elif operation == "-":
        r_sub = num_list[0]
        for i in range(1,len(num_list)):
            r_sub = r_sub-num_list[i]
        print("The subtraction of numbers is :",r_sub)
    elif operation == "*":
        r_mul = 1
        for num in num_list:
            r_mul = r_mul*num
        print("The multiplication of numbers is :",r_mul)
    elif operation == "/":
        r_div = num_list[0]
        for i in range(1,len(num_list)):
            r_div = r_div/num_list[i]
        print("The division of numbers is :",r_div)


    m_cal = input("Do you want to perform more calculations.Write 'y' for Yes and 'n' for No \n")
    if m_cal in m_num_list and m_cal=='y':
        print("Enter the operation you want to perform on numbers [+, *, -, /]")
        num_list.clear()
        continue

    else:
        break

'''








#Question-2 : Given an array with positive and negative integers.You have to find out sum of longest sequence of negative numbers.
              # 1 -  If there is no negative numbers then return -1
              # 2 -  If there is more than 1 longest sequence then take sum of them.
""""
        # arr1 = [-5,3,-2,-7,5,-7,-3,-1,4,3]
        # output = -11
        # 
        # arr2 = [5,2,6,3,9,7,5,2,9]
        # output = -1
        # 
        # arr3 = [-3,-4,-2,4,5,-6,-1,-2,4,-6,-7,8]
        # output = -18


arr = [-3,-4,-2,4,5,-6,-1,-2,4,-6,-7,8]          #arr3 
# arr = [-5,3,-2,-7,5,-7,-3,-1,4,3]              #arr1
# arr = [5,2,6,3,9,7,5,2,9]                      #arr2
len_arr = len(arr)

new_arr = []
new_element = 0

counter_list = []
counter = 0


re = 0
for el in arr:
    if el < 0:
        re += 1
if re == 0:
    print(-1)
    print("The array does not has any negative element")


for i,element in enumerate(arr):
   if element < 0 and arr.index(element) == 0:
       new_element = new_element + (element)
       counter = counter+1

   elif arr.index(element) >= 0:
       if arr[i-1] < 0 and arr[i] < 0:
           new_element = new_element + (element)
           counter = counter+1

       elif arr[i-1] < 0 and arr[i] > 0:
           new_arr.append(new_element)
           new_element = 0
           counter_list.append(counter)
           counter = 0

       elif arr[i-1] > 0 and arr[i] < 0:
           new_element = element
           counter = counter+1



if len(new_arr) > 0:

    # print(new_arr)
    # print(counter_list)

    counter_max = max(counter_list)
    # print(counter_max)
    no_times = counter_list.count(counter_max)
    # print(no_times)
    index_longest_seq = counter_list.index(counter_max)


    result_sum = 0
    if no_times == 1:
        print("The sum of longest sequence is :",new_arr[index_longest_seq])

    else:
        for i in range(0,len(counter_list)-1):
            for j in range(i+1,len(counter_list)):
                if counter_list[i] == counter_list[j]:
                    result_sum = new_arr[i]
                    result_sum = result_sum + new_arr[j]

        print("The sum of longest sequence is :", result_sum)

"""







#Question - 3 : WAP to check given password is match criteria
                # 1: 1 lower case letter
                # 2: 1 upper case letter
                # 3: 1 digit
                # 4: 8 > length < 20
                # 5: 1 special character except(@ # %)



print('''
        1: lower case letter
        2: 1 upper case letter
        3: 1 digit
        4: 8 > length < 20
        5: 1 special character except(@ # %)
''')


d_count = 0
l_count = 0
u_count = 0
special_char_list = ["@","#","%"]
special_char_list1 = ["!","$","^","&","*","+","-","/",".",",","\\","(",")","_","{","}","[","]",";",":",";'","\""]
j = 0
while(True):
    password = input("Enter the password which match the above criteria: \n")
    if len(password) >= 8 and len(password) < 19:
        for i,char in enumerate(password):
            if char in special_char_list or char in special_char_list1:
                if char in special_char_list1:
                    pass
                else:
                    print(f"Use special character other than {special_char_list}. Use like {special_char_list1}")
                    break

            elif char.isdigit():
                d_count += 1

            elif char.islower():
                l_count += 1

            elif char.isupper():
                u_count += 1

            else:
                print("Password does not match the criteria")
                break
            j = i
        if j == len(password) - 1 or d_count == 0 or l_count == 0 or u_count == 0:
            if d_count == 0 or l_count == 0 or u_count == 0:
                print("Password does not match the criteria")

            print("Press 'c' for continuining entering password and 'e' for exit")
            passw = input()
            if passw == 'c':
                continue
            else:
                exit()

    else:
        print("Password does not match the criteria")

        continue














