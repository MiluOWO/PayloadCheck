import re

def IpExtract(info):
    return re.findall(r'(?:\d{1,3}\.){3}\d{1,3}',info[:16])[0]

def CheckPayload(record,payload):
    for i in payload:
        if (i in record):
            return IpExtract(record)
    return 0

def ReadLog(filename,payload):
    CorrectIp =set()
    with open(filename,'r') as f:
        record = f.readlines()
    for i in record:
        a = CheckPayload(i,payload)
        if(a):
            CorrectIp.add(a)
    return CorrectIp
payload = {'GET /admin/admin.php?file=1.zip','GET /admin/admin.php?file=1.zip/shell.php','GET /admin/admin.php?file=phar://1.zip/shell.php'}

print(str(ReadLog('access.log',payload)))

