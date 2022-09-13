#!/usr/bin/python3
from random import randrange, shuffle
import sys
import signal
import time
from os import system, name
from yachalk import chalk
import getpass

def sigint_handler(signal, frame):
	print("Programm beendet, takk")
	sys.exit(0)

def clear():
	# for windows
	if name == 'nt':
		_ = system('cls')
	# for mac and linux(here, os.name is 'posix')
	else:
		_ = system('clear')

def delete_last_lines(n=1):
	CURSOR_UP_ONE = "\x1b[1A"
	ERASE_LINE = "\x1b[2K"

	for _ in range(n):
		sys.stdout.write(CURSOR_UP_ONE) 
		sys.stdout.write(ERASE_LINE) 

def main():
	words = []

	signal.signal(signal.SIGINT, sigint_handler)

	currWord = ""
	lastInput = ""
	while True:
		eingabe = (input(chalk.blue("(add#[Wort], next, count, skip) ")))
		eingabeTxt = eingabe
		eingabe = eingabe.lower()
		if eingabe == "/exit" or eingabe == "/beenden":
			password = getpass.getpass()
			if password=="Klinger":
				print("Merci d'avoir joué")
				sys.exit()
			else:
				print(chalk.red("Passwort falsch, schlimm"))
		elif eingabe.startswith("add") or eingabe.startswith("hinzufügen"):
			lastInput = eingabe
			currWord = ""
			str_arr = eingabeTxt.split("#")
			if len(str_arr) != 2:
				print(chalk.red("Bitte Syntax einhalten"))
				continue
			if len(str_arr[1])==0:
				print(chalk.red("Bitte Syntax einhalten"))
				continue
			if str_arr[1] in words:
				delete_last_lines()
				print(chalk.red("Keine Dopplungen, Du Troll"))
				continue
			words.append(str_arr[1])
			time.sleep(1)
			print('\033[1A' + "Wort eingefügt" + '\033[K')
		elif eingabe == "show" or eingabe == "next" or eingabe == "nächste" or eingabe == "weiter":
			lastInput = eingabe
			lenArr = len(words)
			if lenArr == 0:
				print(chalk.red("Mögest Du mehr Wörter einpflegen. Takk"))
			else:
				i = randrange(0, lenArr)
				currWord = words[i]
				print(currWord)
				words.remove(words[i])
		elif eingabe == "count" or eingabe == "anzahl":
			currWord = ""
			lastInput = eingabe
			print("Es sind noch "+str(len(words))+" Wörter übrig.")
		elif (eingabe == "skip" or eingabe == "meins") and currWord != "":
			if lastInput not in ["next", "show", "nächste", "weiter"]:
				print(chalk.red("Du hast doch gar nichts zu überspringen, Troll"))
			else:
				words.append(currWord)
				delete_last_lines(2)
				currWord = ""
				lastInput = eingabe


if __name__ == "__main__":
	main()