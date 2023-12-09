# script for informing server that reboot and ready to get a command
import os,datetime,socket,setup,psutil
import mysql.connector,time
def runner():
  testIP = "8.8.8.8"
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  s.connect((testIP, 0))
  ipaddr = s.getsockname()[0]
  host = socket.gethostname()

  def getserial():
    # Extract serial from cpuinfo file
    cpuserial = "0000000000000000"
    try:
      f = open('/proc/cpuinfo','r')
      for line in f:
        if line[0:6]=='Serial':
          cpuserial = line[10:26]
      f.close()
    except:
      cpuserial = "ERROR000000000"

    return cpuserial


  cpuinfo = getserial()

  disk_usage=psutil.disk_usage('/').percent

  boot_time = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")

  tempSens =  psutil.sensors_temperatures(fahrenheit=False)["cpu_thermal"][0].current
  # tempSens = 0
  dbSetting = [
    {
    'host': '3.74.54.184',
    'user' : 'wi2023',
    'password': 'Wittehyolo2023.',
    'port' : '3306',
    'database' : setup.remote_database,
    }
  ]
  for i in dbSetting:
    try:

      mydb = mysql.connector.connect(
        host=i['host'],
        user=i['user'],
        password=i['password'],
        port=i['port'],
        database=i['database']
      )
      mycursor = mydb.cursor()
      sql = "INSERT INTO online_devices (cpuinfo, ip, disk_usage, boot_time, tempSens) VALUES (%s, %s,%s, %s,%s)"
      val = (str(cpuinfo), str(ipaddr), str(disk_usage),str(boot_time), str(tempSens))
      mycursor.execute(sql, val)
      mydb.commit()
      time.sleep(1)

      mycursor = mydb.cursor()
      mycursor.execute("SELECT command, update_status FROM  update_devices WHERE cpuinfo =%s", (cpuinfo,))
      myresult = mycursor.fetchall()
      if myresult:
        if myresult[0][1] == "Yes" or myresult[0][1] == "YES":
          print(myresult[0][0])
          os.system(myresult[0][0])
      time.sleep(2)
    except:
      pass
