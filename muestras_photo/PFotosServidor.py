import paramiko

proxy = None
client = paramiko.SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('10.0.5.246', username='lmv-codedata', password='Laboratorio', sock=proxy)

ftp_client = client.open_sftp()
ftp_client.put('2019-09-13_0952.jpg', '/var/www/html/ENTRADA-LMV/Images_Access/2019-09-13_0952.jpg')
ftp_client.close()
