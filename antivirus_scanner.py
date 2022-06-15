# -*- coding: utf-8 -*-
# @Author : Threekiii
# @Time : 2022/5/27 19:40
# @Function: kill soft process detection

import re
import os
import subprocess

def banner():
    print('+-------------------------------------------------------- ----')
    print('+ \033[36m@Function: Anti-software process detection \033[0m')
    print('+ \033[36m@Author : Threekiii \033[0m')
    print('+ \033[31m The code is for learning only, no one may use it for illegal purposes, otherwise the consequences will be borne by oneself. \033[0m')
    print('+-------------------------------------------------------- ----')

def check():
    antivirus_list = []
    with open('process.txt', 'r', encoding='utf-8') as f:
        content = f.readlines()
    try:
        print('+ \033[34m is executing tasklist command, current path: {}\033[0m'.format(os.path.abspath(os.path.dirname(__file__))))
        tmp = subprocess.check_output('tasklist', shell=True).decode()
        tasklist = ''.join(re.findall('.*=(.*)', tmp, re.S)).strip().split('\r\n')
        print('+ \033[34m is performing anti-software process detection...\033[0m')
        for task in tasklist:
            taskname = task.split()[0]
            for process in content:
                processname = process.strip('\n').split('\"')[1]
                if taskname == processname:
                    result = process.strip('\n').split('\"')[3]
                    antivirus_list.append('+ \033[31m process: {}, corresponding to antivirus: {}\033[0m'.format(processname, result))
        print('\n+ \033[31m[Check completed] \033[0m')
        for al in antivirus_list:
            print(al)
    except Exception as e:
        print('\n+ \033[31m[Exception] {}\033[0m'.format(e))

def run():
    banner()
    check()

if __name__ == '__main__':
    run()
