# function is a first class object
""" 
Inner Function:
    - akta function er moddhe r o function declare kora jay.
    - parameter hishebe jerokom number, string pathano jay, temni 'function' o pathano jay. 
    - akta function er vitor theke onno function k call kora jabe
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