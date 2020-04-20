#Made By © Aryan Kashyap

import mysql.connector as sq
from os import system
from time import sleep
import smtplib
import random


def seats_inp():
    global sttic
    train=storage()
    s=sqcon.cursor()
    s.execute('select * from seats_trains')
    data=s.fetchall() 

    rj_A=data[0][2]
    rj_B=data[1][2]
    rj_E=data[2][2]
    smj_A=data[3][2]
    smj_B=data[4][2]
    smj_E=data[5][2]
    sht_A=data[6][2]
    sht_B=data[7][2]
    sht_E=data[8][2]
    
    global seat_inp
    
    seat_inp=int(input('Seats required:'))
    
    if train=='rj':
        if optn==1:
            rj_A=rj_A-seat_inp
            
            
            qu="update seats_trains SET quantity={} where train='{}' and category='{}'".format(rj_A,'RAJDHANI EXPRESS','CLASS A')
            s.execute(qu)
            sqcon.commit()
        if optn==2:
            rj_B=rj_B-seat_inp
            
            
            qu="update seats_trains SET quantity={} where train='{}' and category='{}'".format(rj_B,'RAJDHANI EXPRESS','BUSINESS')
            s.execute(qu)
            sqcon.commit()
        if optn==3:
            rj_E=rj_E-seat_inp
            
            
            qu="update seats_trains SET quantity={} where train='{}' and category='{}'".format(rj_E,'RAJDHANI EXPRESS','ECONOMY')
            s.execute(qu)
            sqcon.commit()
            
    
    
    if train=='smj':
        if optn==1:
            smj_A=smj_A-seat_inp
            
            
            qu="update seats_trains SET quantity={} where train='{}' and category='{}'".format(smj_A,'SAMJHAUTA EXPRESS','CLASS A')
            s.execute(qu)
            sqcon.commit()
        if optn==2:
            smj_B=smj_B-seat_inp
            
            
            qu="update seats_trains SET quantity={} where train='{}' and category='{}'".format(smj_B,'SAMJHAUTA EXPRESS','BUSINESS')
            s.execute(qu)
            sqcon.commit()
        if optn==3:
            smj_E=smj_E-seat_inp
            
            
            qu="update seats_trains SET quantity={} where train='{}' and category='{}'".format(smj_E,'SAMJHAUTA EXPRESS','ECONOMY')
            s.execute(qu)
            sqcon.commit()

    if train=='sht':
        if optn==1:
            sht_A=sht_A-seat_inp
            
            
            qu="update seats_trains SET quantity={} where train='{}' and category='{}'".format(sht_A,'SHATABDI EXPRESS','CLASS A')
            s.execute(qu)
            sqcon.commit()
        if optn==2:
            sht_B=sht_B-seat_inp
            
            
            qu="update seats_trains SET quantity={} where train='{}' and category='{}'".format(sht_B,'SHATABDI EXPRESS','BUSINESS')
            s.execute(qu)
            sqcon.commit()

        if optn==3:
            sht_E=sht_E-seat_inp
            
            
            qu="update seats_trains SET quantity={} where train='{}' and category='{}'".format(sht_E,'SHATABDI EXPRESS','ECONOMY')
            s.execute(qu)
            sqcon.commit()
    sttic=""
    for i in range(seat_inp):
        tc=ticketgenerator()
        sttic=sttic+tc+'\n'
    send_tickets()
    
def storage():
    global train
    if entr==1:
        train='rj'
    if entr==2:
        train='smj'
    if entr==3:
        train='sht'

    return train
def reservation():
    global entr
    a=2
    while a==2:
        system('cls')
        print('Select Your Railway Service')
        print('[1] Rajdhani Express')
        print('[2] Samjhauta Express')
        print('[3] Shatabdi Express')
        entr=int(input('Enter Your Choice:'))
        if entr in (1,2,3):
            train=storage()
            classes(train)
            break
        else:
            system('cls')
            system('color 04')
            print('INVALID INPUT..!!')
            i=input('Press Enter To Exit to Login Page..!')
            system('color 07')
            system('cls')
def login_page():
    
    global email
    global usernm
    usernm=input('Username:')
    passwrrd=input('Password:')
    s=sqcon.cursor()
    s.execute('select * from login_digirail')
    data=s.fetchall()
    rows=s.rowcount

    for i in range(rows):
        if data[i][1]==usernm:
            if data[i][2]==passwrrd:
                email=data[i][3]
                reservation()

                
            
def classes(train):
    a=2
    while a==2:
        system('cls')
        print('Select Your Class')
        print('[1] Class A')
        print('[2] Business Class')
        print('[3] Economy Class')
        entr2=int(input('Enter Your Choice:'))
        if entr2 in (1,2,3):
            seats(entr2,train)
            break
            
        else:
            system('cls')
            system('color 04')
            print('INVALID INPUT..!!')
            i=input('Press Enter To Try Again..!')
            system('color 07')
            system('cls')
def seats(optn1,train):
    s=sqcon.cursor()
    s.execute('select * from seats_trains')
    data=s.fetchall() 

    rj_A=data[0][2]
    rj_B=data[1][2]
    rj_E=data[2][2]
    smj_A=data[3][2]
    smj_B=data[4][2]
    smj_E=data[5][2]
    sht_A=data[6][2]
    sht_B=data[7][2]
    sht_E=data[8][2]
    global optn
    optn=optn1
    if train=='rj':
        if optn==1:
            print('Seats Availaible:',rj_A)
        if optn==2:
            print('Seats Availaible:',rj_B)
        if optn==3:
            print('Seats Availaible:',rj_E)
    
    
    if train=='smj':
        if optn==1:
            print('Seats Availaible:',smj_A)
        if optn==2:
            print('Seats Availaible:',smj_B)
        if optn==3:
            print('Seats Availaible:',smj_E)

    if train=='sht':
        if optn==1:
            print('Seats Availaible:',sht_A)
        if optn==2:
            print('Seats Availaible:',sht_B)
        if optn==3:
            print('Seats Availaible:',sht_E)

    seats_inp()


def ticketgenerator():
    train=storage()
    tic=random.randint(10000,99999)
    tic=str(tic)
    if train=='rj':
        if optn==1:
            ticket='RJ-AC-'+tic    
        if optn==2:
            ticket='RJ-BUS-'+tic
        if optn==3:
            ticket='RJ-ECO-'+tic
    
    
    if train=='smj':
        if optn==1:
            ticket='SMJ-AC-'+tic
        if optn==2:
            ticket='SMJ-BUS-'+tic
        if optn==3:
            ticket='SMJ-ECO-'+tic

    if train=='sht':
        if optn==1:
            ticket='SHT-AC-'+tic
        if optn==2:
            ticket='SHT-BUS-'+tic
        if optn==3:
            ticket='SHT-ECO-'+tic
    
    return ticket

def send_tickets():
    sttic_temp=sttic
    message='Hello '+usernm+',\nHere are your tickets\n'+sttic_temp
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    server.login('digirail2020@gmail.com','digirail123')
    server.sendmail('digirail2020@gmail.com',email,message)
    server.close()

def main_menu():
    a=2
    while a==2:
        system('cls')
        print('WELCOME TO DIGIRAIL')
        sleep(1)
        print('[1] Login')
        print('[2] Sign Up')
        print('[3] Quit')
        entry=int(input("Enter Your Choice here:"))
        if entry==1:
            login_page()
            f()
        if entry==2:
            sign_up()
            f()
        if entry==3:
            quit()
        
        else:
            system('cls')
            system('color 04')
            print('INVALID INPUT..!!')
            i=input('Press Enter To Retry..!')
            system('color 07')
            system('cls')

def sign_up():
    system("cls")
    print("Enter the required credentials to create your account")
    usernm_sign=input("Username:")
    emailid=input("E-mail:")
    phone=input("Phone:")
    
    passwrd_sign=input("Password:")
    confirmpss=input("Confirm Password:")
    if passwrd_sign==confirmpss:
        otp=send_otp(emailid)
        print("An OTP has been sent to",emailid)
        otp_in=input("Enter The OTP:")
        if otp==otp_in:
            write_in_db(usernm_sign,passwrd_sign,emailid,phone)
            print("Registered Successfully")
            i=input("Press enter to continue...")
            system("cls")
            login_page()
        else:
    
            system('color 04')
            print('INVALID INPUT..!!')
            i=input('Press Enter To Retry..!')
            system('color 07')
            system('cls')

def send_otp(emailid):
    x=random.randint(1000,9999) 
    message="Hello There,\n"+"Your OTP is "+str(x)
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    server.login('digirail2020@gmail.com','digirail123')
    server.sendmail('digirail2020@gmail.com',emailid,message)
    server.close()          
    return str(x)

def write_in_db(un,ps,em,ph):
    
    g=sqcon.cursor()
    g.execute("select * from login_digirail")
    data=g.fetchall()
    sno=g.rowcount
    q="insert into login_digirail values({},'{}','{}','{}','{}')".format(sno,un,ps,em,ph)
    
    g.execute(q)
    sqcon.commit()

def staff_menu():
    print("Welcome to the Digirail's staff portal")
    user_staff=input("Username:")
    pswd_staff=input("Password:")
    s=sqcon.cursor()
    s.execute('select * from staff_digirail')
    data=s.fetchall()
    rows=s.rowcount

    for i in range(rows):
        if data[i][1]==user_staff:
            if data[i][2]==pswd_staff:
                staff_main()
                break
def f():
    print("Thank You For using DigiRail.")
    i=input("Press enter to quit..")
    quit()
def staff_main():
    s=sqcon.cursor()
    s.execute('select * from seats_trains')
    data=s.fetchall() 

    rj_A=data[0][2]
    rj_B=data[1][2]
    rj_E=data[2][2]
    smj_A=data[3][2]
    smj_B=data[4][2]
    smj_E=data[5][2]
    sht_A=data[6][2]
    sht_B=data[7][2]
    sht_E=data[8][2]

    system("cls")
    print("Logged in successfully")
    print("Seats Updation Below:-")
    print("Choose a train")
    print("\t[1] Rajdhani Express")
    print("\t[2] Samjhauta Express")
    print("\t[3] Shatabdi Express")    
    tr=int(input("Enter your choice:"))
    sleep(1)
    system("cls")
    print("Choose your Class:-")
    print("\t[1] Class A")
    print("\t[2] Business")
    print("\t[3] Economy")
    cl=int(input("Enter your choice:"))

    qty=int(input("Enter the number of seats to be added:"))

    if tr==1:
        if cl==1:
            rj_A=rj_A+qty
            
            
            qu="update seats_trains SET quantity={} where train='{}' and category='{}'".format(rj_A,'RAJDHANI EXPRESS','CLASS A')
            s.execute(qu)
            sqcon.commit()
        if cl==2:
            rj_B=rj_B+qty
            
            
            qu="update seats_trains SET quantity={} where train='{}' and category='{}'".format(rj_B,'RAJDHANI EXPRESS','BUSINESS')
            s.execute(qu)
            sqcon.commit()
        if cl==3:
            rj_E=rj_E+qty
            
            
            qu="update seats_trains SET quantity={} where train='{}' and category='{}'".format(rj_E,'RAJDHANI EXPRESS','ECONOMY')
            s.execute(qu)
            sqcon.commit()
            
    
    
    if tr==2:
        if cl==1:
            smj_A=smj_A+qty
            
            
            qu="update seats_trains SET quantity={} where train='{}' and category='{}'".format(smj_A,'SAMJHAUTA EXPRESS','CLASS A')
            s.execute(qu)
            sqcon.commit()
        if cl==2:
            smj_B=smj_B+qty
            
            
            qu="update seats_trains SET quantity={} where train='{}' and category='{}'".format(smj_B,'SAMJHAUTA EXPRESS','BUSINESS')
            s.execute(qu)
            sqcon.commit()
        if cl==3:
            smj_E=smj_E+qty
            
            
            qu="update seats_trains SET quantity={} where train='{}' and category='{}'".format(smj_E,'SAMJHAUTA EXPRESS','ECONOMY')
            s.execute(qu)
            sqcon.commit()

    if tr==3:
        if cl==1:
            sht_A=sht_A+qty
            
            
            qu="update seats_trains SET quantity={} where train='{}' and category='{}'".format(sht_A,'SHATABDI EXPRESS','CLASS A')
            s.execute(qu)
            sqcon.commit()
        if cl==2:
            sht_B=sht_B+qty
            
            
            qu="update seats_trains SET quantity={} where train='{}' and category='{}'".format(sht_B,'SHATABDI EXPRESS','BUSINESS')
            s.execute(qu)
            sqcon.commit()

        if cl==3:
            sht_E=sht_E+qty
            
            
            qu="update seats_trains SET quantity={} where train='{}' and category='{}'".format(sht_E,'SHATABDI EXPRESS','ECONOMY')
            s.execute(qu)
            sqcon.commit()
    print("Command successfully executed") 
    f() 
            

#main
sqcon=sq.connect(host='localhost',user='YourUsername',passwd='YourPassword',database='DigiRail')
if sqcon.is_connected():
    system('cls')
    print('Connecting To Server.')
    sleep(1)
    system('cls')
    print('Connecting To Server..')
    sleep(1)
    system('cls')
    print('Connecting To Server...')
    sleep(2)
    system('cls')
    system('color 02')
    print('Connected To Server Successfully!')
    sleep(1)
    system('color 07')
    i=input('Press Enter to continue...')
    system('cls')
else:
    print("Can't establish a secure connection, please check the path of the database..!!")

a=2
while a==2:
    system('cls')
    print('WELCOME TO DIGIRAIL')
    sleep(1)
    print('[1] Customer')
    print('[2] Staff')
    print('[3] Quit')
    entry=int(input("Enter Your Choice here:"))
    if entry==1:
        main_menu()
    if entry==2:
        staff_menu()
    if entry==3:
        quit()
    else:
        system('cls')
        system('color 04')
        print('INVALID INPUT..!!')
        i=input('Press Enter To Retry..!')
        system('color 07')
        system('cls')
sqcon.close()        
i=input()