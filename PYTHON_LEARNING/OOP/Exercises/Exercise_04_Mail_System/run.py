from mail_manager import MailManager
from company import Company

hawaii_hotel = Company('Hawaii Hotel', 'hawaii_hotel@gmail.com')
hawaii_hotel_mail_manager = MailManager(hawaii_hotel.name, hawaii_hotel.mail)

while True:
   
    title = input("\nWrite the mail's title: ")
    body = input("Write the mail's body: ")

    hawaii_hotel_mail_manager.create_mail(title, body)

    adressee_name = input("Write the adressee's name: ")
    adressee_mail = input("Write the adressee's mail: ")

    hawaii_hotel_mail_manager.set_adressee(adressee_name, adressee_mail)

    while True:

        question_1 = input("\nDo you want to add another adressee? Write [Y]es or [N]o.\n").lower()

        if question_1 == 'yes' or question_1 == 'y':
            adressee_name = input("Write the adressee's name: ")
            adressee_mail = input("Write the adressee's mail: ")

            hawaii_hotel_mail_manager.set_adressee(adressee_name, adressee_mail)
        elif question_1 == 'no' or question_1 == 'n':
            break
        else:
            print("Invalid option. Write [Y]es or [N]o.")
    
    hawaii_hotel_mail_manager.send_mail()

    while True:
        question_2 = input("Do you want to send another mail? Write [Y]es or [N]o.\n").lower()

        if question_2 == 'yes' or question_2 == 'y':
            break
        elif question_2 == 'no' or question_2 == 'n':
            break
        else:
            print("Invalid option. Write [Y]es or [N]o.\n")
   
    if question_2 == 'no' or question_2 == 'n':
        break