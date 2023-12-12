#! usr/bin/bash
STR=$(cat /proc/cpuinfo | grep Serial | cut -d ' ' -f 2)
STR=$(echo $STR)
f="http://www.etkiplatform.com/""$STR"".zip"

# Basename : 'file'
    NAME_F=$(echo "$f" | awk '{gsub(/.*[/]|[.].*/, "", $0)} 1')
NAME_F=$(echo $NAME_F)

#VERSION_NEW=$(echo $NAME_F | tail -c 5)
#NAME_F=$(echo $NAME_F | rev | cut -c5- | rev)
#VERSION_NEW=$((VERSION_NEW))

# Basename-extended : 'file.1.0.1.tar'
  EXT_F=$(echo "$f" | awk '{gsub(/.*[/]|[.]{1}[^.]+$/, "", $0)} 1')
EXTENTION_F=$EXT_F
str1=$STR
str2=$NAME_F
echo $str1 $str2

if [ "$str1" = "$str2" ]; then
  cd /var/www/
  sudo wget --spider "$f" && sudo wget "$f" -O "$EXTENTION_F"
  status=$?
  if ! (exit $status); then
      echo "some_command failed"
  else
    yes | sudo unzip "$EXTENTION_F"
    sudo rm "$EXTENTION_F"
    sudo reboot
    echo "completed!"
  fi
else
  echo "This update is not for this module."
fi
