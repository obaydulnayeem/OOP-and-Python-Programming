"""" BASIC INFO==================================="""
"""
    Uses of python:
        - Data science
        - AI
        - Machine learning
        - web crawlling, web development

    Others Info:
        - Indentation is so important in python
"""


""" PRINT=========================="""
# print('kopa python kopa')
# print(4534)


""" VARIABLE======================="""
# age = 45
# a = 3.3
# interest_rate = 2.3
# name = "Nayeem"
# district = 'Barishal'
# is_single = True
# is_sleeping = False
#print(age + a)


""" TYPE==================================================="""
# print(type(age))
# print(type(district))
# print(type(is_single))


""" COMMENT===================================================="""
"""
Ctrl + / --> single line
Alt + Shift + A --> multi line / doc string
"""

""" STRING========================================================================================"""
# print('Kodom Ali' + ' ' + 'Kacha Badam')
# text = f"Kodom Ali {age} living in {district}. Interesting with rate {interest_rate}%"  # fstring
# print(text)

#---------------------------------------------------------------------------------------------------
# name1 = 'Sakib\'s Khan' # escape -> \
# name2 = "Sakib Khan"
# # multiline string
# name3 = """   
#     Sakib Khan
#     Number One
# """
# # print(name1)

# for char in name2:
#     print(char)

# print(name2[3])
# print(name2[1:6])
# print(name2[-3])
# print(name2[::-1])

# name2[0] = 'R' # not possible

# if 'Khan' in name2:
#     print('exists')

#--------------------------------------
# string is a sequence of characters
# mutable -> changeable
# immutable -> we can not change it

""" TOUPLE ============================================================================= """
# touble kichu 'list' er kachakachi
# list er khetre generally same type data rakhe. jemon int er list, string er list, bool er list
    # but touple er khetre mix type er data rakhe.
# function theke ekadhik jinish return korte gele kaje lage.

# def multiple():
#     return 3, 4
# # print(multiple())  # touble -> (), list -> []
# things = 'pen', 'tripod', 'water bottle', 'charger', 'phone', 'web cam', 'sunglass'
# # print(things)
# # print(type(things))
# # print(things[0])
# # print(things[-2])
# # print(things[3:6])

# if 'phone' in things:
#     print('exists')

# for item in things:
#     print(item)

# things[0] = 'wagon' # not possible



""" INPUT==================================================================="""
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

# OTHERS----------------------------------------------
# a, b = map(int, input().split()) # input sample: 3 5


""" OPERATORS====================================================================="""
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


""" CONDITIONALS====================================="""
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


""" NESTED CONDITIONS====================================================================="""
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


""" WHILE LOOP ================================================================="""
# num = 1
# while num <= 10:
#     print(num)
#     num += 1 # or, num = num + 1


""" BREAK and CONTINUE ====================================="""
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


""" FOR LOOP ========================================="""
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


""" RANGE ====================================================="""
# for i in range(1, 10):
#     print(i)

# for i in range(1, 10, 2):
#     print(i)

# for i in range(5):
#     print(i)


""" FUNCTION ========================================================== """
# def double_it(num): # def -> define
#     result = num * 2
#     print(result)
#     return result
# double_it(8)
# #-------------------------------------
# def sum(num1, num2):
#     result = num1 + num2
#     return result

# total = sum(44, 39)
# print('total value', total)

# final = double_it(total)
# print('final value', final)

""" DEFAULT ARGS =========================================================================================="""
# default parameter ---------------
# def sum(num1, num2, num3 = 0): # num3 = 0 --> ai parameter er man na dileo kaj korbe
#     result = num1 + num2 + num3
#     return result

# total = sum(99, 11)
# print('total: ', total)

# args-------------------
# def all_sum(*numbers): # all_sum(num1, num2, *numbers) --> evabe dile 1st 2 ta  bade onno gula print hobe
#     print(numbers)
#     sum = 0
#     for num in numbers:
#         print(num)
#         sum = sum + num
#     return sum
# total = all_sum(45, 45, 75, 22, 76, 5, 2) # ekhane joto parameter pathai kono somossa nei
# print('all sum: ', total)


""" KARGS ============================================================================""" 
# def full_name(first, last):
#     name = f'Full name is: {first} {last}' # first + ' ' + last --> evabe dileo hobe
#     return name

# # name = full_name('Alu', 'Kodu') # taken parameters in order (serial wise)
# name = full_name(last='kodu', first='alu') # taken parameters not in order (not serial wise)
# print(name)

#---------------------------------------------------------------------------------------------
# def famous_name(first, last, **addition): # ** --> kargs --> key jukto args. 
#     name = f'{first} {last}'
#     # print(addition['title'])
#     for key, value in addition.items():
#         print(key, value)
#     return name

# name = famous_name(first='Taheri', last='Ali', title = 'hujur', addition='taheri', title2 = 'sheikh', last2 = 'ajhari')
# print(name)

# # So, def function_name(num1, num2, ..., *args, **kargs, ...)


""" RETURN MULTIPLE THINGS============================================================================="""
# def a_lot(num1, num2):
#     sum = num1 + num2
#     mult = num1 * num2
#     remain = num1 - num2
#     # return sum, mult, remain # normally return
#     return [sum, mult, remain] # list akare return

# everything = a_lot(55, 21)
# print(everything)


""" SCOPE ================================================================================================== """
# balance = 3000 # global scope variable

# def buy_things(item, price):
#     global balance 
#     print(f'Previous balance value', balance)
#     balance = balance - price # local scope variable. 
#     # We can access the global var without using the 'global' keyword
#     # But if we want to modify a global var, we have to use the 'global' keyword
#     print(f'Balance after buying {item}', balance)

# buy_things('sunglass', 1000)

""" BUILT IN FUNCTIONS ============================================================ """
# # ALL: https://docs.python.org/3/library/functions.html

# # Most used:
# # abs(), all(), any(), ascii(), bin(), bool(), enumerate(), dict(), dir(), compile(), complex(), float()
# # int(), input(), len(), globals(), locals(), map(), max(), min(), oct(), open(), pow(), range(), round()
# # sum(), super(), type(), print(), str(), any()

# # highest = max(45, 73, 22, 78, 84, 29)
# highest = max([45, 73, 22, 78, 84, 29]) # in array form
# smallest = min([45, 73, 22, 78, 84, 29])
# count = len([34, 65])
# print(highest, smallest, count)

""" MODULES ======================================================================================== """
# from external_file_name import * # to import all from the file
# from external_file_name import function_name # to import only a function 
# from external_file_name import function_name as new_function_name # to import a function as modified function name 


""" LIST (array / collection) ======================================================================"""
# # https://docs.python.org/3/tutorial/datastructures.html

# # index:    0   1     2   3    4    5    6    7    8    9   10   11   12   13 
# numbers = [45,  64,  74,  8,  95,  34,  67,  78,  34,  23,  67,  89,  56,  23]
# # index:  -14  -13   -12 -11  -10  -9   -8   -7   -6   -5   -4   -3   -2   -1

# print(numbers[3], numbers[-3])

# # list( start : end )
# print(numbers[2:6])

# # list( start : end : step )
# print(numbers[1:7:1])
# print(numbers[1:7:2])
# print(numbers[2:7:-1]) # not works, cause 2 index theke 7 index projonto jaowa jay na
# print(numbers[7:2:-1]) # 7 index theke ulta dik theke 2 index projonto 
# print(numbers[7:2:-2]) # 7 index theke ulta dik theke 2 index projonto akta akta bad diye 
# print(numbers[4:]) # 4 index theke baki shob
# print(numbers[:5]) # 5 index er ag projonto shobgula
# print(numbers[:]) # shuru theke shesh shob / copy a list
# print(numbers[::-1]) # shesh theke shuru / reverse the full array

""" more about LIST ======================================================================================"""
# numbers = [12, 43, 65, 85]
# numbers.append(56)
# print(numbers)

# numbers.insert(2, 71) #insert(index, value)
# print(numbers)

# numbers.remove(65)
# print(numbers)

# if 9 in numbers:
#     numbers.remove(9)
# print(numbers)

# last = numbers.pop()
# print(last, numbers)

# index = numbers.index(71)
# print(index)

# if 3 in numbers:
#     ind = numbers.index(3)
#     print(ind)

# sorted = numbers.sort()
# print(numbers)

""" LIST comprehension / advanced =============================================================================="""
# numbers = [45, 64, 26, 73, 85, 34, 74, 34, 23, 56]
# odds = []
# for num in numbers:
#     if num % 2 == 1 and num % 5 == 0:
#         odds.append(num)

# print(odds)

# odd_nums = [num for num in numbers if num % 2 == 1 if num % 5 == 0]
# print(odd_nums)

#------------------------------------------------------------------------
# players = ['sakib', 'musfik', 'mustafiz']
# ages = [34, 35, 36]

# age_comb = []
# for player in players:
#     print('player:', player)
#     for age in ages:
#         print(player, age)
#         age_comb.append([player, age])
# print(age_comb)

# age_comb2 = [[player, age] for player in players for age in ages]
# print(age_comb2)

""" SET ================================================================================================= """
# set: unique items collection

# list --> []
# touple --> ()
# set --> {}

# numbers = [12, 56, 65, 23, 12, 65]
# print(numbers)
# numbers_set = set(numbers)
# print(numbers_set)
# numbers_set.add(55) # randomwise jekono index e add hote pare
# print(numbers_set)
# # print(numbers_set[2]) # not possible
# # numbers_set[1] = 5 # not possible
# numbers_set.remove(12)

# for item in numbers_set:
#     print(item)

# if 23 in numbers_set:
#     print('exists')

# A = {1, 3, 5}
# B = {1, 2, 3, 4, 5}
# print(A & B) # A intersection B
# print(A | B) # A union B


""" DICTIONARY ======================================================================================= """
# # key value pair
# # dictionary
# # object
# # hash table
# # overlap with set
# #-----------------------------------------------------------
# # numbers = [12, 43, 65, 85, 97, 34, 25, 75, 67]
# # person1 = ['kala chan', 'kalipur', 23, 'student'] # every person er jonno aladavabe key  mone rakha koshtokor

# # solution: 
# person = {'name': 'Kala Pakhi', 'address': 'Kaliapur', 'age': '23', 'job': 'bekar'}
# print(person)
# print(person['job'])
# print(person.keys())
# print(person.values())
# person['language'] = 'python'
# person['name'] = 'sada pakhi'
# del person['age']
# print(person)

# for item in person:
#     print(item) # only key pabo, value pacchi na

# # special dictionary looping
# for key, value in person.items():
#     print(key, value)

""" LIST INDEX ===================================================================================== """
# numbers = [12, 43, 65, 85, 97, 34, 25, 75, 67]
# for num in numbers:
#     print(num) # ai loop er maddhome index pai na. only value pai

# # solution:
# for i, num in enumerate(numbers):
#     print(i, num) # akhn index, value 2tai paowa jabe

""" BUILT IN MODULES =================================================================================="""
# # floor, ceil, gcd, common factor, infinity, sqrt, permutation, reminder, exponential, log, sin, cos, 
# # random, suffle, os, turtle, and so on...
# from math import *
# from random import * 
# from time import sleep
# result = ceil(4.6)
# print(result)
# print(random())
# print(randint(1, 100))
# sleep(4)
# print(choice(['sakib', 'mash', 'mush', 'rid', 'musta']))

""" PACKAGES ================================================================================ """
# # https://pypi.org/project/PyAutoGUI/
# # https://pyautogui.readthedocs.io/en/latest/
# # check: pip --version # eta python install korar somoy e aksathe hoye jay

# # Popular packages: numpy, matplotlib, pytors, cykitlearn, beautiful soup, .... [banan e vul ache]

# # AUTO TYPE ---------------------------------------------------------
# # import pyautogui
# # from time import sleep
# # sleep(3)
# # for i in range(0, 3):
# #     pyautogui.write('Valo hoye ja. akhn o somoy ache', interval=0.25)
# #     pyautogui.press('enter')

# # CAM --------------------------------------------------------
# import cv2
# cam = cv2.VideoCapture(0) # ekhane 1, 2, 3, 4, ... etc deya lagte pare
# while True: 
#    _, frame = cam.read()
#    cv2.imshow('my cam', frame)
#    cv2.waitKey(1)

""" EXCEPTIONS ================================================================================== """
# https://docs.python.org/3/tutorial/errors.html

"""
    try: 
        code...
    except: # kichu language e catch use kore
        code er moddhe kono kichute kaj na korle eta kaj korbe
    finally: 
         chaile etao try er sathe use kora jay.
         or, try, except er satheo aksathe kora jay
"""
# try:    
#     result = 45/0 # division by zero error
# except:
#     print('Error happended')
# finally:
#     print('finally here')

""" FILE ========================================================================== """
# .csv -> comma separated value
# .txt -> text file

# with open('message.txt', 'w') as file: # w -> write
#     file.write('I love you, Python!')

# with open('message.txt', 'a') as file: # a -> append -> jog kora
#     file.write('I love you, Python!')

# with open('message.txt', 'r') as file: # r -> read
#     text = file.read()
#     print(text)

""" LAMBDA FUNCTION ============================================================== """
# # def doubled(x):
# #     return x*2

# doubled = lambda num: num * 2 # uporer 2 line er poriborte evabe 1 line e lekha jay
# squared = lambda num: num * num
# add = lambda x, y : x + y

# result1 = doubled(44)
# result2 = squared(9)
# result3 = add(4, 6)

# print(result1, result2, result3)

""" MAP ================================================================================ """
# numbers = [12, 43, 65, 85, 97, 34, 25, 75, 67]
# doubled = lambda num: num * 2
# doubled_nums = map(doubled, numbers)
# # doubled_nums = map(lambda x : x*2, numbers) # uporer line er poriborte evabeo lekha jabe
# squared_nums = map(lambda x : x*x, numbers)

# print(numbers)
# print(list(doubled_nums))
# print(list(squared_nums))

# DICTIONARY, FILTER, LAMBDA together------------------------------------------------------------------------

# actors = [
#     {'name': 'sabana', 'age': 66},
#     {'name': 'sabnur', 'age': 25},
#     {'name': 'sabina nur', 'age': 35},
#     {'name': 'srabonti', 'age': 40}
# ]

# juniors = filter(lambda actor : actor['age'] < 40, actors) # 'actor' er jaygay onno kono var use korleo hobe. jemon 'x'
# print(list(juniors))

# Fivers = filter(lambda actor : actor['age'] % 5 == 0, actors)
# print(list(Fivers))
