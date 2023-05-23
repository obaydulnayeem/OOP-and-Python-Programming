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

""" MODULES ======================================================== """
# from external_file_name import * # to import all from the file
# from external_file_name import function_name # to import only a function 
# from external_file_name import function_name as new_function_name # to import a function as modified function name 


