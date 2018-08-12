DISM /online /enable-feature /featurename:ServicesForNFS-ClientOnly
DISM /online /enable-feature /featurename:ClientForNFS-Infrastructure
mount     \\192.168.43.98\wshare\newuser     z: