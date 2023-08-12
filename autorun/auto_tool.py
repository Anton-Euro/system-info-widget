import os

print('''
1 - set autorun task
2 - delete autorun task
''')

while True:
    mode = input('enter the mode number: ')
    if mode == '1' or mode == '2':
        break

if mode == '1':
    query = f'schtasks /create /tn desktop_widget /tr "{os.getcwd()}\\run.vbs" /sc ONLOGON /rl HIGHEST'

    bat_dir = '\\'.join(os.getcwd().split('\\')[:-1])

    with open('run.bat', 'w') as f:
        f.write(f'cd /d "{bat_dir}"\nstart {bat_dir}\\systeminfowidget.exe')
    
    with open('run.vbs', 'w') as f:
        f.write(f'Set objShell = WScript.CreateObject("WScript.Shell")\nobjShell.Run("{os.getcwd()}\\run.bat"), 0, True')

    os.system(query)
else:
    query = 'schtasks /delete /tn desktop_widget'

    os.system(query)

input('press enter to exit')