# For chat bot we need to import chatterbot library and tkinter library of python 
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import tkinter as tk
from tkinter import *
bot= ChatBot("My Bot")
conversation=['Hello','Hi',
              'what is your name?','My name is kishor .',
              'Where are  from?','I am from Dharan.',
              'What are you?','I am a bot created Thagunna',
              'Are you having a good day?','Oh great! how about u?',
              'When did you arrive at the office?','Its about 15 minutes ago.'
              'Have you seen my email?','Oh ! I will check it very soon',]
trainer =ListTrainer(bot)
trainer.train(conversation)
# (print("Talk with bot")
# while True
#   query = input()      
#   if query=='exit':
#     break
#   answer=bot.get_response(query)
#   print('bot :' ,answer)
# ans=bot.get_response("what is your name?")
# print(ans))

# creating GUI
from tkinter import *
main= Tk()
main.geometry("500x700")
main.title("My bot !!")
img=PhotoImage(file='ew.png')
photo=Label(main,image=img)
photo.pack(pady=0)
def ask ():
    query=text.get()
    answer_from_bot=bot.get_response(query)
    msg.insert(END,"You :" +query)
    msg.insert(END,"Bot :"+str(answer_from_bot))
    text.delete(0,END)
frame=Frame(main)
sc=Scrollbar(frame)
msg=Listbox(frame,width=80,height=15)
sc.pack(side=RIGHT,fill=Y)
msg.pack(side=LEFT,fill=BOTH,pady=10)
frame.pack()
# creating text field
text=Entry(main,font=('Verdana',18))
text.pack(fill=X,pady=10)
btn=Button(main,text="Ask from bot",font=("Verdana",18),command=ask)
btn.pack()
main.mainloop()