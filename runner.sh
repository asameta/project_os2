cd /home/project_os2
sudo ./boot_time.sh &
sudo python set.py &  # setting user local interface parameters temp cpu
sudo ./update.sh &  # check network connection 30 times per 10 sec. reboot or run scriots
sudo sh nginx_manage.sh &   # attempt to open local interface

sudo  rm -r /home/exworx/.local &
sudo  rm -r /home/exworx/.cache &
sudo hwclock -w &
sudo systemd-tmpfiles --clean;sudo systemd-tmpfiles --remove;sudo apt clean;sudo journalctl --vacuum-size=1M
