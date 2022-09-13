#!/usr/bin/python3
from random import randrange, shuffle
import sys
import signal
import time
from os import system, name

words = []

dictionary = {"close": "Programm beendet, takk",
				"exit": "/beenden",
				"wrongsyntax": "Bitte Syntax einhalten",
				"emptylist": "Mögest Du mehr Wörter einpflegen. Takk",
				"add": "hinzufügen"}


def sigint_handler(signal, frame):
	print(dictionary["close"])
	sys.exit(0)

def clear():
	# for windows
	if name == 'nt':
		_ = system('cls')
	# for mac and linux(here, os.name is 'posix')
	else:
		_ = system('clear')

signal.signal(signal.SIGINT, sigint_handler)

currWord = ""

while True:
	eingabe = (input("(add#[Wort], next, count, mine) "))
	eingabeTxt = eingabe
	eingabe = eingabe.lower()
	if eingabe == dictionary["exit"]:
		sys.exit()

	elif eingabe.startswith("add") or eingabe.startswith("hinzufügen"):
		currWord = ""
		str_arr = eingabeTxt.split("#")
		if len(str_arr) != 2:
			print(dictionary["wrongsyntax"])
			continue
		if len(str_arr[1])==0:
			print(dictionary["wrongsyntax"])
			continue
		words.append(str_arr[1])
		time.sleep(1)
		print ("\033[1A" + "Wort eingefügt" + "\033[K")

	elif eingabe == "show" or eingabe == "next" or eingabe == "nächste" or eingabe == "weiter":
		lenArr = len(words)
		if lenArr == 0:
			print(dictionary["emptylist"])
		else:
			i = randrange(0, lenArr)
			currWord = words[i]
			print(currWord)
			words.remove(words[i])

	elif eingabe == "count" or eingabe == "anzahl":
		currWord = ""
		print("Es sind noch "+str(len(words))+" Wörter übrig.")

	elif (eingabe == "mine" or eingabe == "meins") and currWord != "":
		words.append(currWord)
		print("Wort übersprungen")
		currWord = ""





