#!/bin/sh
while true; do

        ping -I ppp0 -c 1 8.8.8.8

        if [ $? -eq 0 ]; then
                echo "Connection up and running"
        else
                echo "No Connection"
                systemctl daemon-reload
                systemctl enable ppp-default ;systemctl enable quectel;
                systemctl restart ppp-default;systemctl restart quectel
        fi

        sleep 15
done