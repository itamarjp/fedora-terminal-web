import tempfile
import os
import time

cmd = 'dnf --installroot={} -y install @minimal-environment passwd --releasever=32'
systemd = 'systemd-nspawn -bD {} --private-network --network-bridge=virbr0'
passwd_d = 'chroot {} passwd -d root'
networkd = 'chroot {} systemctl enable systemd-networkd'

def finaliza(tempo):
    for x in range(tempo):
      print('por favor feche o navegador/aba')
      time.sleep(1)


with tempfile.TemporaryDirectory(dir = '/var/lib/machines') as tmpdirname:
   print('created temporary directory', tmpdirname)
   print (cmd.format(tmpdirname))
   os.system(cmd.format(tmpdirname))
   print (passwd_d.format(tmpdirname))
   os.system(passwd_d.format(tmpdirname))
   print (networkd.format(tmpdirname))
   os.system(networkd.format(tmpdirname))
   print (systemd.format(tmpdirname))
   os.system(systemd.format(tmpdirname))

finaliza(1000)
