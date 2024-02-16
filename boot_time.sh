if test -f /home/project_os2/logs; then
  cd /home/project_os2/logs
else
  sudo mkdir /home/project_os2/logs
fi

cd /home/project_os2/logs/
if test -f /home/project_os2/logs/current_time.txt; then
  cat current_time.txt >> /home/project_os2/logs/timelog.txt
else
  sudo uptime -s '+%Y-%m-%d %X' > /home/project_os2/logs/current_time.txt
fi
date '+%Y-%m-%d %X' > /home/project_os2/logs/current_time.txt