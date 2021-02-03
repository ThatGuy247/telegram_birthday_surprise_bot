# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 20:31:21 2020

@author: arman
"""

from telegram.ext import Updater, CommandHandler , MessageHandler , Filters
from random import randint
import tkinter as kin

######### Bot Configurations ########
def config(token , txt , img):
    ''' Bot Config '''
    updater = Updater(token=token , use_context=True)
    dispatcher = updater.dispatcher
    
    def start(update, context):
        '''Greets the user'''
        context.bot.send_message(chat_id=update.message.chat_id, text='Welcome!')
        context.bot.send_message(chat_id=update.message.chat_id, text='Send me a 2-digit number and see what happens!')
        
        
    def main(update, context):
        if int(update.message.text) < 20:
            num = 20
            context.bot.send_message(chat_id=update.message.chat_id, 
                                     text='Thats a small number, I\'ll raise it myself')
        else:
            num = int(update.message.text)
            
        for i in range(num):
            a = randint(0, 3)
            context.bot.send_message(chat_id=update.message.chat_id, text=txt) # sends deisred text
            if a not in [1,2]:
                context.bot.send_photo(chat_id=update.message.chat_id, photo=img) # sends desired image
    
    start_handler = CommandHandler('start', start)
    message_handler = MessageHandler(Filters.text, main)
    
    
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(message_handler)

    updater.start_polling()
    
######### GUI Setup ########
    
root = kin.Tk()   
root.title('HBD Bot Config') 
root.geometry('260x170')
root.resizable(width=False,height=False)
root.configure(bg='#9C27B0')


frame1 = kin.Frame(root, width=300 , height=126, bg='#9C27B0' )
frame1.pack(side=kin.TOP)

frame2 = kin.Frame(root, width=300 , height=126, bg='#9C27B0')
frame2.pack(side=kin.TOP)

frame3 = kin.Frame(root, width=300 , height=126, bg='#9C27B0')
frame3.pack(side=kin.TOP)

frame4 = kin.Frame(root, width=300 , height=21, bg='#9C27B0')
frame4.pack(side=kin.TOP)

label1 = kin.Label(frame1, text='Token:     ' , bg='#9C27B0' , fg='#FFFFFF')
label1.pack(side=kin.LEFT, pady=10 , padx=5)

entry1 = kin.Entry(frame1 , textvariable='ex: 1430669907:AAYjBIqvZQRNwrGG3XVRg7mQh2kOmYREslg')
entry1.pack(side=kin.LEFT, pady=10, padx=5)

label2 = kin.Label(frame2, text='HBD Text: ', bg='#9C27B0', fg='#FFFFFF')
label2.pack(side=kin.LEFT, pady=10, padx=5)

entry2 = kin.Entry(frame2, textvariable='ex: Happy Birthday Anna!')
entry2.pack(side=kin.LEFT, pady=10, padx=5)


label3 = kin.Label(frame3, text='Img Link: ', bg='#9C27B0', fg='#FFFFFF')
label3.pack(side=kin.LEFT, pady=10, padx=5)

entry3 = kin.Entry(frame3, textvariable='ex: http://abc.com/abc.jpg')
entry3.pack(side=kin.LEFT, pady=10, padx=5)

######### Main Function ########

def func():
    ''' This is the main function that calls the bot function'''

    tkk ='1111111111:102030ADGFSGJJ' # put your token here
    txtt ='تولدت مبارک دوست من!'
    imgg ='http://www.coca.ir/wp-content/uploads/2020/11/%D9%85%D8%AA%D9%86-%D8%AA%D8%A8%D8%B1%DB%8C%DA%A9-%D8%AA%D9%88%D9%84%D8%AF%D8%AA-%D9%85%D8%A8%D8%A7%D8%B1%DA%A9.jpg'
    o1 = entry1.get()
    o2 = entry2.get()
    o3 = entry3.get()
    if o1:
        tkk = entry1.get()
    if o2:
        txtt = entry2.get()
    if o3:
        imgg = entry3.get()
       
    config(tkk,txtt,imgg) # calls the bot function
    
    label4 = kin.Label(frame4, text='Done!' , bg='#9C27B0' , fg='#FFFFFF')
    label4.pack(side=kin.LEFT, pady=10, padx=5)

######### Start Button ########

button= kin.Button(frame4, text='Run'  , bg='#FFFFFF' , command= lambda: func())
button.pack(side=kin.LEFT, pady=10, padx=5)


root.mainloop()






























