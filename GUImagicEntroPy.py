#cols	 |	0	|	1	|	2	|
#rows	0|	banner		banner		banner
#	1| chars in Str	|Generate variab| amount output |
#	2|   Combobox	|   Combobox	|   Combobox	|
#	3|	<--	 Generate Button	-->
#	4|		by DevMen
#	5|	<--	     Outputs		-->

"""
this GUI is funcional but don't copy the output...I work in that
"""

import random
from tkinter import *
from tkinter import ttk

ABC		= 'abcdefghijklmnñopqrstuvwxyz'	#<-- for change the letters
SIMBOLS		= '¡?=)(/&%$#"!°|*[]-_,;.'	#<-- for change the simbols
VOWELS		= "aeiou"			#<-- for vowels in name
CONSONANTS	= "bcdfghjklmnpqrstvwxyz"	#<-- for consonants in name

def genPass(largo):
	generated = ''
	for letra in range(0, largo):
		var = random.randrange(3)
		if 0 == var:
			generated += ABC[random.randrange(26)]
		elif 1 == var:
			generated += ABC[random.randrange(26)].upper()
		else:
			generated += str(random.randrange(9))
	salida["text"] += "\n"+generated

def genStrongPass(largo):
	generated = ''
	for letra in range(0, largo):
		var = random.randrange(4)
		if 0 == var:
			generated += ABC[random.randrange(26)]
		elif 1 == var:
			generated += ABC[random.randrange(26)].upper()
		elif 2 == var:
			generated += SIMBOLS[random.randrange(21)]
		else:
			generated += str(random.randrange(9))
	salida["text"] += "\n"+generated

def genName(largo):
	if largo > 1:
		n = int(largo/2)
	else:
		n = largo
	name = ""

	for i in range(n): # silabas
		name += CONSONANTS[random.randint(0,len(CONSONANTS)-1)]
		name += VOWELS[random.randint(0,len(VOWELS)-1)]
		if largo%2 == 1 and largo != 1 :
			name += CONSONANTS[random.randint(0,len(CONSONANTS)-1)]
	salida["text"] += "\n"+name[:largo]

def pressButton():
        salida["text"] = ""
        if comboGen.get() == 'all':
                salida["text"] += '=====|Passwords|======='
                for e in range(int(comboOut.get())):genPass(int(comboChars.get())) #en revision
                salida["text"] += '\n======================\n'
                salida["text"] += '==|Strong Passwords|==='
                for e in range(int(comboOut.get())):genStrongPass(int(comboChars.get()))
                salida["text"] += '\n======================\n'
                salida["text"] += '=====|User Names|======'
                for e in range(int(comboOut.get())):genName(int(comboChars.get()))
        elif comboGen.get() == "name":
                for e in range(int(comboOut.get())):genName(int(comboChars.get()))
        elif comboGen.get() == "pass":
                for e in range(int(comboOut.get())):genPass(int(comboChars.get()))
        if comboGen.get() == "strong Pass":
                for e in range(int(comboOut.get())):genStrongPass(int(comboChars.get()))

ventanaRaiz = Tk()
ventanaRaiz.title("Combobox con Tkinter")
ventanaRaiz.resizable(False, False)

# Row 0 here
bannerText =  """
MagicEntroPy
"""
banner = Label(ventanaRaiz, text=bannerText,
	font="Times 23 italic", bg = "red").grid(
		column=0, row=0,columnspan=3,sticky="nswe")
# Row 1 here
labChars = Label(ventanaRaiz, text="chars in string",width=20, height=3).grid(column=0, row=1)
labGenerate = Label(ventanaRaiz, text="generate", width=20, height=3).grid(column=1,row=1)
labAmount = Label(ventanaRaiz, text="amount of output", width=20, height=3).grid(column=2,row=1)

# Row 2 here
comboChars = ttk.Combobox(ventanaRaiz, values=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], width=5)
comboChars.current(2)
comboChars.grid(column=0, row=2)
comboGen = ttk.Combobox(ventanaRaiz, values=["all", 'name','pass','strong Pass'], width=5)
comboGen.current(0)
comboGen.grid(column=1, row=2)
comboOut = ttk.Combobox(ventanaRaiz, values=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], width=5)
comboOut.current(5)
comboOut.grid(column=2, row=2)

# Row 3 here
bot = Button(ventanaRaiz, text="generate", font=" , 10", command=pressButton).grid(column=0, row=3,columnspan=3,sticky="nsew",pady=23)

# Row 4 here
byDev ='--> by DevelopmentMen <--'
byDevLab = Label(ventanaRaiz, text=byDev, font="Helvetica 10 italic").grid(column=1,row=4,pady=6)

# Row 5 here
#salida = Label(ventanaRaiz, text="Press Generate Button")
salida = Label(ventanaRaiz,text="Press generate button to Magic")
salida.grid(column=0, row=5, columnspan=3)


ventanaRaiz.mainloop()
