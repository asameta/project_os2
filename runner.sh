cd /home/project_os2
sudo ./boot_time.sh &
sudo python3 set.py &  # setting user local interface parameters temp cpu
sudo ./update.sh &  # check network connection 30 times per 10 sec. reboot or run scriots

sudo  rm -r /home/exworx/.local &
sudo  rm -r /home/exworx/.cache &
sudo hwclock -w &
