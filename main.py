import cron_shutdown as cs
while True:
    inp = str(input(f'{cs.wellow}[H]{cs.blue} Shutdown Menu  {cs.wellow}[Q]{cs.blue} Quit{cs.rst} '))

    if inp == 'q' or inp == 'Q':
        break
    elif inp == 'H' or inp == 'h':

        while True:
            inp = str(input(f'{cs.wellow}[H]{cs.blue} Set Routine  {cs.wellow}[L]{cs.blue} List Routines  {cs.wellow}[Q]{cs.blue} Quit{cs.rst} '))

            if inp == 'L' or inp == 'l':

                while True:
                    print('')
                    cs.lst()
                    inp = str(input(f'{cs.wellow}[D]{cs.blue} Delete Routine  {cs.wellow}[Q]{cs.blue} Quit{cs.rst} '))
                    if inp == 'Q' or inp == 'q':
                        break
                    elif inp == 'D' or inp == 'd':
                        cs.del_tsk()
                        break

            elif inp == 'Q' or inp == 'q':
                break

            elif inp == 'H' or inp == 'h':

                while True:
                    HS = str(input(f'{cs.blue}Set shutdown time ({cs.wellow}ex 17:30{cs.blue}) or {cs.wellow}[Q]{cs.blue} Quit{cs.rst} ')).strip()

                    if HS == 'q' or HS == 'Q':
                        break
                    elif HS[0].isnumeric() and int(HS[0])<3 and HS[1].isnumeric() and HS[2]==':' and HS[3].isnumeric() and int(HS[3])<6 and HS[4].isnumeric() and len(HS) == 5:
                        H = HS[0:2]
                        M = HS[3:5]

                        while True:
                            cs.cron(H, M)
                            break

                    else:
                        print(f'{cs.red}[!] Invalid format\n')
