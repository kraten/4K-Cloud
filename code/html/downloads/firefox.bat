cd C:\Program Files\VcXsrv
xlaunch.exe -run config.xlau
cd C:\Program Files\PuTTY
putty.exe -X -C -ssh root@192.168.43.98 1235 -pw q -m test.txt