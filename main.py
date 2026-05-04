import cron_shutdown as cs
while True:
    inp = str(input('[H] Shutdown Menu  [Q] Quit '))

    if inp == 'q' or inp == 'Q':
        break
    elif inp == 'H' or inp == 'h':

        while True:
            inp = str(input('[H] Set Routine  [L] List Routines  [Q] Quit '))

            if inp == 'L' or inp == 'l':

                while True:
                    cs.lst()
                    inp = str(input('[D] Delete Routine  [Q] Quit '))
                    if inp == 'Q' or inp == 'q':
                        break
                    elif inp == 'D' or inp == 'd':
                        cs.del_tsk()
                        break

            elif inp == 'Q' or inp == 'q':
                break

            elif inp == 'H' or inp == 'h':

                while True:
                    HS = str(input('Set shutdown time (ex 17:30) or [Q] Quit ')).strip()

                    if HS == 'q' or HS == 'Q':
                        break
                    elif HS[0].isnumeric() and int(HS[0])<3 and HS[1].isnumeric() and HS[2]==':' and HS[3].isnumeric() and int(HS[3])<6 and HS[4].isnumeric() and len(HS) == 5:
                        H = HS[0:2]
                        M = HS[3:5]

                        while True:
                            cs.cron(H, M)
                            break

                    else:
                        print('[!] Invalid format')