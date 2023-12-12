import subprocess, psutil, configparser, os,time

def run():
    try:
        ip_add = subprocess.getoutput(
            "sudo ifconfig ppp0 | grep -E -o 'inet [0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}'  | cut -d' ' -f2")
        serial = subprocess.getoutput("cat /proc/cpuinfo | grep Serial | cut -d ' ' -f 2")
        temperature = psutil.sensors_temperatures(fahrenheit=False)["cpu_thermal"][0].current
        time = subprocess.getoutput("date")

        config = configparser.ConfigParser()
        config.read('/var/www/html/dist/data/connect.ini')
        config['connect']['ip_add'] = str(ip_add)
        config['connect']['serial'] = str(serial)
        config['connect']['temperature'] = str(temperature)
        config['connect']['time'] = str(time)

        with open('/var/www/html/dist/data/connect.ini', 'w') as configfile:  # save
            config.write(configfile)
    except:
        print("err")
if __name__ == "__main__":
    while True:
        time.sleep(300)
        run()
