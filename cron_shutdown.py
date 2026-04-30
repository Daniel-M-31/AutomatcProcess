import subprocess as sp

def cron(h, m):
    cmand = f"{m} {h} * * * /sbin/shutdown -h now\n"

    try:
        #Search programmed tasks
        sch = sp.run(['contrab', '-l'], capture_output=True, text=True)
        pgd_tks = sch.stdout if sch.returncode else ''


        prss = sp.Popen(['crontab', '-'], stdin=sp.PIPE)
        prss.communicate(input=cmand.encode())

    except:
        print(f"{Exception()}")