import os

import time


with open('hosts&ips') as file:
    dump = file.read()

    dump = dump.splitlines()

    for ip in dump:
        print('verificando in dump:', ip)
        print("#" * 100)
        os.system('ping -n 2 {}'.format(ip))
        print("#" * 100)
        time.sleep(5)

