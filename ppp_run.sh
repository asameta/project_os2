apt install ppp
cd /etc/ppp/peers
wget https://raw.githubusercontent.com/Quectel-Community/meta-quectel-community/master/recipes-quectel-community/quectel-ppp/quectel-ppp-0.1/quectel-ppp
wget https://raw.githubusercontent.com/Quectel-Community/meta-quectel-community/master/recipes-quectel-community/quectel-ppp/quectel-ppp-0.1/quectel-chat-disconnect
wget https://raw.githubusercontent.com/Quectel-Community/meta-quectel-community/master/recipes-quectel-community/quectel-ppp/quectel-ppp-0.1/quectel-chat-connect

echo "[Unit]
  Description=Quectel UC-20 3G Internet
  After=multi-user.target
[Service]
  ExecStart=/sbin/pppd call quectel-ppp
  User=root
  Restart=always
[Install]
  WantedBy=multi-user.target">/etc/systemd/system/quectel.service;

echo "[Unit]
Description=Add route ppp0
Before=quectel.service
[Service]
ExecStart=/sbin/route add default ppp0
User=root
Restart=on-failure
RestartSec=5s
[Install]
WantedBy=multi-user.target">/etc/systemd/system/ppp-default.service;

systemctl enable ppp-default
systemctl enable quectel
systemctl restart ppp-default
systemctl restart quectel
