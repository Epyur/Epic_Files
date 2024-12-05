import re

def send_email(recepient, message, sender = 'university.help@gmail.com'):
    dog = "@"
    domen_1 = '.ru'
    domen_2 = '.com'
    domen_3 = '.net'
    if dog in recepient:
        if dog in sender:
            if domen_1 in recepient or domen_2 in recepient or domen_3 in recepient:
                if domen_1 in sender or domen_2 in sender or domen_3 in sender:
                    if recepient == sender:
                        print('Нельзя отправить письмо самому себе!')
                    elif sender == 'university.help@gmail.com':
                        print('Письмо успешно отправлено с адреса ', sender, 'на адрес', recepient)
                else:
                    print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса ', sender, 'на адрес ', recepient)
            else:
                print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса ', sender, 'на адрес ', recepient)
        else:
            print('Невозможно отправить письмо с адреса ', sender, 'на адрес', recepient)
    else:
        print('Невозможно отправить письмо с адреса ', sender, 'на адрес', recepient)



send_email('university.help@gmail.net', 'text')