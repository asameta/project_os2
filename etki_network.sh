while [ 0 ]
do
    sudo pppd call quectel-ppp>/home/project_os2/logs/quectel.log 2>&1
    sudo killall -0 pppd
    sudo route del default
    sudo route add default ppp0
    sleep 30
done
