import subprocess as sp


def cron(h, m):
    cmand = f"{m} {h} * * * /sbin/shutdown -h now\n"

    try:
        #Search programmed tasks
        sch = sp.run(['sudo', 'crontab', '-l'], capture_output=True, text=True)

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

    try:
        sch = sp.run(['sudo', 'crontab', '-l'], capture_output=True, text=True)

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
        print(f'[!] Unexpected error occurred')


def del_tsk():
    tsk = str(input('[R] Reset all tasks [Q] Quit  |  Enter HH:MM to disable '))

    if not tsk.isalpha():
        dltsk = tsk.replace(':', ' ').split()
        dltsk.reverse()
        dltsk = ' '.join(dltsk)

    else:
        dltsk = tsk

    if dltsk != 'q' or dltsk != 'Q':
        try:
            sch = sp.run(['sudo', 'crontab', '-l'], capture_output=True, text=True)
            tks = sch.stdout.splitlines() if sch.stdout else ''

            if dltsk != 'R' and dltsk != 'r':

                for i in tks:

                    if sch.stdout and f'{dltsk} * * * /sbin/shutdown -h now' in i:
                        tks.remove(i)
                        break
            else:
                for i in range(0, len(tks)):
                    if sch.stdout and f'* * * /sbin/shutdown -h now' in tks[(i-1)]:
                        tks[i-1] = ''

            upt_tks = '\n'.join(tks)+'\n'


            prss = sp.Popen(['sudo', 'crontab', '-'], stdin=sp.PIPE)
            prss.communicate(input=upt_tks.encode())

            print('[OK] Shutdown removed successfully')
            lst()

        except:
            print(f"[!] Unexpected error occurred")

    else: return