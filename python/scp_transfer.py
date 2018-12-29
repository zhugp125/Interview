#!/bin/env python3
# coding: utf-8

import paramiko
import os
import sys
import time

def create_sftp(host, port, user, pwd):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port, user, pwd)
    
    paramiko.SFTPClient.from_transport(ssh.get_transport())
    return ssh, ssh.open_sftp()

def sftp_upload(sftp, local_file, remote_dir):
    if not os.path.exsits(local_file):
        print('%1 not exists' % local_file)
        return
        
    file = os.path.split(local_file)[1]
    remote_file = os.path.join(remote_dir, file)
    sftp.put(local_file, remote_file)
    
def sftp_download(sftp, local_file, remote_file):
    if os.path.exsits(local_file):
        print('%1 exists' % local_file)
        os.system('copy "' + local_file + '" "' + local_file + ".bak" + '"')
        
    sftp.get(remote_file, local_file)
    
def main():
    cf = configparser.ConfigParser()
    cf.read('config.ini')

    host = '172.30.84.3'
    port = 22
    user = 'root'
    pwd = 'password'
    ssh, sftp = create_sftp(host, port, user, pwd)
    
    local_file = ''
    remote_file = ''
    sftp_upload(sftp, local_file, remote_file)
    
    ssh.close()
    
if __name__ == '__main__':
    main()