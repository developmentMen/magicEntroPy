#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================
# Author	--> devMen
# Date created	--> 01/04/2021
# Last modified	--> 02/04/2021 <-- UPDATE HERE
# Version	--> Python 3.8.5
# =============================
'''
	| magicEntroPy |
 este programa fue echo para crear
 de manera aleatoria nombres y constraseñas

 this program was made to create random
 users and passwords
'''
# =============================
# Imports
import random
import argparse
# =============================
ABC='abcdefghijklmnñopqrstuvwxyz'	#<-- for change the letters
SIMBOLS = '¡?=)(/&%$#"!°|*[]-_,;.'	#<-- for change the simbols
VOWELS = "aeiou"			#<-- for vowels in name
CONSONANTS = "bcdfghjklmnpqrstvwxyz"	#<-- for consonants in name

def banner():
	return """
                   _       _______                       ______       
                  (_)     (_______)       _             (_____ \      
 ____  _____  ____ _  ____ _____   ____ _| |_  ____ ___  _____) )   _ 
|    \(____ |/ _  | |/ ___)  ___) |  _ (_   _)/ ___) _ \|  ____/ | | |
| | | / ___ ( (_| | ( (___| |_____| | | || |_| |  | |_| | |    | |_| |
|_|_|_\_____|\___ |_|\____)_______)_| |_| \__)_|   \___/|_|     \__  |
            (_____|                                            (____/ 
==================================================> by ☆ developmentMen☆
"""

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
	return(generated)

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
	return(generated)

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
	return(name[:largo])

def main(chars, generateType, numbers):
        prePrint = " --> "
        if generateType == 'all':
                print('=====|Passwords|=======')
                for e in range(numbers):print(prePrint+genPass(chars))
                print('======================>\n')
                print('==|Strong Passwords|===')
                for e in range(numbers):print(prePrint+genStrongPass(chars))
                print('======================>\n')
                print('=====|User Names|======')
                for e in range(numbers):print(prePrint+genName(chars))
        elif generateType == "name" or generateType == "n":
                for e in range(numbers):print(prePrint+genName(chars))
        elif generateType == "pass" or generateType == "p":
                for e in range(numbers):print(prePrint+genPass(chars))
        elif generateType == "spass" or generateType == "s":
                for e in range(numbers):print(prePrint+genStrongPass(chars))
        else:
                print("invalid generate parameter")
                print("""use:	\n\tfor username --> n or name \n
	for password --> p or pass \n
	for strong pass --> s or spass""")

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="generate random user and pass")
	parser.add_argument(
		'-c', '--chars', type=int, required=True,
		help="nums of chars in string")
	parser.add_argument(
		'-g', '--generate', type=str, default='all',
		help="generate name|pass|strongPass ---> n | p | s")
	parser.add_argument(
		'-n', '--numbers', type=int, default=3,
		help="amount of generated names or passwords")
	group = parser.add_mutually_exclusive_group()
	group.add_argument('-nb', '--noBanner', action='store_true', help='no print banner')
	args = parser.parse_args()
	if not args.noBanner: print(banner())
	main(args.chars, args.generate, args.numbers)
