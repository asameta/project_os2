import threading
import requests,time,os,hashlib,zlib,setup,os
from krohne import IFC050
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
from datetime import datetime
import pytz

def sendPHP(datas):

    fail_count =0
    try:
        x = requests.post(setup.url, data=datas, timeout=10)
        if (x.text.split(':')[0] == 'command'):
            os.system(x.text.split(':')[1])
        else:
            pass
            # print(x.text)
        fail_count = 0
        response = x.text
    except:
        fail_count += 1
        if fail_count == setup.fail:
            os.system('sudo reboot')
        # print('net error!')

    time.sleep(int(setup.wait))

def sendETKI(dataSeries):
  sys_host ='http://3.78.44.39:8086'
  sys_token ='aM_LyB4mSTVg9oO3Dc3qn3nnOBdFWDLXdizdIYVRMc6eucZcsmy2WdijRDjqCGCuCg_V2Vo5bzHVY5ZhInQBRw=='
  sys_org = 'Electro'
  sys_bucket = "os2_db"

  noc = InfluxDBClient(url=sys_host, token=sys_token, org=sys_org)
  write_api = noc.write_api(write_options=SYNCHRONOUS)

  try:
      data = {}
      data = {"point{}".format(i + 1): Point("os_records")
      .tag("server", delta["server"]) \
          .tag("slave", delta["slave"]) \
          .tag("unit", delta["unit"]) \
          .field(delta["parameter"], delta["value"]) \
          .time(datetime.now(pytz.timezone('Europe/Istanbul')), WritePrecision.NS)
              for i, delta in enumerate(dataSeries)}

      write_api.write(bucket=sys_bucket, record=list(data.values()))

  except:
      # print("[Warning] : bucket failed")
      pass
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

def run():
    flowmeter = IFC050(setup.address,
                       setup.port,
                       setup.stopbits,
                       setup.bytesize,
                       setup.parity,
                       setup.baudrate)

    serial_number = getserial()

    if serial_number:
        volume_flow = None
        counter1 = None
        operating_time = None
        device_status = None

        try:
            volume_flow = flowmeter.getVolumeFlow()*3600
        except:
            pass

        try:
            counter1 = flowmeter.getCounter1()
        except:
            pass

        try:
            operating_time = flowmeter.getOperatingTime()
        except:
            pass

        try:
            device_status = str(flowmeter.getDeviceStatus())
        except:
            device_status = 0
            print("[]:MODBUS ERR. Check parameters or connection cables")

        if volume_flow !=None and counter1 != None and operating_time != None and device_status != None :
            checksum = zlib.crc32((str(volume_flow) +
                                   str(counter1) +
                                   str(serial_number) +
                                   str(operating_time) +
                                   str(device_status) +
                                   'poweras').encode())

            datas = {'volume_flow': volume_flow,
                     'counter1': counter1,
                     'serial_number': serial_number,
                     'operating_time': operating_time,
                     'device_status': device_status,
                     'checksum': checksum}
            #  sending to influx db
            # threading.Thread(target=sendPHP, args=(datas,)).start()
        else:
            pass

        dataSeries = []

        if volume_flow is not None:
            dataSeries.append({
                "server": str(serial_number),
                "slave": str(flowmeter.address),
                "parameter": str("1"),
                "value": round(volume_flow, 3),
                "unit": str("m3/h"),
            })

        if counter1 is not None:
            dataSeries.append({
                "server": str(serial_number),
                "slave": str(flowmeter.address),
                "parameter": str("2"),
                "value": round(counter1, 3),
                "unit": str("m3"),
            })

        if operating_time is not None:
            dataSeries.append({
                "server": str(serial_number),
                "slave": str(flowmeter.address),
                "parameter": str("3"),
                "value": round(operating_time, 3),
                "unit": str("s"),
            })

        if device_status is not None:
            dataSeries.append({
                "server": str(serial_number),
                "slave": str(flowmeter.address),
                "parameter": str("4"),
                "value": str(device_status),
                "unit": str(""),
            })


        if dataSeries:
            threading.Thread(target=sendETKI, args=(dataSeries,)).start()

    else:
        print("[Warning] : no serial detected!")
        pass