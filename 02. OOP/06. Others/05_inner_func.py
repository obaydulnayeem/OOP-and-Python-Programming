# function is a first class object
""" 
- akta function er moddhe r o functio declare kora jay.
- python e parameter hishebe jerokom number, string paowa jay, temni 'function' o pathano jay. 

"""

def double_decker():
    print('starting the double decker')

    def inner_fun():
        print('inside the inner')
        return 3000
    return inner_fun

# print(double_decker())
# print(double_decker()()) # karon double_decker() o akta function

def do_something(work):
    print('work started')
    print(work)
    print('work ended')

def coding():
    print('coding in python')

def sleeping():
    print('sleeping and dreaming in python')

# do_something(2)
# do_something('ami busy')

# do_something(coding) # function er moddhe function pathaichi

do_something(sleeping)