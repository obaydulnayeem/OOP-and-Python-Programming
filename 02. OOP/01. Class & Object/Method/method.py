# def call(): # method
#     print('calling someone I dont know')
#     return 'call done'

class Phone:
    price = 12000 # features / properties / attributes 
    color = 'blue'
    brand = 'samsung'
    features = ['camera', 'speaker', 'hammer']

    def call(self): # python e 'self' parameter ta default  hishebe diye dite hoy. noyto shobkichu thikvabe kaj korbe na.
        print('calling one person')

    def send_sms(self, phone, sms): 
        text = f'sending sms to: {phone} and message: {sms}'
        return text

my_phone = Phone() # object
print(my_phone.features)

my_phone.call()

result = my_phone.send_sms(23434534, 'Missy, I missed to miss you')
print(result)