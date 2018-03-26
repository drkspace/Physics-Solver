#(c) Daniel Robert Kramer, All Rights Reserved
from Tkinter import *
from rhr import *
import pyperclip
from decimal import *
from subprocess import call
from ttk import Separator, Style
from PIL import Image, ImageTk
from os import listdir
from os.path import isfile, join
from random import randint

#Creating the main window
root = Tk()
root.geometry('700x700')

#Names of the constants
constant_label = [u"\u03C0", 'e', 'Proton/Neutron Mass (kg)', 'Electron Mass (kg)', 'Avagadro\'s Number (1/mol)', 'Electron Charge (C)', 'Protron Charge (C)', 'G (N*m^2/kg^2)', 'g (m/s^2)', u"\u03B5"+u"\u2080", "k", u"\u03BC"+u"\u2080","Mass of the earth (kg)", "Mass of the Sun (kg)"]

#Values of the constants
constant_values = ['3.14159', '2.71828', '1.67*10^-27', '9.11*10^-31', '6.02*10^23', '-1.6*10^-19', '1.6*10^-19','6.67*10^-11', '9.81', '8.85*10^-12', '8.99*10^9', '4'+u"\u03C0"+"*10^-7", "5.972*10^24", "1.989*10^30"]

#Style for the seperator lines in the sections
s=Style()
s.configure('TSeparator', background='black')	

#Method for finding the direction of the force on a particle given a field and velocity
def rhr_force():

	#Setting the frame to make cleanup easier
	frame = Frame(root)
	frame.grid(row=0, column=0, sticky='w')

	Separator(frame, style='TSeparator', orient='vertical').grid(row=0, column=1, rowspan=7, sticky='ns')
	
	#Setting the variables 
	b = IntVar()
	v = IntVar()
	f = StringVar()
	f.set('')

	#Method to set the answer if all the radio buttons are selected
	def update():
		
		#Testing to see if the both radio button sets are selected
		if b.get() is not 0 and v.get() is not 0:
			f.set("Force Direction: {}".format(vector_to_english[str(rhr_field(B=b.get(), V=v.get()))]))
	
	#Set the label for the magnetic field direction
	Label(frame, text = "Magnetic Field Direction").grid(row=0, column=0, sticky='w', padx=1)
	for i in range(len(printout_list)):
		
		#Create the radiobutton for the direction of the field
		Radiobutton(frame, text = printout_list[i], variable = b, value= i+1, command = lambda: update()).grid(row = i+1, column = 0, sticky='w', padx=1)

	#Set the label for the velocity field direction
	Label(frame, text = "Velocity Direction").grid(row=0, column=2, sticky='w', padx=1)
	for i in range(len(printout_list)):
		
		#Create the radiobutton for the direction of the velocity
		Radiobutton(frame, text = printout_list[i], variable = v, value= i+1, command = lambda: update()).grid(row = i+1, column = 2, sticky='w', padx=1)

	#Label for the answer
	Label(frame, textvariable = f, font="16").grid(row = 8, column = 0, sticky='w', columnspan=3)
	
	#Method and button for returning to the menu
	def return_to_menu():
		frame.grid_forget()
		main()
	
	Button(frame, text = "Back to menu", command = lambda: return_to_menu()).grid(row=0, column=3, sticky='w')

#Method for finding the direction of the magnetic field given a current direction and point location
def rhr_wire():
	
	#Setting the frame to make cleanup easier
	frame = Frame(root)
	frame.grid(row=0, column=0, sticky='w')

	Separator(frame, style='TSeparator', orient='vertical').grid(row=0, column=1, rowspan=7, sticky='ns')

	#Setting the variables 
	i = IntVar()
	p = IntVar()
	b = StringVar()
	b.set('')

	#Method to set the answer if all the radio buttons are selected
	def update():
		
		#Testing to see if the both radio button sets are selected
		if i.get() is not 0 and p.get() is not 0:
			b.set(vector_to_english[str(rhr_current(I=i.get(), P=p.get()))])

	#Set the label for the current direction
	Label(frame, text = "Current Direction").grid(row=0, column=0, sticky='w', padx=1)
	for k in range(len(printout_list)):

		#Create the radiobutton for the direction of the current
		Radiobutton(frame, text = printout_list[k], variable = i, value= k+1, command = lambda: update()).grid(row = k+1, column = 0, sticky='w', padx=1)

	#Set the label for the point location
	Label(frame, text = "Point Location").grid(row=0, column=2, sticky='w', padx=1)
	for k in range(len(printout_list_2)):

		#Create the radiobutton for the location of the point
		Radiobutton(frame, text = printout_list_2[k], variable = p, value= k+1, command = lambda: update()).grid(row = k+1, column = 2, sticky='w', padx=1)

	Label(frame, textvariable = b, font="16").grid(row = 8, column = 0, sticky='w', columnspan=3)
	
	def return_to_menu():
		frame.grid_forget()
		main()
	
	Button(frame, text = "Back to menu", command = lambda: return_to_menu()).grid(row=0, column=3, sticky='w')

def lenz_law():
	frame = Frame(root)
	frame.grid(row=0, column=0, sticky='w')
	
	Separator(frame, style='TSeparator', orient='vertical').grid(row=0, column=1, rowspan=7, sticky='ns')
	Separator(frame, style='TSeparator', orient='vertical').grid(row=0, column=3, rowspan=7, sticky='ns')


	b = IntVar()
	db = IntVar()
	da = IntVar()
	d = StringVar()
	d.set('')

	def update():
		if b.get() is not 0 and db.get() is not 0 and da.get() is not 0:
			d.set(induced_current(B=b.get(), dB=db.get(), dA=da.get()))

	Label(frame, text = "Magnetic Field Direction").grid(row=0, column=0, sticky='w', padx=1)
	for k in range(len(printout_list)):
		Radiobutton(frame, text = printout_list[k], variable = b, value= k+1, command = lambda: update()).grid(row = k+1, column = 0, sticky='w', padx=1)

	Label(frame, text = "Change in the Magnetic Field").grid(row=0, column=2, sticky='w', padx=1)
	for k in range(len(printout_list_3)):
		Radiobutton(frame, text = printout_list_3[k], variable = db, value= k+1, command = lambda: update()).grid(row = k+1, column = 2, sticky='w', padx=1)
	
	Label(frame, text = "Change in the Area").grid(row=0, column=4, sticky='w', padx=1)
	for k in range(len(printout_list_3)):
		Radiobutton(frame, text = printout_list_3[k], variable = da, value= k+1, command = lambda: update()).grid(row = k+1, column = 4, sticky='w', padx=1)

	Label(frame, textvariable = d, font ="20").grid(row = 8, column = 0, sticky='w', columnspan=3)
	
	def return_to_menu():
		frame.grid_forget()
		main()
	
	Button(frame, text = "Back to menu", command = lambda: return_to_menu()).grid(row=0, column=5, sticky='w')

def set_clip_board(astr):
	pyperclip.copy(astr)

def constants():

	frame=Frame(root)
	frame.grid(row=0,column=0)

	for i in range(len(constant_label)):
		text = constant_label[i]+': '+constant_values[i]
		value = constant_values[i]
		Label(frame, text=text).grid(row = i, column=0, sticky='w')
		Button(frame, text='Copy Value', command = lambda v=value: set_clip_board(v)).grid(row=i, column=1)

	def goto(command):
		frame.grid_forget()
		command()
	Button(frame, text='Calculate Larger Value', command=lambda: goto(pi)).grid(row=0, column = 3,sticky='w')
	Button(frame, text='Calculate Larger Value', command=lambda: goto(e)).grid(row=1, column = 3,sticky='w')
	Button(frame, text='Back to the menu', command = lambda: goto(menu)).grid(row=len(constant_label)-1, column = 3 , sticky='w')

def pi():

	win = Tk()
	Label(win, text="Number of Digits").grid(row=0, column=0)	
	e=Entry(win)
	e.grid(row=0, column=1)
	Button(win, text="Submit", command=lambda: calculate(e.get())).grid(row=1,column=0)
	
	def calculate(digits):
		ZERO = Decimal('0')
		ONE = Decimal('1')
		TWO = Decimal('2')
		TEN = Decimal('10')
		NEG_ONE = Decimal('-1')
		win.destroy()
		frame=Frame(root)
		frame.grid(row=0, column=0)
		Label(frame, text='pi:').grid(row=0, column=0)
		v = StringVar()
		Label(frame, textvariable=v, wraplength=410).grid(row=1, column=0, sticky='w')
		v.set("calculating value")
		def back():
			frame.grid_forget()
			constants()
		Button(frame, text="back", command = back).grid(row=2, column=0, sticky='w')
		digits=int(digits)
		#print "Setting up decimal"
	    	getcontext().prec = digits+10
	    	#print "Done setting up decimal"

	    	sum = Decimal('0')
	    	a = Decimal('12')**Decimal('.5')
	    	nThird = Decimal('-1')/Decimal('3')
	  
	    	i=ZERO
		last_answer=str(-1)
	    	while True:
			numerator = nThird**i
			den = i*TWO+ONE
			sum = sum + (numerator/den)
			i+=ONE
			
			if i%TWO==0:
				ans = str((a*sum).quantize(Decimal(TEN**(NEG_ONE*Decimal(digits))), rounding=ROUND_HALF_UP))
				if last_answer == ans:
					break
				call('clear',shell=True)
				v.set(ans)
				print ans
				last_answer=str(ans)
			
def e():
	
	win = Tk()
	Label(win, text="Number of Digits").grid(row=0, column=0)	
	en=Entry(win)
	en.grid(row=0, column=1)
	Button(win, text="Submit", command=lambda: calculate(en.get())).grid(row=1,column=0)

	def calculate(digits):
		TEN = Decimal('10')
		NEG_ONE = Decimal('-1')
		win.destroy()
		frame=Frame(root)
		frame.grid(row=0, column=0)
		Label(frame, text='e:').grid(row=0, column=0)
		v = StringVar()
		Label(frame, textvariable=v, wraplength=410).grid(row=1, column=0, sticky='w')
		v.set("calculating value")
		def back():
			frame.grid_forget()
			constants()
		Button(frame, text="back", command = back).grid(row=2, column=0, sticky='w')
		digits=int(digits)
		#print "Setting up decimal"
	    	getcontext().prec = digits+10
	    	#print "Done setting up decimal"

	    	sum = Decimal('0')

		i=Decimal('0')
		last_answer=Decimal('-1')
		fact=Decimal('1')
		while True:
			
			sum+=(i+Decimal('1'))/fact
			i+=Decimal('1')
			fact*=i

			ans = str((Decimal('.5')*sum).quantize(Decimal(TEN**(NEG_ONE*Decimal(digits))), rounding=ROUND_HALF_UP))
			if last_answer == ans:
				break
			call('clear',shell=True)
			v.set(ans)
			print ans
			last_answer=str(ans)
			
		

def menu():
	frame=Frame(root)
	frame.grid(row=0, column=0)
	def next(command):
		frame.grid_forget()
		command()
	Button(frame, text='Force on a charged particle', command = lambda: next(rhr_force)).grid(row = 0,column = 0, sticky = 'w')
	Button(frame, text='Magnetic field from a Current', command =lambda: next(rhr_wire)).grid(row = 1,column = 0, sticky = 'w')
	Button(frame, text='Induced current from a magnetic field', command =lambda: next(lenz_law)).grid(row = 2,column = 0, sticky = 'w')
		
	Separator(frame, style='TSeparator', orient='horizontal').grid(row=3, columnspan=2, sticky='ew')
	
	Button(frame, text='Constants', command=lambda: next(constants)).grid(row = 5, column = 0, sticky = 'w')
	Button(frame, text='Not memes', command=lambda: next(memes)).grid(row=6,column=0,sticky='w')
	
def memes():
	
	
	path = "memes"
	files = [f for f in listdir(path) if isfile(join(path, f))]
	frame=Frame(root)
	frame.grid(row=0,column=0)
	
	label=1	

	def setImage():
		global label
		try:
			label.grid_forget()
		except:
			pass
		
		randfile=files[randint(0,len(files)-1)]
		image=Image.open("memes/"+randfile)

		width,height=image.size
		if height>600:
			image=image.resize((width*3/4,height*3/4), Image.ANTIALIAS)
		photo=ImageTk.PhotoImage(image)
		

		label=Label(frame, image=photo)
		label.image=photo
		label.grid(row=0,column=0)

	setImage()
	def return_to_menu():
		frame.grid_forget()
		main()
	
	Button(frame, text = "Back to menu", command = lambda: return_to_menu()).grid(row=0, column=1, sticky='w')
	Button(frame, text= "Anotha One", command = setImage).grid(row=1,column=1,sticky='w')

def main():
	
	menu()
	
	root.mainloop()

if __name__=='__main__':
	main()

	

