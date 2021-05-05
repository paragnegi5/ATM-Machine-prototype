
import cv2
from random import randint
from getpass import getpass
from time import sleep
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
members={}



#email sending function
def email_to_send(to_address,text_to_send,subject_of_mail,img=None):

    
    from_addr=#"Enter your own email id"
    to_addr=to_address
    

    username = #'Enter your email'
    password = #"Enter yout email password and turn on access for less secure app access"
    
    msg = MIMEMultipart()

    msg['From'] = 'parag.negi001@gmail.com'
    msg['To'] = to_address
    msg['Subject'] = subject_of_mail
    html = "<html><head></head><body>"+text_to_send+"</body></html>"
    msg.attach(MIMEText(html, 'html'))

    if img!=None:
        fp = open(img, 'rb')
        msgImage = MIMEImage(fp.read())
        fp.close()
        msgImage.add_header('Content-ID', '<image1>')
        msg.attach(msgImage)
    
    
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(username,password)
    server.sendmail(from_addr,to_addr,msg.as_string())
    server.quit()


# openacc()
def openacc():
    print("Welcome\n")
    name=input("Please enter your name: ").upper()
    pin=getpass("Please enter a 4 digit PIN: ")
    email=input("Please enter your email id: ")
    account_number="5"
    i=0
    #same account number check
    while i<10:
        account_number += str(randint(0,9))
        i=i+1
    members[account_number]=[]
    members[account_number].append(name)
    members[account_number].append(pin)
    members[account_number].append(email)
    print("Your new account number is: "+account_number)
    deposit_money=input("Do you want to deposit money in your account (Yes/No): ").upper()
    to=email
    text="Hi..<br></br><br></br>Mr. <b>{}</b>.<br></br><br></br>Congratulations! Thank you for trusting us.<br></br><br></br>Your new account has been created with acccount number {}<br></br><br></br>Wish you a great BANKING ahead.".format(name,account_number)
    subject="New account opened"
    email_to_send(to,text,subject)
    if deposit_money=="YES":
        deposit=input("Please enter the amount you would like to deposit: ")
        members[account_number].append(deposit)
        subject="Transaction Alert"
        text="<b>Mr. {}</b> your account <b>{}</b> has been credited with <b>Rs.{}</b>.".format(name,account_number,deposit)
        email_to_send(to,text,subject)
        j=input("Press 0 for menu and 1 to exit: ")
        if int(j)==0:
            welcome_function()
        elif int(j)==1:
            exit_menu()
        else:
            print("Invalid option. Thank you for banking with us.")
    elif deposit_money=="NO":
        members[account_number].append('0')
        j=input("Press 0 for menu and 1 to exit: ")
        if int(j)==0:
            welcome_function()
        elif int(j)==1:
            exit_menu()
        else:
            print("Invalid option. Thank you for banking with us.")



#money withdrawn email function
# withdraw_money()
def withdraw_money():
    account_number=input("Please enter your account number: ")
    if account_number in members.keys():
        print("Welcome "+members[account_number][0])
        pin=getpass("Please enter you PIN: ")
        if pin==members[account_number][1]:
            money=input("Please enter the amount you want to withdraw: ")
            if int(money)>int(members[account_number][3]):
                print("Insufficient funds")
            else:
                print("Money withdrawn: "+money)
                print("Available balance: "+str(int(members[account_number][3])-int(money)))
                members[account_number][3]=str(int(members[account_number][3])-int(money))
                subject="Transaction Alert"
                text="<b>Mr. {}</b> your account <b>{}</b> has been debited with <b>Rs.{}</b>. Available balance is <b>Rs.{}</b>.".format(members[account_number][0],account_number,money,members[account_number][3])
                to=members[account_number][2]
                email_to_send(to,text,subject)
                j=input("Press 0 for menu and 1 to exit: ")
                if int(j)==0:
                    welcome_function()
                elif int(j)==1:
                    exit_menu()
                else:
                    print("Invalid option. Thank you for banking with us.")
        else:
            print("Invalid PIN")
            to=members[account_number][2]
            subject="Unknown Access"
            text="Someone is trying to access your account"
            email_to_send(to,text,subject,img_name)
    else:
        print("Invalid account number")
        j=input("Press 0 for menu and 1 to exit: ")
        if int(j)==0:
            welcome_function()
        elif int(j)==1:
            exit_menu()
        else:
            print("Invalid option. Thank you for banking with us.")


# deposit_money()
def deposit_money():
    account_number=input("Please enter your account number: ")
    if account_number in members.keys():
        print("Welcome "+members[account_number][0])
        pin=getpass("Please enter you PIN: ")
        if pin==members[account_number][1]:
            money=input("Please enter the amount you would like to deposit: ")
            print("Money deposited: "+money)
            print("Available balance: "+str(int(members[account_number][3])+int(money)))
            members[account_number][3]=str(int(members[account_number][3])+int(money))
            subject="Transaction Alert"
            text="<b>Mr. {}</b> your account <b>{}</b> has been credited with <b>Rs.{}</b>. Available balance is <b>Rs.{}</b>.".format(members[account_number][0],account_number,money,members[account_number][3])
            to=members[account_number][2]
            email_to_send(to,text,subject)
            j=input("Press 0 for menu and 1 to exit: ")
            if int(j)==0:
                welcome_function()
            elif int(j)==1:
                exit_menu()
            else:
                print("Invalid option. Thank you for banking with us.")
            
        else:
            print("Invalid PIN")
            to=members[account_number][2]
            subject="Unknown Access"
            text="Someone is trying to access your account"
            email_to_send(to,text,subject,img_name)
    else:
        print("Invalid account number")
        j=input("Press 0 for menu and 1 to exit: ")
        if int(j)==0:
            welcome_function()
        elif int(j)==1:
            exit_menu()
        else:
            print("Invalid option. Thank you for banking with us.")




# check_balance()
def check_balance():
    account_number=input("Please enter your account number: ")
    if account_number in members.keys():
        print("Welcome "+members[account_number][0])
        pin=getpass("Please enter you PIN: ")
        if pin==members[account_number][1]:
            print("Available balance: "+members[account_number][3])
            j=input("Press 0 for menu and 1 to exit: ")
            if int(j)==0:
                welcome_function()
            elif int(j)==1:
                exit_menu()
            else:
                print("Invalid option. Thank you for banking with us.")
        else:
            print("Invalid PIN")
            image_save(image_recorder)
            to=members[account_number][2]
            subject="Unknown Access"
            text="Someone is trying to access your account"
            email_to_send(to,text,subject,img_name)
    else:
        print("Invalid account number")
        j=input("Press 0 for menu and 1 to exit: ")
        if int(j)==0:
            welcome_function()
        elif int(j)==1:
            exit_menu()
        else:
            print("Invalid option. Thank you for banking with us.")




# pin_change()
def pin_change():
    account_number=input("Please enter your account number: ")
    if account_number in members.keys():
        print("Welcome "+members[account_number][0])
        pin=getpass("Please enter you PIN: ")
        if pin==members[account_number][1]:
            OTP=""
            i=0
            while i<5:
                OTP += str(randint(0,9))
                i=i+1
            to=members[account_number][2]
            text="OTP for changing your PIN is <b>{}</b>.".format(OTP)
            subject="PIN Change Request"
            email_to_send(to,text,subject)
            otpsent=input("OTP has been sent on your email. Please enter the OTP: ")
            k=0
            while(k<3):
                if otpsent==OTP:
                    newpin=input("Please enter the new PIN: ")
                    members[account_number][1]=newpin
                    subject="PIN Changed"
                    text="<b>Mr. {}</b> PIN for your account <b>{}</b> has been changed sucessfully.".format(members[account_number][0],account_number)
                    to=members[account_number][2]
                    email_to_send(to,text,subject)
                    print("Your PIN had been changed successfully.")
                    break
                elif k==2:
                    print("You have entered an incorrect OTP three times.Please try again.")
                    break
                else:
                    otpsent=input("You have entered an incorrect OTP. Please try again: ")
                    k=k+1
                    continue
            j=input("Press 0 for menu and 1 to exit: ")
            if int(j)==0:
                welcome_function()
            elif int(j)==1:
                exit_menu()
            else:
                print("Invalid option. Thank you for banking with us.")
                    
        else:
            print("Invalid PIN")
            to=members[account_number][2]
            subject="Unknown Access"
            text="Someone is trying to access your account"
            email_to_send(to,text,subject,img_name)
    else:
        print("Invalid account number")
        j=input("Press 0 for menu and 1 to exit: ")
        if int(j)==0:
            welcome_function()
        elif int(j)==1:
            exit_menu()
        else:
            print("Invalid option. Thank you for banking with us.")



#exit menu
def exit_menu():
    print("Thank you for banking with us.")



def welcome_function():
    print("Welcome to your bank\n")
    i=input("Please choose from the following options:- \n1.)Open New Account \n2.)Withdraw money\n3.)Deposit money\n4.)Check balance\n5.)PIN change\n6.)Exit\n\n")
    if int(i)==1:
        openacc()
    elif int(i)==2:
        withdraw_money()
    elif int(i)==3:
        deposit_money()
    elif int(i)==4:
        check_balance()
    elif int(i)==5:
        pin_change()
    elif int(i)==6:
        exit_menu()
    else:
        print("Invalid Option")



cam = cv2.VideoCapture(0)
cv2.namedWindow("test")


ret, frame = cam.read()
cv2.imshow("test", frame)
img_name = "test.png"
cv2.imwrite(img_name, frame)

cam.release()

cv2.destroyAllWindows()
sleep(3)

welcome_function()