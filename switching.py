from ping3 import ping
import os
import time
for i in range(5):
  print("Cek koneksi awal")
  os.system("nmcli c s") 
  print("matikan wifi")
  os.system("nmcli c down FASOPONLY_4G")
  print("cek koneksi")
  os.system("nmcli c s")
  print(" wifi mati jalankan program")
  D1=ping("192.168.8.1", unit="ms")
  print(D1)
  os.system("hostname -I")
  print("dapat data,matikan lan lalu konek wifi")
  os.system("nmcli c down 'Wired connection 1'")
  os.system("nmcli c up FASOPONLY_4G")
  print("cek koneksi lagi")
  os.system("nmcli c s")
  os.system("hostname -I")
  print("setelah ok, kirim data ke wa")
  print("kemudian matikan wifi terus konekan lan")
  os.system("nmcli c down FASOPONLY_4G")
  os.system("nmcli c up 'Wired connection 1'")
  print("cek koneksi, lalu looping setelah 10 detik")
  time.sleep(10)
  
