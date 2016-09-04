import os
import sys
import random
import tkinter
from tkinter import *
import tkinter.messagebox
import smtplib
from smtplib import *
import sys
from imp import reload





try:
    input = raw_input
except NameError:
    pass

############################################################

'''subject=input("What would you like to say?  \n")
print("")
recipient=input("Who would you like to send that to?  \n")
print("")'''




root = Tk()



string = '''
   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _   _
  / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \
 ( C ) o ) n ) g ) r ) a ) t ) u ) l ) a ) t ) i ) o ) n ) s )   )   )
  \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/

\n
\n  
'''






def leftClick():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("neounknown455@gmail.com", "Al455drank2002")
 
    msg = string + noteEntry.get()
    recipient = nameEntry.get()
    server.sendmail("neounknown455@gmail.com", recipient, msg)
    server.quit()






topFrame = Frame(root, bg="green")
topFrame.pack()

middleFrame = Frame(root, bg="green")
middleFrame.pack()

bottomFrame = Frame(root, bg="green")
bottomFrame.pack()

#type your msg below
newNote = Label(topFrame, text="EᗰᗩIᒪ ᗷOᗪY  \n", width=60, fg="blue", bg="orange")
newNote.grid(row=0)
#actual msg
noteEntry = Entry(topFrame, width=30, bg="grey", fg="blue")
noteEntry.grid(rowspan=2)
#recipient?
name = Label(middleFrame, text="ᖇEᑕIᑭIEᑎT  \n ", width=60, fg="blue", bg="orange")
name.grid(row=0)
#enter your recipient email below
nameEntry = Entry(middleFrame, width=30, bg="grey", fg="blue")
nameEntry.grid(row=1)


link = Button(bottomFrame, text="Send", command=leftClick, bg="blue", fg="green")
link.pack(side=LEFT)







root.mainloop()


#################################################################################











