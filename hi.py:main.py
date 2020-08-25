#!utf-8
#??hi.py

def say(word):
	print(word)
def ask(question):
	input(question)
def define(const, f, skipn=False, name):
	def inside_define():
		eval(f"{name} = const")
		f()
		if skipn:
			print(f"variable with name{name} was added succesiful!")
	return inside_define

def is_in32(value):
	if value > 2147483648:
		return False
	else:
		return True
def say_is_int32(value):
	if value > 2147483648:
		say("Is not in32!")
	else:
		say("Is in32!")


