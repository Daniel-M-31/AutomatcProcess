import subprocess as sp
import getpass as gp


def cron(h, m):
    cmand = f"{m} {h} * * * /sbin/shutdown -h now\n"
    pswd = gp.getpass('Enter sudo password: ')

    try:
        #Search programmed tasks
        sch = sp.run(['sudo', '-S', 'crontab', '-l'], input=(pswd+'\n'), capture_output=True, text=True)
        del pswd
        pgd_tks = sch.stdout if sch.returncode ==0 else ''

        if cmand in pgd_tks:
            print('[!] Task already exists')
            return
        if pgd_tks and not pgd_tks.endswith('\n'):
            pgd_tks += '\n'

        upt_tsks = pgd_tks + cmand

        #Task executor
        prss = sp.Popen(['sudo', 'crontab', '-'], stdin=sp.PIPE)
        prss.communicate(input=upt_tsks.encode())

        print(f'[OK] Shutdown scheduled: {h}:{m}]\n\n')

    except:
        print(f"[!] Unexpected error occurred")


def lst():
    tsk = ['', '']
    pswd = gp.getpass('Enter sudo password: ')
    try:
        sch = sp.run(['sudo', '-S', 'crontab', '-l'], input=(pswd + '\n'), capture_output=True, text=True)
        del pswd

        for i in sch.stdout:
            if i.isnumeric():
                if len(tsk[1])<2:
                    tsk[1] += i
                else: tsk[0] += i

                if len(tsk[1])==2 and len(tsk[0])==2:
                    print(f'#Shutdown set for {tsk[0]}:{tsk[1]}\n')

            if i == '\n':
                tsk = ['', '']

    except:
        print(f"[!] Unexpected error occurred")


def del_tsk():
    tsk = str(input('[R] Reset all tasks [Q] Quit  |  Enter HH:MM to disable '))

    if not tsk.isalpha():
        dltsk = tsk.replace(':', ' ').split()
        dltsk.reverse()
        dltsk = ' '.join(dltsk)

    try:
        sch = sp.run(['sudo', 'crontab', '-l'], capture_output=True, text=True)
        tks = sch.stdout.splitlines() if sch.stdout else ''

        if tsk != 'R' and tsk != 'r':

            for i in tks:

                if sch.stdout and f'{dltsk} * * * /sbin/shutdown -h now' in i  :
                    tks.remove(i)
                    break

            upt_tks = '\n'.join(tks)+'\n'


            prss = sp.Popen(['sudo', 'crontab', '-'], stdin=sp.PIPE)
            prss.communicate(input=upt_tks.encode())

            print('[OK] shutdown remove')
            lst()

    except:
        print(f"[!] Unexpected error occurred")