import os
import email
import datetime
import random

# this script changes eml files names in directory, based on header title. script works in working directory
# new title format: date_email_title
# useful when windows CHKDSK and SCANDISK creates file00000C.chk like files on error (first of all change files extension from .chk to .eml)
# !!! you may want to create backup copy before using this script

n = 0
eml_files_count = 0
for f in os.listdir():
    if f[-4:] == '.eml':
        eml_files_count += 1

def print_status(n, count, new_file_name):
    status = str(n) + '/' + str(count) + '   ' + new_file_name
    print(status)

for f in os.listdir():
    if f[-4:] == '.eml':
        n += 1
        
        with open(f, encoding='utf-8', errors='ignore') as message:
            
            msg = email.message_from_file(message)
            #mail_subject = email.header.decode_header(msg['Subject'])[0]
            try:
                try:
                    # this is because some emails are not utf-8 encoded, so in this case it will decode it with iso-8859-2 instead of leaving this as byte object
                    mail_subject = email.header.decode_header(msg['Subject'])[0][0].decode(encoding='utf-8')
                except:
                    mail_subject = email.header.decode_header(msg['Subject'])[0][0].decode(encoding='iso-8859-2')
            
            except (UnicodeError, AttributeError, TypeError):
                # when subject is already string object
                mail_subject = msg['Subject']
                
            try:
                # sometimes email.header.decode_header(msg['From']) returns list of tuples like: [(b'from', 'utf-8'), (b' <from_email_address>', None)]
                
                mail_from = email.header.decode_header(msg['From'])[1][0].decode(encoding='utf-8')[2:][:-1]
            except IndexError:
                # and sometimes like: [('FROM <from_email_address>', None)]
                mail_from = email.header.decode_header(msg['From'])[0][0]

            mail_date = email.utils.parsedate_to_datetime(msg['Date']).strftime('%Y-%m-%d')


        if mail_subject is not None:
            # this line replaces multiple spaces with one space
            ' '.join(mail_subject.split())

            if len(mail_subject) > 64:
                # leaves 64 first chars
                mail_subject = mail_subject[0:64]

            new_title = mail_date + '__' + mail_from + '__' + mail_subject + '.eml'
        else:
            new_title = mail_date + '__' + mail_from + '.eml'

        # delete <, >, \, /, :, *, |, ", ?, \n, \r, \t characters from new file name as these will give [WinError 123] when trying to rename in Windows
        to_delete = '<>\/:*|"?\n\r\t'
        for ch in to_delete:
            new_title = new_title.replace(ch, '')
             
        try:
            os.rename(f, new_title)
            print_status(n, eml_files_count, new_title)

        except FileExistsError:
            # if while with given name already exists
            new_title = new_title[:-4] + str(n) + '.eml'
            os.rename(f, new_title)
            print_status(n, eml_files_count, new_title)

