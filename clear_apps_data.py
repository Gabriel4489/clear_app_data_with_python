import os
from time import sleep

lists = []

def delete_cache():
	try:
		os.system("adb shell ls > validate.txt")
	except Exception as e:
		print(e)

	file = open("validate.txt")

	for i in file:
		if "storage":
			os.system("cls")
			print("your read to use this tool")
			print()

			os.system("adb shell pm list packages > all_packages.txt")

			for i in open("all_packages.txt"):
				#sleep(0.02)
				i = i.replace("package:","")
				lists.append(i.strip())
			#print(lists)
			s = 0
			for iterm in lists:
				print(str(s) + ": clear cache for " + iterm)
				os.system("adb shell pm clear " + iterm)
				s = s + 1

			print("your phone might have a lot of space by now")
			print("all work is done")
			print("thank you for using me!")
			print("exiting...")
			exit(0)

	print("your not capable of using this tool, please consider app requirements")
	exit(1)

validate = input("do you really want to delete all your app caches?(y/n): ").lower()

if validate == 'y':
	delete_cache()
elif validate == 'n':
	print("ok exiting...")
	exit(0)
else:
	print("invalid choice")
