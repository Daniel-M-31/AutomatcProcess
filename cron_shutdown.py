import subprocess as sp

red = '\033[0;31m'
green = '\033[0;32m'
blue = '\033[0;34m'
wellow = '\033[0;33m'
rst = '\033[0m'

def cron(h, m):
    cmand = f"{m} {h} * * * /sbin/shutdown -h now\n"

    try:
        #Search programmed tasks
        sch = sp.run(['sudo', 'crontab', '-l'], capture_output=True, text=True)

        pgd_tks = sch.stdout if sch.returncode ==0 else ''

        if cmand in pgd_tks:
            print(f'{red}[!] Task already exists \n')
            return
        if pgd_tks and not pgd_tks.endswith('\n'):
            pgd_tks += '\n'

        upt_tsks = pgd_tks + cmand

        #Task executor
        prss = sp.Popen(['sudo', 'crontab', '-'], stdin=sp.PIPE)
        prss.communicate(input=upt_tsks.encode())

        print(f'{green}[OK] Shutdown scheduled: {blue}{h}:{m}\n')

    except:
        print(f"{red}[!] Unexpected error occurred")


def lst():
    tsk = ['', '']

    try:
        sch = sp.run(['sudo', 'crontab', '-l'], capture_output=True, text=True)

        for i in sch.stdout:
            if i.isnumeric():
                if len(tsk[1])<2:
                    tsk[1] += i
                else: tsk[0] += i

                if len(tsk[1])==2 and len(tsk[0])==2:
                    print(f'{blue}#Shutdown set for {wellow}{tsk[0]}:{tsk[1]}\n')

            if i == '\n':
                tsk = ['', '']

    except:
        print(f'{red}[!] Unexpected error occurred')


def del_tsk():
    tsk = str(input(f'{wellow}[R]{blue} Reset all tasks {wellow}[Q]{blue} Quit  |  Enter {wellow}HH:MM{blue} to disable{rst} ')).strip()
    if not tsk.isalpha():
        dltsk = tsk.replace(':', ' ').split()
        dltsk.reverse()
        dltsk = ' '.join(dltsk)

    elif tsk != '':
        dltsk = tsk

    else:
        return

    if dltsk == 'q' or dltsk == 'Q':
        return
    try:

        sch = sp.run(['sudo', 'crontab', '-l'], capture_output=True, text=True)
        tks = sch.stdout.splitlines() if sch.stdout else ''

        if dltsk == 'R' or dltsk == 'r':
            if not any(' * * * /sbin/shutdown -h now' in i for i in tks):
                return print(f'{red}[!] All tasks have been removed\n')

            for i in range(0, len(tks)):
                if sch.stdout and f'* * * /sbin/shutdown -h now' in tks[(i - 1)]:
                    tks[i - 1] = ''

        else:
            if not f'{dltsk} * * * /sbin/shutdown -h now' in tks:
                return print(f'{red}[!] Task not found\n')

            for i in tks:
                if sch.stdout and f'{dltsk} * * * /sbin/shutdown -h now' in i:
                    tks.remove(i)
                    break


        upt_tks = '\n'.join(tks)+'\n'


        prss = sp.Popen(['sudo', 'crontab', '-'], stdin=sp.PIPE)
        prss.communicate(input=upt_tks.encode())

        print(f'{green}[OK] Shutdown removed successfully\n')
        lst()

    except:
            print(f"{red}[!] Unexpected error occurred\n")
