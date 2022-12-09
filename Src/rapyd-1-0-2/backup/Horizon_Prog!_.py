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
        self.device = StringVar()
        self.ArrowKeysOn = IntVar()
        self.COM_port_index = StringVar()
        self.ataddr = StringVar()
        self.entry_at_addr = StringVar()
        self.entry_at_addr_exe = StringVar()
        self.entry_at_addr_rt = StringVar()
        self.ethipaddr = StringVar()
        self.ethmacaddr = StringVar()
        self.ifbw = IntVar()
        self.entry_ipaddr = StringVar()
        self.phyipaddr = StringVar()
        self.phymacaddr = StringVar()
        self.serial_number = StringVar()
        self.text_to_send = StringVar()
        self._Frame2 = Frame(self)
        self._Frame2.pack(fill='y',side='left')
        self._Frame4 = Frame(self,background='#dbdbdb')
        self._Frame4.pack(fill='y',side='left')
        self._Frame3 = Frame(self)
        self._Frame3.pack(side='left')
        self._Frame6 = Frame(self._Frame2)
        self._Frame6.pack(side='top')
        self._Label1 = Label(self._Frame6
            ,text='Введите номер COM-порта (см. диспетчер устройств):')
        self._Label1.pack(side='top')
        self._COM_port_index = Entry(self._Frame6
            ,textvariable=self.COM_port_index)
        self._COM_port_index.pack(side='top')
        self._COM_port_connect = Button(self._Frame6
            ,command=self._on__COM_port_connect_command,text='Открыть COM-порт')
        self._COM_port_connect.pack(side='top')
        self._Label3 = Label(self._Frame6,justify='left'
            ,text='Выберете устройство:')
        self._Label3.pack(side='top')
        self._MA41 = Radiobutton(self._Frame6,command=self._set_serial
            ,justify='left',text='Модуль МА-41',value='ma41'
            ,variable=self.device)
        self._MA41.pack(side='top')
        self._MA45 = Radiobutton(self._Frame6,command=self._set_serial
            ,justify='left',text='Модуль МА-45',value='ma45'
            ,variable=self.device)
        self._MA45.pack(side='top')
        self._LSR4 = Radiobutton(self._Frame6,command=self._set_serial
            ,justify='left',text='Считыватель ЛС-Р4',value='lsr4'
            ,variable=self.device)
        self._LSR4.pack(side='top')
        self._LSE4 = Radiobutton(self._Frame6,command=self._set_serial
            ,justify='left',text='Считыватель ЛС-Е4',value='lse4'
            ,variable=self.device)
        self._LSE4.pack(side='top')
        self._1M500 = Radiobutton(self._Frame6,command=self._set_serial
            ,justify='left',text='Кассета 1-M-500',value='1m500'
            ,variable=self.device)
        self._1M500.pack(side='top')
        self._Label2 = Label(self._Frame6,text='Серийный номер:')
        self._Label2.pack(side='top')
        self._serialnumber = Entry(self._Frame6,textvariable=self.serial_number)
        self._serialnumber.pack(side='top')
        self._prog_and_increment = Button(self._Frame6
            ,command=self._on__prog_and_increment_command,state='disabled'
            ,text='Write to EEPROM ataddr, ipaddr, macaddr, ifbw and increment serial number (up key)')
        self._prog_and_increment.pack(side='top')
        self._Label9 = Label(self._Frame6,text='at addr')
        self._Label9.pack(side='top')
        self._ataddr = Entry(self._Frame6,state='disabled'
            ,textvariable=self.ataddr)
        self._ataddr.pack(side='top')
        self._Label5 = Label(self._Frame6,text='phy ipaddr:')
        self._Label5.pack(side='top')
        self._phyipaddr = Entry(self._Frame6,state='disabled'
            ,textvariable=self.phyipaddr)
        self._phyipaddr.pack(side='top')
        self._Label6 = Label(self._Frame6,text='eth ipaddr:')
        self._Label6.pack(side='top')
        self._ethipaddr = Entry(self._Frame6,state='disabled'
            ,textvariable=self.ethipaddr)
        self._ethipaddr.pack(side='top')
        self._ethmacaddr = Entry(self._Frame6,state='disabled'
            ,textvariable=self.ethmacaddr)
        self._ethmacaddr.pack(side='bottom')
        self._Label8 = Label(self._Frame6,text='eth macaddr:')
        self._Label8.pack(side='bottom')
        self._phymacaddr = Entry(self._Frame6,state='disabled'
            ,textvariable=self.phymacaddr)
        self._phymacaddr.pack(side='bottom')
        self._Label7 = Label(self._Frame6,text='phy macaddr:')
        self._Label7.pack(side='bottom')
        self._Frame1 = Frame(self._Frame2)
        self._Frame1.pack(side='top')
        self._Label10 = Label(self._Frame1,text='at frequency trim:')
        self._Label10.pack(side='top')
        self._Frame10 = Frame(self._Frame2)
        self._Frame10.pack(side='top')
        self._Frame7 = Frame(self._Frame2)
        self._Frame7.pack(side='top')
        self._Frame14 = Frame(self._Frame4)
        self._Frame14.pack(side='top')
        self._ReceivedText = Text(self._Frame14)
        self._ReceivedText.pack(side='bottom')
        self._label_Rcvd_Text = Label(self._Frame14
            ,text='Принято от устройства:')
        self._label_Rcvd_Text.pack(side='bottom')
        self._send = Button(self._Frame14,command=self._on__send_command
            ,state='disabled',text='Отправить на устройство команду')
        self._send.pack(side='bottom')
        self._text_to_send = Entry(self._Frame14,textvariable=self.text_to_send)
        self._text_to_send.pack(side='bottom')
        self._Label4 = Label(self._Frame14,text='Введите команду для отправки:')
        self._Label4.pack(side='bottom')
        self._Frame9 = Frame(self._Frame4)
        self._Frame9.pack(fill='x',side='top')
        self._btn_ping = Button(self._Frame9,command=self._on__btn_ping_command
            ,state='disabled',text='ping')
        self._btn_ping.pack(side='left')
        self._ipaddr = Entry(self._Frame9,textvariable=self.entry_ipaddr)
        self._ipaddr.pack(side='left')
        self._Frame15 = Frame(self._Frame4)
        self._Frame15.pack(fill='x',side='top')
        self._btn_phyipaddr = Button(self._Frame15
            ,command=self._on__btn_phyipaddr_command,state='disabled'
            ,text='phy ipaddr')
        self._btn_phyipaddr.pack(anchor='w',side='left')
        self._btn_ataddr = Button(self._Frame15
            ,command=self._on__btn_ataddr_command,state='disabled'
            ,text='at addr')
        self._btn_ataddr.pack(side='left')
        self._Frame18 = Frame(self._Frame4)
        self._Frame18.pack(fill='x',side='top')
        self._btn_adf_tst = Button(self._Frame18
            ,command=self._on__btn_adf_tst_command,state='disabled'
            ,text='adf tst')
        self._btn_adf_tst.pack(anchor='w',side='left')
        self._btn_adf_tst_50 = Button(self._Frame18
            ,command=self._on__btn_adf_tst_50_command,state='disabled'
            ,text='adf tst 50')
        self._btn_adf_tst_50.pack(anchor='w',side='left')
        self._Frame19 = Frame(self._Frame4)
        self._Frame19.pack(fill='x',side='top')
        self._btn_dbg0 = Button(self._Frame19,command=self._on__btn_dbg0_command
            ,state='disabled',text='dbg 0')
        self._btn_dbg0.pack(anchor='w',side='left')
        self._btn_dbg1 = Button(self._Frame19,command=self._on__btn_dbg1_command
            ,state='disabled',text='dbg 1')
        self._btn_dbg1.pack(anchor='w',side='left')
        self._Frame16 = Frame(self._Frame4)
        self._Frame16.pack(fill='x',side='top')
        self._btn_at_dst_rt = Button(self._Frame16
            ,command=self._on__btn_at_dst_rt_command,state='disabled'
            ,text='at dst 0xXXXX + rt')
        self._btn_at_dst_rt.pack(anchor='w',side='left')
        self._entry_at_addr = Entry(self._Frame16
            ,textvariable=self.entry_at_addr)
        self._entry_at_addr.pack(side='left')
        self._Frame17 = Frame(self._Frame4)
        self._Frame17.pack(fill='x',side='top')
        self._Label11 = Label(self._Frame17,text='ЛС-Р4:')
        self._Label11.pack(side='left')
        self._entry_at_addr_exe = Entry(self._Frame17
            ,textvariable=self.entry_at_addr_exe)
        self._entry_at_addr_exe.pack(side='left')
        self._btn_exe_at_dst_rt = Button(self._Frame17
            ,command=self._on__btn_exe_at_dst_rt_command,state='disabled'
            ,text='exe 0xXXXX at dst 0xXXXX + rt')
        self._btn_exe_at_dst_rt.pack(side='left')
        self._Label12 = Label(self._Frame17,text='МА:')
        self._Label12.pack(side='left')
        self._entry_at_addr_rt = Entry(self._Frame17
            ,textvariable=self.entry_at_addr_rt)
        self._entry_at_addr_rt.pack(side='left')
        self._Frame20 = Frame(self._Frame4)
        self._Frame20.pack(fill='x',side='top')
        self._Frame5 = Frame(self._Frame10)
        self._Frame5.pack(side='left')
        self._left = Button(self._Frame5,command=self._on__left_command
            ,state='disabled',text='<-------(left key)--at trim left')
        self._left.pack(side='left')
        self._Frame13 = Frame(self._Frame10)
        self._Frame13.pack(side='left')
        self._right = Button(self._Frame13,command=self._on__right_command
            ,state='disabled',text='at trim right--(right key)------->')
        self._right.pack(side='left')
        self._Frame8 = Frame(self._Frame10)
        self._Frame8.pack(side='left')
        self._ArrowKeysOn = Checkbutton(self._Frame8
            ,text='Arrow keys control on',variable=self.ArrowKeysOn)
        self._ArrowKeysOn.pack(side='left')
        self._Frame11 = Frame(self._Frame7)
        self._Frame11.pack(side='left')
        self._ifbw0 = Radiobutton(self._Frame11,text='ifbw 0 (для ADF7021)'
            ,value=0,variable=self.ifbw)
        self._ifbw0.pack(side='top')
        self._ifbw1 = Radiobutton(self._Frame11,text='ifbw 1 (для ADF7021-N)'
            ,value=1,variable=self.ifbw)
        self._ifbw1.pack(side='top')
        self._Frame12 = Frame(self._Frame7)
        self._Frame12.pack(side='left')
        self._set_ifbw = Button(self._Frame12,command=self._on__set_ifbw_command
            ,state='disabled',text='Set IFBW')
        self._set_ifbw.pack(side='top')
        #
        #Your code here
        #
        

            

        
        self.device.set('ma41')
        self.serial_number.set('16001')
        self.ifbw.set(0)
        
        self.COM_port_index.set(str(defaultCOMportindex))
        self.text_to_send.set(str("sys info"))
        self.entry_ipaddr.set('10.2.1.20')
        self.entry_at_addr.set('0x0001')
        self.entry_at_addr_exe.set('0x1001')
        self.entry_at_addr_rt.set('0x0077')
        
    #
    #Start of event handler methods
    #


    def _on__COM_port_connect_command(self,Event=None):
        global connected
        try:
            global ser
            ser = serial.Serial("COM"+self.COM_port_index.get(),timeout=0.02)
            ser.baudrate = 115200
            connected=1
            self._COM_port_connect.config(state='disabled')
            self._prog_and_increment.config(state="normal")
            self._send.config(state="normal")
            self._set_ifbw.config(state="normal")
            self._prog_and_increment.config(state="normal")
            self._left.config(state="normal")
            self._right.config(state="normal")
            self._btn_ping.config(state="normal")
            self._btn_phyipaddr.config(state="normal")
            self._btn_ataddr.config(state="normal")
            self._btn_adf_tst.config(state="normal")            
            self._btn_adf_tst_50.config(state="normal")            
            self._btn_dbg0.config(state="normal")
            self._btn_dbg1.config(state="normal")
            self._btn_at_dst_rt.config(state="normal")
            self._btn_exe_at_dst_rt.config(state="normal")
            
        except:            
            connected=0
            mbox.showerror("Ошибка", "Невозможно открыть COM-порт")  
            
        



    def _on__btn_adf_tst_50_command(self,Event=None):
        write_ram('adf tst 50')

    def _on__btn_adf_tst_command(self,Event=None):
        write_ram('adf tst')

    def _on__btn_at_dst_rt_command(self,Event=None):
        write_ram('at dst '+str(self.entry_at_addr.get()))
        write_ram('rt')

    def _on__btn_ataddr_command(self,Event=None):
        write_ram('at addr')

    def _on__btn_dbg0_command(self,Event=None):
        write_ram('dbg 0')

    def _on__btn_dbg1_command(self,Event=None):
        write_ram('dbg 1')

    def _on__btn_exe_at_dst_rt_command(self,Event=None):
        write_ram('exe '+self.entry_at_addr_exe.get()+' at dst '+self.entry_at_addr_rt.get())
        write_ram('exe '+self.entry_at_addr_exe.get()+' rt')

    def _on__btn_phyipaddr_command(self,Event=None):
        write_ram('phy ipaddr')

    def _on__btn_ping_command(self,Event=None):
        write_ram('ping '+str(self.entry_ipaddr.get()))

    def _on__left_command(self,Event=None):
        global trim
        if trim <15:
            trim+=1
            read_and_print(1)
            write_ram_eep("at trim "+str(trim)+'\r')
            read_and_print(1)
            read_and_print(1)

    def _on__prog_and_increment_command(self,Event=None):
        setup_ip_mac_etc()
        ok=1

        if write_and_verify('at addr',self.ataddr.get(),'ataddr')==0:            
           ok=0
           mbox.showerror("Ошибка","Ошибка записи at addr")

        if write_and_verify('phy ipaddr',self.phyipaddr.get(),'ipaddr')==0:            
           ok=0
           mbox.showerror("Ошибка","Ошибка записи phy ipaddr")
           
        if write_and_verify('eth ipaddr',self.ethipaddr.get(),'ipaddr')==0:            
           ok=0
           mbox.showerror("Ошибка","Ошибка записи eth ipaddr")   
           
        if write_and_verify('phy macaddr',self.phymacaddr.get(),'macaddr')==0:            
           ok=0
           mbox.showerror("Ошибка","Ошибка записи phy macaddr")                 
           
        if write_and_verify('eth macaddr',self.ethmacaddr.get(),'macaddr')==0:            
           ok=0
           mbox.showerror("Ошибка","Ошибка записи eth macaddr")
           
        self._on__set_ifbw_command()
           
        
        if ok==1:
             self.serial_number.set(str(int(self.serial_number.get())+1))
        
        
        

    def _on__right_command(self,Event=None):
        global trim
        if trim >0:
            trim-=1
            read_and_print(1)
            write_ram_eep("at trim "+str(trim)+'\r')
            read_and_print(1)

    def _on__send_command(self,Event=None):
        ser.write(self._text_to_send.get()+'\r')
        


    def _on__set_ifbw_command(self,Event=None):        
        write_ram_eep('adf ifbw '+str(self.ifbw.get()))
        


    def _set_serial(self,Event=None):
        if self.device.get()=='ma41':
            self.serial_number.set('16001')
            
        if self.device.get()=='ma45':
            self.serial_number.set('16001')         

        if self.device.get()=='lsr4':
            self.serial_number.set('1008')

        if self.device.get()=='lse4':
            self.serial_number.set('1008')
      
        if self.device.get()=='1m500':
            self.serial_number.set('1008')
            
        setup_ip_mac_etc()


      
    #
    #Start of non-Rapyd user code
    #


pass #---end-of-form---

connected=0
COMtimeout=30
defaultCOMportindex=5
stop_reading_COM=0
trim=7

def read_string_from_serial():
    char = '*'
    string=""
    while (char<>'') and (char <> '\r'):
        char=ser.read()
        string=string+char
        if char=='\r':
            string=string+'\n'     
        if (char=='') and (string<>""):         
            string=string+'\n'
    return string

def read_and_print(disable_stop):
    string=''
    if stop_reading_COM==1 and disable_stop==0: return ''
    global connected
    if connected==1: 
        string=read_string_from_serial()
        if string<>"":
            App._ReceivedText.insert('1.0', string)  
    return string
            
def verify(string,value,type):
    if type=='ataddr':
        if string.upper().find(("0X"+str(hex(numh()*256+numl()))[2:].zfill(4)).upper())==-1: return 0
    if type=='ipaddr':
        if string.find(value)==-1: return 0
    if type=='macaddr':
        if string.find(value[:12]+str(hex(numh())[2:]).upper().zfill(2)+':'+str(hex(numl())[2:]).upper().zfill(2))==-1: return 0
        
    return 1
        


def write_and_verify(param,value,type):
    if value=='': return 1 #1-ok, 0-not ok
    global stop_reading_COM
    stop_reading_COM=1        

    write_eep(param+' '+value)
    string=write_eep(param)      

    if verify(string,value,type)==0:
        stop_reading_COM=0
        return 0
        
    stop_reading_COM=0
    return 1
    
    
def loopproc():             
     read_and_print(0)
     setup_ip_mac_etc() 
     Root.after(COMtimeout,loopproc) 

def write_ram(string):
    read_and_print(1)
    ser.write(string+'\r') 
    read_and_print(1)
    return read_and_print(1)
    
def write_eep(string):
    read_and_print(1)
    ser.write('eeprom '+string+'\r')
    read_and_print(1)
    return read_and_print(1)
    
def write_ram_eep(string):      
    write_eep(string)
    write_ram(string)
    
    
def numh():
    return int(math.floor(int(App.serial_number.get())/1000))
   
def numl():
    return int(int(App.serial_number.get()) % 1000)

def setup_ip_mac_etc():  

    if App.serial_number.get()=='':return

    try:
        int(App.serial_number.get())
    except:
        App.serial_number.set('')
        mbox.showerror('Ошибка','Недопустимый символ!')
        return
        
        

    if App.device.get()=='ma41' or App.device.get()=='ma45':    
        App.ataddr.set(hex(numh()*256+numl()))
        App.phyipaddr.set('10.2.'+str(numh())+'.'+str(numl()))
        App.ethipaddr.set('')
        App.phymacaddr.set('00:11:D8:13:'+hex(numh())[2:]+':'+hex(numl())[2:])
        App.ethmacaddr.set('')        

    if App.device.get()=='lsr4':
        App.ataddr.set(hex(numh()*256+numl()))
        App.phyipaddr.set('10.1.'+str(numh())+'.'+str(numl()))
        App.ethipaddr.set('')
        App.phymacaddr.set('00:11:D8:13:'+hex(numh())[2:]+':'+hex(numl())[2:])
        App.ethmacaddr.set('')        

    if App.device.get()=='lse4':
        App.ataddr.set(hex(numh()*256+numl()))
        App.phyipaddr.set('10.2.'+str(numh())+'.'+str(numl()))
        App.ethipaddr.set('10.0.'+str(numh())+'.'+str(numl()))
        App.phymacaddr.set('00:11:D8:13:'+hex(numh())[2:]+':'+hex(numl())[2:])
        App.ethmacaddr.set('00:11:D8:13:'+hex(numh())[2:]+':'+hex(numl())[2:]) 

    if App.device.get()=='1m500':            
        App.ataddr.set(hex(numh()*256+numl()))
        App.phyipaddr.set('10.1.'+str(numh())+'.'+str(numl()))
        App.ethipaddr.set('10.0.'+str(numh())+'.'+str(numl()))
        App.phymacaddr.set('00:11:D8:13:'+hex(numh())[2:]+':'+hex(numl())[2:])
        App.ethmacaddr.set('00:11:D8:13:'+hex(numh())[2:]+':'+hex(numl())[2:])          
        

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
 
    import sys
    
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

        Root.geometry('1000x640+10+10')
        Root.title('Horizon programming')
        

        
        Root.after(COMtimeout,loopproc)
        
        def left_key(event): 
           if App.ArrowKeysOn.get()==1:
               if connected==1:
                   App._on__left_command()
            
        def right_key(event):
           if App.ArrowKeysOn.get()==1:
                if connected==1:
                   App._on__right_command()            

        def up_key(event):
                if connected==1:
                   App._on__prog_and_increment_command()                
        
        Root.bind('<Left>', left_key)
        Root.bind('<Right>', right_key)
        Root.bind('<Up>', up_key)

        
        Root.mainloop()
    #--------------------------------------------------------------------------#
    # User code should go above this comment.                                  #
    #--------------------------------------------------------------------------#
except:
    rpErrorHandler.RunError()