from bank import *
from tkinter import *
ob1 = Bank()
window = Tk()
window.geometry('800x500')
window.title("Bank displayment")
lb1_user = Label(window,text='Username',font = ('ariel',15,'bold'))
lb1_user.place(x=50,y=50)
en1_user = Entry(window,font = ('ariel',15,'bold'))
en1_user.place(x=170,y=50)
lb1_password = Label(window,text='Password',font = ('ariel',15,'bold'))
lb1_password.place(x=50,y=106)
en1_password = Entry(window,font = ('ariel',15,'bold'),show='*')
en1_password.place(x=150+20,y=106)
lb1_amount = Label(window,text="Amount",font = ('ariel',15,'bold'))
lb1_amount.place(x = 420,y=50)
en1_amount = Entry(window,font = ('ariel',15,'bold'))
en1_amount.place(x = 530,y=50)
lb1_transfer = Label(window,text="Recipient",font = ('ariel',15,'bold'))
lb1_transfer.place(x = 420,y=100)
en1_transfer = Entry(window,font = ('ariel',15,'bold'))
en1_transfer.place(x = 530,y=100)
lb_display=Label(window,text="",font=("ariel",15,"bold"),borderwidth=2,relief="solid",width=60,height=8,bg="white")
lb_display.place(x=50,y=160)
def create():
    username = en1_user.get().title()
    password = en1_password.get()
    data = ob1.create_acct(username,password)
    print(data)
    lb_display.config(text=data)
btn1 = Button(window,text='Create account',font = ('ariel',15,'bold'),command = create)
btn1.place(x=50,y=400)
def balance():
    username = en1_user.get().title()
    password = en1_password.get()
    data2 = ob1.check_balance(username,password)
    print(data2)
    lb_display.config(text=data2)
btn2 = Button(window,text='Check balance',font = ('ariel',15,'bold'),command = balance)
btn2.place(x=250,y=400)
def deposit():
    username = en1_user.get().title()
    password = en1_password.get()
    amount = int(en1_amount.get())
    data3 = ob1.deposit_amount(username,password,amount)
    print(data3)
    lb_display.config(text=data3)
btn3 = Button(window,text='Deposit amount',font = ('ariel',15,'bold'),command = deposit)
btn3.place(x = 450,y=400)
def withdraw():
    username = en1_user.get().title()
    password = en1_password.get()
    amount = int(en1_amount.get())
    data4 = ob1.withdraw_amount(username,password,amount)
    print(data4)
    lb_display.config(text=data4)
btn4 = Button(window,text='Withdraw amount',font = ('ariel',15,'bold'),command=withdraw)
btn4.place(x=650,y=400)
def transfer():
    username = en1_user.get().title()
    password = en1_password.get()
    amount = int(en1_amount.get())
    transfer_person =en1_transfer.get().title()
    data5 = ob1.transfer_amount(username,password,amount,transfer_person)
    print(data5)
    lb_display.config(text=data5)
btn5 = Button(window,text='Transfer to 🤵',font = ('ariel',15,'bold'),command = transfer)
btn5.place(x=370,y=455)

window.mainloop()
