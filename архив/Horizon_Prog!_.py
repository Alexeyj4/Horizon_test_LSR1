#!/usr/bin/python
#coding=utf8


import rpErrorHandler
from Tkinter import *
#------------------------------------------------------------------------------#
#                                                                              #
#                                 Horizon_Prog                                 #
#                                                                              #
#------------------------------------------------------------------------------#
class Horizon_Prog(Frame):
    def __init__(self,Master=None,*pos,**kw):
        #
        #Your code here
        #    

        apply(Frame.__init__,(self,Master),kw)
        self.entry_first_num = StringVar()
        self.entry_last_num = StringVar()
        self.serial_number = StringVar()
        self.text_to_send = StringVar()
        self.text_to_send2 = StringVar()
        self._Frame2 = Frame(self)
        self._Frame2.pack(fill='y',side='left')
        self._Frame4 = Frame(self,background='#dbdbdb')
        self._Frame4.pack(fill='y',side='left')
        self._Frame3 = Frame(self)
        self._Frame3.pack(side='left')
        self._Frame27 = Frame(self._Frame2)
        self._Frame27.pack(side='top')
        self._Label1 = Label(self._Frame27,text='Выберете кассету')
        self._Label1.pack(side='top')
        self._CassList = Listbox(self._Frame27,selectmode='single')
        self._CassList.pack(side='top')
        self._SSH_connect = Button(self._Frame27
            ,command=self._on__SSH_connect_command,text='Подключиться')
        self._SSH_connect.pack(side='bottom')
        self._Frame6 = Frame(self._Frame2)
        self._Frame6.pack(side='top')
        self._Label2 = Label(self._Frame6,text='MAC ЛСР1:')
        self._Label2.pack(side='right')
        self._Frame5 = Frame(self._Frame2)
        self._Frame5.pack(side='top')
        self._Frame1 = Frame(self._Frame2)
        self._Frame1.pack(fill='x',side='top')
        self._dev_add = Button(self._Frame1,command=self._on__dev_add
            ,state='disabled',text='Этап 1 dev add')
        self._dev_add.pack(fill='x',side='top')
        self._pos_tst = Button(self._Frame1,command=self._on__pos_tst_command
            ,text='Этап 2 pos tst')
        self._pos_tst.pack(fill='x',side='top')
        self._dev_remove = Button(self._Frame1
            ,command=self._on__dev_remove_command,state='disabled'
            ,text='Этап 3 dev remove')
        self._dev_remove.pack(fill='x',side='top')
        self._Frame29 = Frame(self._Frame4)
        self._Frame29.pack(side='top')
        self._Label4 = Label(self._Frame29,text='Введите команду для отправки:')
        self._Label4.pack(side='bottom')
        self._Frame19 = Frame(self._Frame4)
        self._Frame19.pack(side='top')
        self._Frame14 = Frame(self._Frame4)
        self._Frame14.pack(side='top')
        self._label_Rcvd_Text = Label(self._Frame14,text='Принято:')
        self._label_Rcvd_Text.pack(side='top')
        self._ReceivedText = Text(self._Frame14
            ,font=('@Arial Unicode MS', 10, 'bold'),height='35')
        self._ReceivedText.pack(side='top')
        self._Frame9 = Frame(self._Frame4)
        self._Frame9.pack(fill='x',side='top')
        self._Label3 = Label(self._Frame9,text='Первый номер')
        self._Label3.pack(side='left')
        self._first_num = Entry(self._Frame9,textvariable=self.entry_first_num)
        self._first_num.pack(side='left')
        self._Label5 = Label(self._Frame9,text='Последний номер')
        self._Label5.pack(side='left')
        self._last_num = Entry(self._Frame9,textvariable=self.entry_last_num)
        self._last_num.pack(side='left')
        self._dev_remove_list = Button(self._Frame9
            ,command=self._on__dev_remove_list_command,state='disabled'
            ,text='dev remove')
        self._dev_remove_list.pack(anchor='w',side='left')
        self._Frame8 = Frame(self._Frame5)
        self._Frame8.pack(side='left')
        self._serialnumber = Entry(self._Frame8,textvariable=self.serial_number)
        self._serialnumber.pack(side='right')
        self._Frame7 = Frame(self._Frame5)
        self._Frame7.pack(side='left')
        self._increment = Button(self._Frame7
            ,command=self._on__increment_command,state='disabled',text='"+1"')
        self._increment.pack(side='left')
        self._Frame31 = Frame(self._Frame19)
        self._Frame31.pack(expand='yes',fill='x',side='left')
        self._text_to_send = Entry(self._Frame31,textvariable=self.text_to_send)
        self._text_to_send.pack(side='top')
        self._send = Button(self._Frame31,command=self._on__send_command
            ,state='disabled',text='Отправить на устройство команду')
        self._send.pack(fill='x',side='top')
        self._Frame30 = Frame(self._Frame19)
        self._Frame30.pack(expand='yes',fill='x',side='left')
        self._text_to_send2 = Entry(self._Frame30
            ,textvariable=self.text_to_send2)
        self._text_to_send2.pack(side='top')
        self._send2 = Button(self._Frame30,command=self._on__send2_command
            ,state='disabled',text='Отправить на устройство команду')
        self._send2.pack(side='top')
        #
        #Your code here
        #
        
        self._CassList.insert(0, "10.0.0.7")
        self._CassList.selection_set(0)
        

        self.serial_number.set('20453')
        self.entry_first_num.set('20501')
        self.entry_last_num.set('20510')

        self.text_to_send.set(str("list"))
        self.text_to_send2.set(str("dev list"))
        


  
        
    #
    #Start of event handler methods
    #


    def _on__SSH_connect_command(self,Event=None):
        global connected
        global client
        global ssh
        
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(hostname=self._CassList.get(self._CassList.curselection()), username='root', password='talnakh', port=22)
            ssh= client.invoke_shell()
         
            
            connected=1
            
            
            self._SSH_connect.config(state='disabled')
            self._send.config(state="normal")
            self._send2.config(state="normal")
            self._dev_add.config(state="normal")
            self._pos_tst.config(state="normal")
            self._dev_remove.config(state="normal")
            self._dev_remove_list.config(state="normal")
            self._increment.config(state="normal")
            
        except:            
            connected=0
            mbox.showerror("Ошибка", "Не удалось подключиться к кассете")  
     

    def _on__dev_add(self,Event=None):
        sshsend('dev add '+ self.serial_number.get() + ' ' + last_octet_ip())
        

    def _on__dev_remove_command(self,Event=None):
        sshsend('dev rm '+self.serial_number.get())

    def _on__dev_remove_list_command(self,Event=None):
        for i in range(int(self.entry_first_num.get()),int(self.entry_last_num.get())+1):
            sshsend('dev rm '+str(i))

    def _on__increment_command(self,Event=None):
        self.serial_number.set(int(self.serial_number.get())+1)

    def _on__pos_tst_command(self,Event=None):

              os.system('start cmd /K C:/horizon_test/lsr1_test/pos_tst.exe 10.0.3.'+last_octet_ip()+' '+self.serial_number.get())



          

    def _on__send2_command(self,Event=None):
            sshsend(self._text_to_send2.get())

    def _on__send_command(self,Event=None):      
            sshsend(self._text_to_send.get())

        

    #
    #Start of non-Rapyd user code
    #


pass #---end-of-form---

connected=0

    
    
def loopproc():             
 #    read_and_print(0)
 #    setup_ip_mac_etc() 
     Root.after(COMtimeout,loopproc) 


    

def sshsend(s):
        ssh.send(s)
        ssh.send('\n') 
        time.sleep(0.5)        
        App._ReceivedText.insert('1.0', ssh.recv(16384))
        
def last_octet_ip():
        n=str(App.serial_number.get())[-2:]
        if n=='01':
            n='101'
        return n
 


try:
    #--------------------------------------------------------------------------#
    # User code should go after this comment so it is inside the "try".        #
    #     This allows rpErrorHandler to gain control on an error so it         #
    #     can properly display a Rapyd-aware error message.                    #
    #--------------------------------------------------------------------------#

    #Adjust sys.path so we can find other modules of this project
   
   

    
    
    
    if '.' not in sys.path:
        sys.path.append('.')
    #Put lines to import other modules of this project here
 
    import subprocess
    import os
    import shlex
    import sys
    import paramiko    
    import serial
    import msvcrt
    import time
    import math
    import tkMessageBox as mbox
 
 
    
    if __name__ == '__main__':

        Root = Tk()
        import Tkinter
        Tkinter.CallWrapper = rpErrorHandler.CallWrapper
        del Tkinter
        App = Horizon_Prog(Root)
        App.pack(expand='yes',fill='both')

        Root.geometry('800x750+10+10')
        Root.title('Horizon test')

        


        
        Root.mainloop()
    #--------------------------------------------------------------------------#
    # User code should go above this comment.                                  #
    #--------------------------------------------------------------------------#
except:
    rpErrorHandler.RunError()