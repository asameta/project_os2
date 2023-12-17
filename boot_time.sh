cat /home/project_os2/logs/current_time.txt >> /home/project_os2/logs/timelog.txt

while [ 0 ]
do
  date '+%Y-%m-%d %X' > /home/project_os2/logs/current_time.txt 2&1
  sleep 1
done