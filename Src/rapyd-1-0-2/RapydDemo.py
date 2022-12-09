#!/usr/bin/python

import rpErrorHandler
from Tkinter import *
#----------------------------------------------------------------------------------------#
#                                                                                        #
#                                       RapydDemo                                        #
#                                                                                        #
#----------------------------------------------------------------------------------------#
class RapydDemo(Frame):
    def __init__(self,Master=None,*pos,**kw):
        kw['takefocus'] = 1
        """
        This is a *really* simple little calculator just to demonstrate some of
            the features of Rapyd-Tk. Note that the calculations are done Python
            style, that is, 3/2 evaluates to 1. If you want a floating point
            result, include a floating point number: 3.0/2 evaluates to 1.5.
        """

        apply(Frame.__init__,(self,Master),kw)
        self.bind('<KeyPress>',self.__on_calc_Key)
        self.__Frame2 = Frame(self,relief='sunken')
        self.__Frame2.pack(fill='both',pady='5',side='top')
        self.__Label1 = Label(self.__Frame2,anchor='e',font=('helvetica', 12, 'bold')
            ,takefocus=1,text=0)
        self.__Label1.pack(expand='yes',fill='both',padx='4',pady='4',side='left')
        self.__Label1.bind('<KeyPress>',self.__on_calc_Key)
        self.__Frame1 = Frame(self)
        self.__Frame1.pack(expand='yes',fill='both',side='top')
        self.__Frame4 = Frame(self.__Frame1)
        self.__Frame4.pack(expand='yes',fill='both',side='left')
        self.__ButtonBksp = Button(self.__Frame4,padx='0',text='Bksp')
        self.__ButtonBksp.pack(expand='yes',fill='both',side='top')
        self.__ButtonBksp.bind('<ButtonRelease-1>',self.__on_ButtonBksp_ButRel_1)
        self.__ButtonDigit7 = Button(self.__Frame4,padx='0',text=7)
        self.__ButtonDigit7.pack(expand='yes',fill='both',side='top')
        self.__ButtonDigit7.bind('<ButtonRelease-1>',self.__on_ButtonDigit_ButRel_1)
        self.__ButtonDigit4 = Button(self.__Frame4,padx='0',text=4)
        self.__ButtonDigit4.pack(expand='yes',fill='both',side='top')
        self.__ButtonDigit4.bind('<ButtonRelease-1>',self.__on_ButtonDigit_ButRel_1)
        self.__ButtonDigit1 = Button(self.__Frame4,padx='0',text=1)
        self.__ButtonDigit1.pack(expand='yes',fill='both',side='top')
        self.__ButtonDigit1.bind('<ButtonRelease-1>',self.__on_ButtonDigit_ButRel_1)
        self.__ButtonDigit0 = Button(self.__Frame4,padx='0',text=0,width='4')
        self.__ButtonDigit0.pack(expand='yes',fill='both',side='top')
        self.__ButtonDigit0.bind('<ButtonRelease-1>',self.__on_ButtonDigit_ButRel_1)
        self.__Frame3 = Frame(self.__Frame1)
        self.__Frame3.pack(expand='yes',fill='both',side='left')
        self.__ButtonRocip = Button(self.__Frame3,padx='0',text='1/X')
        self.__ButtonRocip.pack(expand='yes',fill='both',side='top')
        self.__ButtonRocip.bind('<ButtonRelease-1>',self.__on_ButtonRocip_ButRel_1)
        self.__ButtonDigit8 = Button(self.__Frame3,padx='0',text=8)
        self.__ButtonDigit8.pack(expand='yes',fill='both',side='top')
        self.__ButtonDigit8.bind('<ButtonRelease-1>',self.__on_ButtonDigit_ButRel_1)
        self.__ButtonDigit5 = Button(self.__Frame3,padx='0',text=5)
        self.__ButtonDigit5.pack(expand='yes',fill='both',side='top')
        self.__ButtonDigit5.bind('<ButtonRelease-1>',self.__on_ButtonDigit_ButRel_1)
        self.__ButtonDigit2 = Button(self.__Frame3,padx='0',text=2)
        self.__ButtonDigit2.pack(expand='yes',fill='both',side='top')
        self.__ButtonDigit2.bind('<ButtonRelease-1>',self.__on_ButtonDigit_ButRel_1)
        self.__ButtonDot = Button(self.__Frame3,padx='0',text='.')
        self.__ButtonDot.pack(expand='yes',fill='both',side='top')
        self.__ButtonDot.bind('<ButtonRelease-1>',self.__on_ButtonDigit_ButRel_1)
        self.__Frame5 = Frame(self.__Frame1)
        self.__Frame5.pack(expand='yes',fill='both',side='left')
        self.__ButtonClr = Button(self.__Frame5,padx='0',text='Clr')
        self.__ButtonClr.pack(expand='yes',fill='both',side='top')
        self.__ButtonClr.bind('<ButtonRelease-1>',self.__on_ButtonClr_ButRel_1)
        self.__ButtonDigit9 = Button(self.__Frame5,padx='0',text=9)
        self.__ButtonDigit9.pack(expand='yes',fill='both',side='top')
        self.__ButtonDigit9.bind('<ButtonRelease-1>',self.__on_ButtonDigit_ButRel_1)
        self.__ButtonDigit6 = Button(self.__Frame5,padx='0',text=6)
        self.__ButtonDigit6.pack(expand='yes',fill='both',side='top')
        self.__ButtonDigit6.bind('<ButtonRelease-1>',self.__on_ButtonDigit_ButRel_1)
        self.__ButtonDigit3 = Button(self.__Frame5,padx='0',text=3)
        self.__ButtonDigit3.pack(expand='yes',fill='both',side='top')
        self.__ButtonDigit3.bind('<ButtonRelease-1>',self.__on_ButtonDigit_ButRel_1)
        self.__ButtonEqual = Button(self.__Frame5,padx='0',text='=')
        self.__ButtonEqual.pack(expand='yes',fill='both',side='top')
        self.__ButtonEqual.bind('<ButtonRelease-1>',self.__on_ButtonEqual_ButRel_1)
        self.__Frame6 = Frame(self.__Frame1)
        self.__Frame6.pack(expand='yes',fill='both',side='left')
        self.__ButtonNeg = Button(self.__Frame6,padx='0',text='+/-')
        self.__ButtonNeg.pack(expand='yes',fill='both',side='top')
        self.__ButtonNeg.bind('<ButtonRelease-1>',self.__on_ButtonNeg_ButRel_1)
        self.__ButtonDivide = Button(self.__Frame6,padx='0',text='/')
        self.__ButtonDivide.pack(expand='yes',fill='both',side='top')
        self.__ButtonDivide.bind('<ButtonRelease-1>',self.__on_ButtonDigit_ButRel_1)
        self.__ButtonMultiply = Button(self.__Frame6,padx='0',text='*')
        self.__ButtonMultiply.pack(expand='yes',fill='both',side='top')
        self.__ButtonMultiply.bind('<ButtonRelease-1>',self.__on_ButtonDigit_ButRel_1)
        self.__ButtonSubtract = Button(self.__Frame6,padx='0',text='-')
        self.__ButtonSubtract.pack(expand='yes',fill='both',side='top')
        self.__ButtonSubtract.bind('<ButtonRelease-1>',self.__on_ButtonDigit_ButRel_1)
        self.__ButtonAdd = Button(self.__Frame6,padx='0',text='+')
        self.__ButtonAdd.pack(expand='yes',fill='both',side='top')
        self.__ButtonAdd.bind('<ButtonRelease-1>',self.__on_ButtonDigit_ButRel_1)
        #
        #Your code here
        #
        self.__Value = '0'
        self.__Update()
    #
    #Start of event handler methods
    #


    def __on_ButtonBksp_ButRel_1(self,Event=None):
        """
        User clicked on the backspace button.
        """
        self.__RemChr()

    def __on_ButtonClr_ButRel_1(self,Event=None):
        """"
        User clicked on the clear-all button.
        """
        self.__Value = '0'
        self.__Update()

    def __on_ButtonDigit_ButRel_1(self,Event=None):
        """
        User clicked on a digit button.
        """
        Digit = str(Event.widget.config()['text'][4])
        self.__NewChr(Digit)


    def __on_ButtonEqual_ButRel_1(self,Event=None):
        """
        User hit the evaluate button
        """
        self.__Eval()


    def __on_ButtonNeg_ButRel_1(self,Event=None):
        """
        User clicked on the negate button
        """
        if self.__Eval():
            if self.__Value <> '0':
                self.__Value = '-%s'%self.__Value
                self.__Eval()        

    def __on_ButtonRocip_ButRel_1(self,Event=None):
        """
        User hit the rociprical button.
        """
        if self.__Eval():
            if self.__Value <> '0':
                self.__Value = '1.0/%s'%self.__Value
                self.__Eval()

    def __on_calc_Key(self,Event=None):
        """
        User pressed a key.
        """
        if len(Event.char) == 1:
            if ord(Event.char) == 8:
                self.__RemChr()
            elif ord(Event.char) == 13:
                self.__Eval()
            elif ord(Event.char) >= ord(' '):    
                self.__NewChr(Event.char)
    #
    #Start of non-Rapyd user code
    #
    def __Eval(self):
        """
        Attempt to evaluate and update __Value
        
        Result is 1 if the evaluation succeeded and 0 if not.
        """
        try:
            #This will blow up the the expression isn't valid
            T = eval(self.__Value)
            #And this will blow up if the result isn't numeric
            float(T)
            self.__Value = str(T)
            self.__Update()
            Result = 1
        except:
            #Expression is invalid
            Hold = self.__Value
            self.__Value = '--- ERROR ---'
            self.__Update()
            self.update_idletasks()
            time.sleep(1)
            self.__Value = Hold
            self.__Update()
            Result = 0
        return Result  

    def __NewChr(self,Chr):
        """
        Add a new character to the current value.
        """
        if self.__Value == '0':
            #If value is zero the new digit replaces, otherwise it get appended.
            self.__Value = ''
        self.__Value += str(Chr)
        self.__Update()

    def __RemChr(self):
        """
        Remove one character from the current value.
        """
        self.__Value = self.__Value[:-1]
        self.__Update()
        
    def __Update(self):
        """
        Deal with self.__Value having been changed.
        """
        self.__Value = str(self.__Value)
        if not self.__Value:
            self.__Value = '0'
        self.__Label1.config(text=self.__Value)
        self.focus_set()

pass #---end-of-form---

try:
    #--------------------------------------------------------------------------#
    # User code should go after this comment so it is inside the "try".        #
    #     This allows rpErrorHandler to gain control on an error so it         #
    #     can properly display a Rapyd-aware error message.                    #
    #--------------------------------------------------------------------------#
    import os.path
    import sys
    import time
    if not '.' in sys.path:
        sys.path.append('.')
    if __name__ == '__main__':

        Root = Tk()
        import Tkinter
        Tkinter.CallWrapper = rpErrorHandler.CallWrapper
        del Tkinter
        App = RapydDemo(Root)
        App.pack(expand='yes',fill='both')

        Root.geometry('200x280+10+10')
        Root.title('calc')
        Root.mainloop()
    #--------------------------------------------------------------------------#
    # User code should go above this comment.                                  #
    #--------------------------------------------------------------------------#
except:
    rpErrorHandler.RunError()