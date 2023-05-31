def timer():
    def inner():
        print('time started')

        print('time ended')
    return inner

timer()()