#!/bin/env python3
# coding: utf-8

import ftplib

def ftp_download(ftp, remote_file, local_file):
    with open(local_file, 'wb') as f:
        ftp.retrbinary('RETR %s' % remote_file, f.write)

def ftp_upload(ftp, remote_file, local_file):
    with open(local_file, 'rb') as f:
        ftp.storbinary('STOP %s' % remote_file, f)

def main():
    ftp = ftplib.FTP(host='192.168.1.131', user='root', passwd='suse.vm.131')
    # upload
    ftp_upload(ftp, 'remote_file', 'local_file')

    # quit ftp server
    ftp.quit()
    
if __name__ == '__main__':
    main()