# Macloc

Macloc server and webapp

## Sources

- **webapp** :
    the dedicated web application. check the [relative instructions](webapp/README.md)
- **webserver** :
    the complete webserver.

## Connection

## Setup raspberry

1) Install 2018-11-13-raspbian-stretch-lite in an ssd with rufus
2) Perform command "touch ssh" while being in boot partition (to enable ssh login on boot)
3) Connect with ssh pi/raspberrypi
4) Create a dedicated user
```sh
sudo adduser macloc
sudo usermod -aG sudo macloc
echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDo/lqJ5dK+pXu+hzMObW4zD/XiElCRF/5nFqA0WMpbaKA2g1arjwXI+8RJKJANzyWCTApxPkVobH4e0qdOzEK2r4qxp+RyWfDINmpYI/O44ulqbcD6ocowkDAXyLrM/UAWciljutQ1TMbcqNlGI2mSPxonIA158A9XvJ4J+4CgIJn/iHlgO4m0/hz6/NtHyunVcZeaDonCxpjQ5WoazBq/slesMTJiXUR5RgNjH14ylkl3IZzyR/R/gM+uVMFUiqT7uyFQ8a+TsDdxl+3Bga3K//aiDY14XjyAw0dqBh0YHNuzgHJ1+LIIHAuypcCEPV30+T4GHfiveolNXFHuYzrf macloc" > ~/.ssh/authorized_keys/macloc.pub
```
5) change default password for user pi for security reason (log in as pi, and launch command passwd)

6) remove access with root account and allow only ssh login
```sh
sudo vim "/etc/ssh/sshd_config"

    PermitRootLogin no
    PasswordAuthentication no
```
7) Configure the IP (need to know a free ip and gateway ip)
```sh
sudo vim /etc/dhcpcd.conf

    interface eth0
    static ip_address=192.168.1.200/24
    static routers=192.168.1.254
    static domain_name_servers=192.168.1.254
```
8) Install needed packages
```sh
sudo apt-get -y update
sudo apt-get -y install git vim python3 python3-venv python3-dev supervisor apache2 npm
```
9) Prepare the workspace:
```sh
cd ~
echo "export FLASK_APP=webserver.py" >> ~/.profile
mkdir workspace
cd workspace
git clone https://github.com/Zanobos/macloc
cd macloc/webserver
python3 -m venv venv
source venv/bin/activate
pip install -r app/doc/requirements.txt
pip install gunicorn
flask db upgrade
```
10) Prepare supervisor
```sh
sudo touch /etc/supervisor/conf.d/maclocbe.conf
sudo vim /etc/supervisor/conf.d/maclocbe.conf

    [program:maclocbe]
    command=/home/macloc/workspace/macloc/webserver/venv/bin/gunicorn -b 192.168.1.200:5000 -w 2 webserver:app
    directory=/home/macloc/workspace/macloc/webserver
    user=macloc
    autostart=true
    autorestart=true
    stopasgroup=true
    killasgroup=true
```
11) Prepare the hardware for can acquisition. Connect the can controller to the RPI, then
```sh
sudo apt-get install can-utils
sudo vim /boot/config.txt

    dtparam=spi=on
    dtoverlay=mcp2515-can0,oscillator=8000000,interrupt=25
    dtoverlay=spi-bcm2835-overlay

sudo reboot

sudo touch /etc/network/interfaces.d/can0
sudo vim /etc/network/interfaces.d/can0

    auto can0
    iface can0 can static 
        bitrate 500000
sudo reboot
```
12) Configure apache
```sh
sudo chown -R macloc /var/www/html/
sudo chgrp -R www-data /var/www/html/
```
13) Set up FE files
```sh
cd ~/workspace/macloc/webapp
sudo npm install npm@latest -g
npm install
npm run build
cp dist/* /var/www/html
```
