while [ 0 ]
do

 if [ $(sudo ifconfig eth0 | grep -E -o 'inet [0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}'  | cut -d' ' -f2) ];
 then
    if [ $(sudo systemctl status nginx | grep Active |cut -d":" -f2 |cut -d" " -f2) -eq "failed" ];
    then
      sudo systemctl restart nginx
    else
      break
    fi
 fi
done
