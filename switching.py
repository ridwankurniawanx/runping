from ping3 import ping
import os
import time
import requests
################
STD1_0="UP"
STD2_0="UP"
STD3_0="UP"
################
os.system("nmcli c down FASOPONLY_4G")
################
D1=ping("192.168.18.1", unit="ms")
D1=ping("192.168.18.30", unit="ms")
D1=ping("192.168.18.122", unit="ms")
################
def datatostatus(data):
    if data==False:
        status="FALSE"
        response="False"
        value=556
    elif data==None:
        status="DOWN"
        response="Timeout"
        value=555
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
    os.system("nmcli c down FASOPONLY_4G")
    os.system("nmcli c up 'Wired connection 1'")
    os.system("nmcli c s")
else:
    print("tidak kirim wa")

STD1_0=STD1
STD2_0=STD2
STD3_0=STD3



# for i in range(5):
#   print("Cek koneksi awal")
#   os.system("nmcli c s") 
#   print("matikan wifi")
#   os.system("nmcli c down FASOPONLY_4G")
#   print("cek koneksi")
#   os.system("nmcli c s")
#   print(" wifi mati jalankan program")
#   D1=ping("192.168.8.1", unit="ms")
#   print(D1)
#   os.system("hostname -I")
#   print("dapat data,matikan lan lalu konek wifi")
#   os.system("nmcli c down 'Wired connection 1'")
#   os.system("nmcli c up FASOPONLY_4G")
#   print("cek koneksi lagi")
#   os.system("nmcli c s")
#   os.system("hostname -I")
#   print("setelah ok, kirim data ke wa")
#   print("kemudian matikan wifi terus konekan lan")
#   os.system("nmcli c down FASOPONLY_4G")
#   os.system("nmcli c up 'Wired connection 1'")
#   print("cek koneksi, lalu looping setelah 10 detik")
#   time.sleep(10)
