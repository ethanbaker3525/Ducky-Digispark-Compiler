# PRINT DUCK

print("        ,----,\n   ___.`      `,\n   `---  D     :\n     `'.      .'\n        )    (                   ,\n       /      \_________________/|\n      /                          |\n     |                           ;\n     |               _____       /\n     |      \       ______7    ,'\n     |       \    ______7     /\n      \       `-,____7      ,'      \n^~^~^~^`\__________________/~^~^~^~^")
print("   ___  _      _ ____              __  \n  / _ \\(_)__ _(_) __/__  ___ _____/ /__\n / // / / _ `/ /\\ \\/ _ \/ _ `/ __/  '_/\n/____/_/\\_, /_/___/ .__/\_,_/_/ /_/\\_\\ \n       /___/     /_/                   ")
print("     ____                 __       \n    / __/__  _______  ___/ /__ ____\n   / _// _ \\/ __/ _ \\/ _  / -_) __/\n  /___/_//_/\\__/\\___/\\_,_/\\__/_/   \n                                   ")

# GET DUCKY SCRIPT

ducky_code.append(input('Paste in the ducky script that you wish to compile... '))

while 1:
	inp = input('')
	if inp != '':
		ducky_code.append(inp)
	else:
		break

# COMPILE THE SCRIPT

temp = []

for i in ducky_code:
	if i[:3] == 'GUI':
		temp.append(i.upper().replace('GUI ', 'DigiKeyboard.sendKeyStroke(KEY_') +',MOD_CMD_LEFT);')
	elif i[:3] == 'REM':
		temp.append(i.replace('REM ', '//'))
	elif i[:5] == 'DELAY':
		temp.append(i.replace('DELAY ', 'DigiKeyboard.delay(')+');')
	elif i[:6] == 'STRING':
		temp.append(i.replace('STRING ','DigiKeyboard.print("')+'");')
	elif i[:5] == 'ENTER':
		temp.append('DigiKeyboard.sendKeyStroke(KEY_ENTER);')
	else:
		raise Exception('Error, unexpected command on line: '+i)

# PRINT THE FINAL DIGISPARK COMPATABLE CODE

print('#include "DigiKeyboard.h"\n#define MOD_CMD_LEFT 0x00000008\nvoid setup() {\n  DigiKeyboard.sendKeyStroke(0);\n' + '\n'.join(temp) + '\n}\nvoid loop() {\n  digitalWrite(1, HIGH);\n  DigiKeyboard.delay(90000);\n}')
