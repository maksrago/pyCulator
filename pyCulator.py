import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import pyCulator_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = pyCulatorTopFrame (root)
    pyCulator_support.init(root, top)
    root.resizable(0, 0)
    root.mainloop()

w = None
def create_pyCulatorTopFrame(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = pyCulatorTopFrame (w)
    pyCulator_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_pyCulatorTopFrame():
    global w
    w.destroy()
    w = None

class pyCulatorTopFrame:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("372x641+364+126")
        top.title("pyCulator")
        top.configure(background="#d9d9d9")

        #Calculator Functions    
        #This fuction clears the calculator

        global operator
        global operandOne
        global operandTwo
        global output

        operator = ''
        operandOne = ''
        operandTwo = ''
        output = ''

        def clearOutput():
            self.pyCulatorOut.delete('1.0', tk.END)

        def pressZero():
            self.pyCulatorOut.insert(tk.END, '0')
        
        def pressOne():
            self.pyCulatorOut.insert(tk.END, '1')
        
        def pressTwo():
            self.pyCulatorOut.insert(tk.END, '2')

        def pressThree():
            self.pyCulatorOut.insert(tk.END, '3')

        def pressFour():
            self.pyCulatorOut.insert(tk.END, '4')
        
        def pressFive():
            self.pyCulatorOut.insert(tk.END, '5')

        def pressSix():
            self.pyCulatorOut.insert(tk.END, '6')

        def pressSeven():
            self.pyCulatorOut.insert(tk.END, '7')

        def pressEight():
            self.pyCulatorOut.insert(tk.END, '8')

        def pressNine():
            self.pyCulatorOut.insert(tk.END, '9')

        def pressAdd():
            x = self.pyCulatorOut.get('0.0', tk.END)
            if len(x) == 0:
                self.pyCulatorOut.insert(tk.END, '')
            else:
                self.pyCulatorOut.insert(tk.END, '+')

        def pressSubtract():
            x = self.pyCulatorOut.get('0.0', tk.END)
            if len(x) == 0:
                self.pyCulatorOut.insert(tk.END, '')
            else:
                self.pyCulatorOut.insert(tk.END, '-')

        def pressMultiply():
            x = self.pyCulatorOut.get('0.0', tk.END)
            if len(x) == 0:
                self.pyCulatorOut.insert(tk.END, '')
            else:
                self.pyCulatorOut.insert(tk.END, '*')

        def pressDivide():
            x = self.pyCulatorOut.get('0.0', tk.END)
            if len(x) == 0:
                self.pyCulatorOut.insert(tk.END, '')
            else:
                self.pyCulatorOut.insert(tk.END, '/')

        def pressModulo():
            x = self.pyCulatorOut.get('0.0', tk.END)
            if len(x) == 0:
                self.pyCulatorOut.insert(tk.END, '')
            else:
                self.pyCulatorOut.insert(tk.END, '%')

        def pressDecimal():
            x = self.pyCulatorOut.get('0.0', tk.END)
            if len(x) == 0:
                self.pyCulatorOut.insert(tk.END, '')
            else:
                self.pyCulatorOut.insert(tk.END, '.')

        def pressPM():
            x = self.pyCulatorOut.get('0.0', tk.END)
            if len(x) == 0:
                self.pyCulatorOut.insert(tk.END, '')
            else:
                self.pyCulatorOut.insert(tk.CURRENT, '-')

        def pressEquals():
            x = self.pyCulatorOut.get('0.0', tk.END)
            clearOutput()
            if len(x) == 0:
                self.pyCulatorOut.insert(tk.END, '')
            else:
                self.pyCulatorOut.insert(tk.END, eval(x))

        self.pyCulatorContainer = tk.Frame(top)
        self.pyCulatorContainer.place(relx=0.0, rely=0.0, relheight=1.006, relwidth=1.008)
        self.pyCulatorContainer.configure(relief='groove')
        self.pyCulatorContainer.configure(borderwidth="2")
        self.pyCulatorContainer.configure(relief="groove")
        self.pyCulatorContainer.configure(background="#252525")
        self.pyCulatorContainer.configure(width=375)

        self.Button_AC = tk.Button(self.pyCulatorContainer)
        self.Button_AC.place(relx=0.027, rely=0.295, height=84, width=87)
        self.Button_AC.configure(activebackground="#ececec")
        self.Button_AC.configure(activeforeground="#000000")
        self.Button_AC.configure(background="#a4a4a4")
        self.Button_AC.configure(disabledforeground="#a3a3a3")
        self.Button_AC.configure(font="-family {Source Sans Pro Light} -size 24")
        self.Button_AC.configure(foreground="#000000")
        self.Button_AC.configure(highlightbackground="#d9d9d9")
        self.Button_AC.configure(highlightcolor="black")
        self.Button_AC.configure(pady="0")
        self.Button_AC.configure(relief="flat")
        self.Button_AC.configure(text='''C''', command=clearOutput)
        self.Button_AC.configure(width=87)

        self.Button_PM = tk.Button(self.pyCulatorContainer)
        self.Button_PM.place(relx=0.267, rely=0.295, height=84, width=87)
        self.Button_PM.configure(activebackground="#ececec")
        self.Button_PM.configure(activeforeground="#000000")
        self.Button_PM.configure(background="#a4a4a4")
        self.Button_PM.configure(disabledforeground="#a3a3a3")
        self.Button_PM.configure(font="-family {Source Sans Pro Light} -size 24")
        self.Button_PM.configure(foreground="#000000")
        self.Button_PM.configure(highlightbackground="#d9d9d9")
        self.Button_PM.configure(highlightcolor="black")
        self.Button_PM.configure(pady="0")
        self.Button_PM.configure(relief="flat")
        self.Button_PM.configure(text='''±''', command=pressPM)

        self.Button_Modulo = tk.Button(self.pyCulatorContainer)
        self.Button_Modulo.place(relx=0.507, rely=0.295, height=84, width=87)
        self.Button_Modulo.configure(activebackground="#ececec")
        self.Button_Modulo.configure(activeforeground="#000000")
        self.Button_Modulo.configure(background="#a4a4a4")
        self.Button_Modulo.configure(disabledforeground="#a3a3a3")
        self.Button_Modulo.configure(font="-family {Source Sans Pro Light} -size 28")
        self.Button_Modulo.configure(foreground="#000000")
        self.Button_Modulo.configure(highlightbackground="#d9d9d9")
        self.Button_Modulo.configure(highlightcolor="black")
        self.Button_Modulo.configure(pady="0")
        self.Button_Modulo.configure(relief="flat")
        self.Button_Modulo.configure(text='''%''', command=pressModulo)

        self.Button_Divide = tk.Button(self.pyCulatorContainer)
        self.Button_Divide.place(relx=0.747, rely=0.295, height=84, width=87)
        self.Button_Divide.configure(activebackground="#ececec")
        self.Button_Divide.configure(activeforeground="#000000")
        self.Button_Divide.configure(background="#f69021")
        self.Button_Divide.configure(disabledforeground="#a3a3a3")
        self.Button_Divide.configure(font="-family {Source Sans Pro Light} -size 30")
        self.Button_Divide.configure(foreground="#FFFFFF")
        self.Button_Divide.configure(highlightbackground="#d9d9d9")
        self.Button_Divide.configure(highlightcolor="black")
        self.Button_Divide.configure(pady="0")
        self.Button_Divide.configure(relief="flat")
        self.Button_Divide.configure(text='''÷''', command=pressDivide)

        self.Button_7 = tk.Button(self.pyCulatorContainer)
        self.Button_7.place(relx=0.027, rely=0.434, height=84, width=87)
        self.Button_7.configure(activebackground="#ececec")
        self.Button_7.configure(activeforeground="#000000")
        self.Button_7.configure(background="#d3d4d6")
        self.Button_7.configure(disabledforeground="#a3a3a3")
        self.Button_7.configure(font="-family {Source Sans Pro Light} -size 24")
        self.Button_7.configure(foreground="#000000")
        self.Button_7.configure(highlightbackground="#d9d9d9")
        self.Button_7.configure(highlightcolor="black")
        self.Button_7.configure(pady="0")
        self.Button_7.configure(relief="flat")
        self.Button_7.configure(text='''7''', command=pressSeven)

        self.Button_8 = tk.Button(self.pyCulatorContainer)
        self.Button_8.place(relx=0.267, rely=0.434, height=84, width=87)
        self.Button_8.configure(activebackground="#ececec")
        self.Button_8.configure(activeforeground="#000000")
        self.Button_8.configure(background="#d3d4d6")
        self.Button_8.configure(disabledforeground="#a3a3a3")
        self.Button_8.configure(font="-family {Source Sans Pro Light} -size 24")
        self.Button_8.configure(foreground="#000000")
        self.Button_8.configure(highlightbackground="#d9d9d9")
        self.Button_8.configure(highlightcolor="black")
        self.Button_8.configure(pady="0")
        self.Button_8.configure(relief="flat")
        self.Button_8.configure(text='''8''', command=pressEight)

        self.Button_9 = tk.Button(self.pyCulatorContainer)
        self.Button_9.place(relx=0.507, rely=0.434, height=84, width=87)
        self.Button_9.configure(activebackground="#ececec")
        self.Button_9.configure(activeforeground="#000000")
        self.Button_9.configure(background="#d9d9d9")
        self.Button_9.configure(disabledforeground="#a3a3a3")
        self.Button_9.configure(font="-family {Source Sans Pro Light} -size 24")
        self.Button_9.configure(foreground="#000000")
        self.Button_9.configure(highlightbackground="#d9d9d9")
        self.Button_9.configure(highlightcolor="black")
        self.Button_9.configure(pady="0")
        self.Button_9.configure(relief="flat")
        self.Button_9.configure(text='''9''', command=pressNine)

        self.Button_Multiply = tk.Button(self.pyCulatorContainer)
        self.Button_Multiply.place(relx=0.747, rely=0.434, height=84, width=87)
        self.Button_Multiply.configure(activebackground="#ececec")
        self.Button_Multiply.configure(activeforeground="#000000")
        self.Button_Multiply.configure(background="#f69021")
        self.Button_Multiply.configure(disabledforeground="#a3a3a3")
        self.Button_Multiply.configure(font="-family {Source Sans Pro Light} -size 30")
        self.Button_Multiply.configure(foreground="#FFFFFF")
        self.Button_Multiply.configure(highlightbackground="#d9d9d9")
        self.Button_Multiply.configure(highlightcolor="black")
        self.Button_Multiply.configure(pady="0")
        self.Button_Multiply.configure(relief="flat")
        self.Button_Multiply.configure(text='''×''', command=pressMultiply)

        self.Button_4 = tk.Button(self.pyCulatorContainer)
        self.Button_4.place(relx=0.027, rely=0.574, height=84, width=87)
        self.Button_4.configure(activebackground="#ececec")
        self.Button_4.configure(activeforeground="#000000")
        self.Button_4.configure(background="#d9d9d9")
        self.Button_4.configure(disabledforeground="#a3a3a3")
        self.Button_4.configure(font="-family {Source Sans Pro Light} -size 28")
        self.Button_4.configure(foreground="#000000")
        self.Button_4.configure(highlightbackground="#d9d9d9")
        self.Button_4.configure(highlightcolor="black")
        self.Button_4.configure(pady="0")
        self.Button_4.configure(relief="flat")
        self.Button_4.configure(text='''4''', command=pressFour)

        self.Button_5 = tk.Button(self.pyCulatorContainer)
        self.Button_5.place(relx=0.267, rely=0.574, height=84, width=87)
        self.Button_5.configure(activebackground="#ececec")
        self.Button_5.configure(activeforeground="#000000")
        self.Button_5.configure(background="#d9d9d9")
        self.Button_5.configure(disabledforeground="#a3a3a3")
        self.Button_5.configure(font="-family {Source Sans Pro Light} -size 28")
        self.Button_5.configure(foreground="#000000")
        self.Button_5.configure(highlightbackground="#d9d9d9")
        self.Button_5.configure(highlightcolor="black")
        self.Button_5.configure(pady="0")
        self.Button_5.configure(relief="flat")
        self.Button_5.configure(text='''5''', command=pressFive)

        self.Button_6 = tk.Button(self.pyCulatorContainer)
        self.Button_6.place(relx=0.507, rely=0.574, height=84, width=87)
        self.Button_6.configure(activebackground="#ececec")
        self.Button_6.configure(activeforeground="#000000")
        self.Button_6.configure(background="#d9d9d9")
        self.Button_6.configure(disabledforeground="#a3a3a3")
        self.Button_6.configure(font="-family {Source Sans Pro Light} -size 28")
        self.Button_6.configure(foreground="#000000")
        self.Button_6.configure(highlightbackground="#d9d9d9")
        self.Button_6.configure(highlightcolor="black")
        self.Button_6.configure(pady="0")
        self.Button_6.configure(relief="flat")
        self.Button_6.configure(text='''6''', command=pressSix)

        self.Button_Minus = tk.Button(self.pyCulatorContainer)
        self.Button_Minus.place(relx=0.747, rely=0.574, height=84, width=87)
        self.Button_Minus.configure(activebackground="#ececec")
        self.Button_Minus.configure(activeforeground="#000000")
        self.Button_Minus.configure(background="#f69021")
        self.Button_Minus.configure(disabledforeground="#a3a3a3")
        self.Button_Minus.configure(font="-family {Source Sans Pro Light} -size 30")
        self.Button_Minus.configure(foreground="#FFFFFF")
        self.Button_Minus.configure(highlightbackground="#d9d9d9")
        self.Button_Minus.configure(highlightcolor="black")
        self.Button_Minus.configure(pady="0")
        self.Button_Minus.configure(relief="flat")
        self.Button_Minus.configure(text='''-''', command=pressSubtract)
        self.Button_Minus.configure(width=87)

        self.Button_1 = tk.Button(self.pyCulatorContainer)
        self.Button_1.place(relx=0.027, rely=0.713, height=84, width=87)
        self.Button_1.configure(activebackground="#ececec")
        self.Button_1.configure(activeforeground="#000000")
        self.Button_1.configure(background="#d9d9d9")
        self.Button_1.configure(disabledforeground="#a3a3a3")
        self.Button_1.configure(font="-family {Source Sans Pro Light} -size 28")
        self.Button_1.configure(foreground="#000000")
        self.Button_1.configure(highlightbackground="#d9d9d9")
        self.Button_1.configure(highlightcolor="black")
        self.Button_1.configure(pady="0")
        self.Button_1.configure(relief="flat")
        self.Button_1.configure(text='''1''', command=pressOne)

        self.Button_2 = tk.Button(self.pyCulatorContainer)
        self.Button_2.place(relx=0.267, rely=0.713, height=84, width=87)
        self.Button_2.configure(activebackground="#ececec")
        self.Button_2.configure(activeforeground="#000000")
        self.Button_2.configure(background="#d9d9d9")
        self.Button_2.configure(disabledforeground="#a3a3a3")
        self.Button_2.configure(font="-family {Source Sans Pro Light} -size 28")
        self.Button_2.configure(foreground="#000000")
        self.Button_2.configure(highlightbackground="#d9d9d9")
        self.Button_2.configure(highlightcolor="black")
        self.Button_2.configure(pady="0")
        self.Button_2.configure(relief="flat")
        self.Button_2.configure(text='''2''', command=pressTwo)

        self.Button_3 = tk.Button(self.pyCulatorContainer)
        self.Button_3.place(relx=0.507, rely=0.713, height=84, width=87)
        self.Button_3.configure(activebackground="#ececec")
        self.Button_3.configure(activeforeground="#000000")
        self.Button_3.configure(background="#d9d9d9")
        self.Button_3.configure(disabledforeground="#a3a3a3")
        self.Button_3.configure(font="-family {Source Sans Pro Light} -size 28")
        self.Button_3.configure(foreground="#000000")
        self.Button_3.configure(highlightbackground="#d9d9d9")
        self.Button_3.configure(highlightcolor="black")
        self.Button_3.configure(pady="0")
        self.Button_3.configure(relief="flat")
        self.Button_3.configure(text='''3''', command=pressThree)

        self.Button_Plus = tk.Button(self.pyCulatorContainer)
        self.Button_Plus.place(relx=0.747, rely=0.713, height=84, width=87)
        self.Button_Plus.configure(activebackground="#ececec")
        self.Button_Plus.configure(activeforeground="#000000")
        self.Button_Plus.configure(background="#f69021")
        self.Button_Plus.configure(disabledforeground="#a3a3a3")
        self.Button_Plus.configure(font="-family {Source Sans Pro Light} -size 30")
        self.Button_Plus.configure(foreground="#FFFFFF")
        self.Button_Plus.configure(highlightbackground="#d9d9d9")
        self.Button_Plus.configure(highlightcolor="black")
        self.Button_Plus.configure(pady="0")
        self.Button_Plus.configure(relief="flat")
        self.Button_Plus.configure(text='''+''', command=pressAdd)

        self.Button_0 = tk.Button(self.pyCulatorContainer)
        self.Button_0.place(relx=0.027, rely=0.853, height=84, width=176)
        self.Button_0.configure(activebackground="#ececec")
        self.Button_0.configure(activeforeground="#000000")
        self.Button_0.configure(background="#d9d9d9")
        self.Button_0.configure(disabledforeground="#a3a3a3")
        self.Button_0.configure(font="-family {Source Sans Pro Light} -size 28")
        self.Button_0.configure(foreground="#000000")
        self.Button_0.configure(highlightbackground="#d9d9d9")
        self.Button_0.configure(highlightcolor="black")
        self.Button_0.configure(pady="0")
        self.Button_0.configure(relief="flat")
        self.Button_0.configure(text='''0''', command=pressZero)

        self.Button_Decimal = tk.Button(self.pyCulatorContainer)
        self.Button_Decimal.place(relx=0.507, rely=0.853, height=84, width=87)
        self.Button_Decimal.configure(activebackground="#ececec")
        self.Button_Decimal.configure(activeforeground="#000000")
        self.Button_Decimal.configure(background="#d9d9d9")
        self.Button_Decimal.configure(disabledforeground="#a3a3a3")
        self.Button_Decimal.configure(font="-family {Source Sans Pro Light} -size 30")
        self.Button_Decimal.configure(foreground="#000000")
        self.Button_Decimal.configure(highlightbackground="#d9d9d9")
        self.Button_Decimal.configure(highlightcolor="black")
        self.Button_Decimal.configure(pady="0")
        self.Button_Decimal.configure(relief="flat")
        self.Button_Decimal.configure(text='''.''', command=pressDecimal)

        self.Button_Equals = tk.Button(self.pyCulatorContainer)
        self.Button_Equals.place(relx=0.747, rely=0.853, height=84, width=87)
        self.Button_Equals.configure(activebackground="#ececec")
        self.Button_Equals.configure(activeforeground="#000000")
        self.Button_Equals.configure(background="#f69021")
        self.Button_Equals.configure(disabledforeground="#a3a3a3")
        self.Button_Equals.configure(font="-family {Source Sans Pro Light} -size 30")
        self.Button_Equals.configure(foreground="#FFFFFF")
        self.Button_Equals.configure(highlightbackground="#d9d9d9")
        self.Button_Equals.configure(highlightcolor="black")
        self.Button_Equals.configure(pady="0")
        self.Button_Equals.configure(relief="flat")
        self.Button_Equals.configure(text='''=''', command=pressEquals)

        self.pyCulatorOut = tk.Text(self.pyCulatorContainer)
        self.pyCulatorOut.place(relx=0.027, rely=0.155, relheight=0.124, relwidth=0.944)
        self.pyCulatorOut.configure(background="#252525")
        self.pyCulatorOut.configure(font="-family {Source Sans Pro} -size 48")
        self.pyCulatorOut.configure(foreground="#FFFFFF")
        self.pyCulatorOut.configure(highlightbackground="#d9d9d9")
        self.pyCulatorOut.configure(highlightcolor="black")
        self.pyCulatorOut.configure(insertbackground="black")
        self.pyCulatorOut.configure(pady="0")
        self.pyCulatorOut.configure(relief="flat")
        self.pyCulatorOut.configure(selectbackground="#c4c4c4")
        self.pyCulatorOut.configure(selectforeground="black")
        self.pyCulatorOut.configure(width=354)
        self.pyCulatorOut.configure(wrap="word")

if __name__ == '__main__':
    vp_start_gui()