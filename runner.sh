cd /home
sudo ./etki_network.sh &
sudo python3 sender.py &
sudo ./boot_time.sh &
sudo ./update.sh &
sudo python3 set.py &
sudo sh nginx_manage.sh &
sudo  rm -r /home/exworx/.local &
sudo  rm -r /home/exworx/.cache &
sudo hwclock -w &
