#!/bin/bash

STATE2=1
cd /home/project_os2

while true; do
  cd /home/project_os2
  check_online(){
    netcat -z -w 5 8.8.8.8 53 && echo 1 || echo 0
  }

  # Initial check to see if we are online
  IS_ONLINE=$(check_online)
  # How many times we should check if we're online - this prevents infinite looping
  MAX_CHECKS=60
  # Initial starting value for checks
  CHECKS=0

#  declare -i
  # Loop while we're not online.
  while [ $IS_ONLINE -eq 0 ];
  do
    STATE2=1
    # We're offline. Sleep for a bit, then check again
    #echo  network_equal_0
    sleep 10;
    sudo hwclock -s
    IS_ONLINE=$(check_online)

    CHECKS=$[ $CHECKS + 1 ]
    if [ $CHECKS -gt $MAX_CHECKS ]; then
        #echo manytimes_tested_no_proper_network
        sudo hwclock -s
        sudo reboot
        break
    fi
  done

#  if [ $IS_ONLINE -eq 0 ]; then
#    # We never were able to get online. Kill script.
#    #echo many_attempt_to_test
#    sudo reboot
#    exit 1
#  fi

  if [ $STATE2 -eq 1 ]; then
    while [ $IS_ONLINE -eq 1 ]; do
        STATE2=0
        cd /home/exworx/project_os2

        sudo git fetch
        sudo git merge

        sudo systemctl restart nginx &

        # Restart upEtki.py
        sudo pkill -f "python /home/project_os2/upEtki.py"
        sudo python /home/project_os2/upEtki.py &

        # Restart sender.py
        if pgrep -f "python /home/project_os2/sender.py" > /dev/null; then
            echo "sender.py is running. Restarting..."
            sudo pkill -f "python /home/project_os2/sender.py"
        fi
        sudo python /home/project_os2/sender.py &  # Data sender to cloud

        break
        echo "all_clear"
    done
  fi
  sleep 20

done
