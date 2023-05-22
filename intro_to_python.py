# BASIC INFO===================================
"""
    Uses of python:
        - Data science
        - AI
        - Machine learning
        - web crawlling, web development

    Others Info:
        - Indentation is so important in python
"""


# PRINT==========================
#print('kopa python kopa')
#print(4534)


# VARIABLE=======================
# age = 45
# a = 3.3
# interest_rate = 2.3
# name = "Nayeem"
# district = 'Barishal'
# is_single = True
# is_sleeping = False
#print(age + a)


# TYPE===================================================
# print(type(age))
# print(type(district))
# print(type(is_single))


# COMMENT====================================================
"""
Ctrl + / --> single line
Alt + Shift + A --> multi line / doc string
"""

# STRING========================================================================================
# print('Kodom Ali' + ' ' + 'Kacha Badam')
# text = f"Kodom Ali {age} living in {district}. Interesting with rate {interest_rate}%"  # fstring
# print(text)


# INPUT===================================================================
# print('Now I need money')
# input()
# input('Give me some money: ')
# money = input('Give me some money: ')
# print("Here is your money:", money)

# first_money = input('Kodom Ali, Dosto kichu tk dey: ')
# second_money = input('Peyara Begum, Dosto kichu tk dey: ')
# print(type(first_money))
# by default the input from user will be string type
# first_money_int = int(first_money)
#print(type(first_money_int))
# second_money_int = int(second_money)
# print("Money I got from kodom", first_money, 'and from peyara', second_money)
# total = first_money_int + second_money_int
# print('Total Money I got: ', total)


# OPERATORS=====================================================================
# +, -, *, /, %, //, **
# num1 = 15
# num2 = 6
# print(num1 + num2)
# print(num1 - num2)
# print(num1 * num2)
# print(num1 / num2)
# print(10/3)
# print(10%3) # reminder / vag sesh
# print(10//3) # purno vag fol
# print(5**2) ## power
# COMPARISON:
# >, <, >=, <=, ==, !==, +=, -=, *=, /=, in, not, not in, is, is not 
# not available: ++ --


# CONDITIONALS=====================================
# in, not, not in, is, is not, and, or

# a = 3
# if a > 5:
#     print( '5 er beshi')
#     print('koto beshi ke jane')
# elif a > 2: # not available: else if
#     print('Olpo boro')
# else: 
#     print('chuti chuti rate lombi hoye')

# boss = False
# if boss is True:
#     print('tel er baksho niye ashtechi')
# else: 
#     print('lunch er pore ashen')


# NESTED CONDITIONS=====================================================================
# coin = 'head'
# if boss == True:
#     print('boss, you are xoss!')
#     if coin == 'tail':
#         print('batting')
#     else:
#         print('bowling')
#         if 5 > 2 or boss != True:
#             print('do something')
#             if 8 % 2 == 0 and 5 % 2 == 1:
#                 print('8 is even')
# else:
#     print('you are not a boss!')


# WHILE LOOP =================================================================
# num = 1
# while num <= 10:
#     print(num)
#     num += 1 # or, num = num + 1


# BREAK and CONTINUE =====================================
# num = 1
# while num <= 10:
#     print(num)
#     num = num + 1
#     if num == 5:
#         break

#-------------------------
# 'continue' actually means 'skip'
# num = 0
# while num <= 10:
#     num = num + 1
#     if num % 2 == 0:
#         continue
#     print(num)


# FOR LOOP =========================================
# numbers = [5, 10, 15, 20, 25]
# sum = 0
# for num in numbers:
#     # print(num)
#     sum = sum + num
#     if sum > 20: 
#         print('bigger values')
# print(sum)

#--------------------------------------
# text = 'Pagla Haowar tore...'
# for char in text:
#     print(char)

#--------------------------------------------
# friends = ['nayeem', 'tanvir', 'shuvo', 'anis']
# for friend in friends:
#     print(friend)

# for index, friend in enumerate(friends):
#     print(index, friend)


# RANGE =====================================================
# for i in range(1, 10):
#     print(i)

# for i in range(1, 10, 2):
#     print(i)
