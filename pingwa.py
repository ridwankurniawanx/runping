from ping3 import ping
import os
import time
import requests
################
STD1_0="UP"
STD2_0="UP"
STD3_0="UP"
################

################

################
os.system("nmcli c down FASOPONLY_4G")
os.system("nmcli c up 'Wired connection 1'")
################
D1=ping("192.168.18.1", unit="ms")
D2=ping("192.168.18.30", unit="ms")
D3=ping("192.168.18.122", unit="ms")
################
def datatostatus(data):
    if data==False:
        status="FALSE"
        response="False"
        value=556.0
    elif data==None:
        status="DOWN"
        response="Timeout"
        value=555.0
    else:
        status="UP"
        response=round(data,1)
        value=round(data,1)
    return status,response,value
#################
STD1=datatostatus(D1)[0]
STD2=datatostatus(D2)[0]
STD3=datatostatus(D3)[0]
RSP1=datatostatus(D1)[1]
RSP2=datatostatus(D2)[1]
RSP3=datatostatus(D3)[1]
VAL1=datatostatus(D1)[2]
VAL2=datatostatus(D2)[2]
VAL3=datatostatus(D3)[2]
#################
print("kirimdata ke database")
#################
if (STD1!=STD1_0) or (STD2!=STD2_0) or (STD3!=STD3_0):
    os.system("nmcli c down 'Wired connection 1'")
    os.system("nmcli c up FASOPONLY_4G")
    print("kirim wa")
    print(str(STD1)+str(RSP1)+str(VAL1))
    print(str(STD2)+str(RSP2)+str(VAL2))
    print(str(STD3)+str(RSP3)+str(VAL3))
    url = "https://api.watsap.id/send-message";
    pesan= "_*GIXYZ ALERT!!!*_\n============\n```Router  "+STD1+"\nLaptop  "+STD2+"\nHP      "+STD3+"```"
    payload={'id_device' : '652', 'api-key' : '8803a77e3041cb5ca064790976c4dfbc6a3c1899', 'no_hp'  : '6285840292122', 'pesan'  : pesan}
    headers = {}
    response = requests.request("POST", url, headers=headers, data=payload)
    os.system("nmcli c down FASOPONLY_4G")
    os.system("nmcli c up 'Wired connection 1'")
    os.system("nmcli c s")
else:
    print("tidak kirim wa")

STD1_0=STD1
STD2_0=STD2
STD3_0=STD3

