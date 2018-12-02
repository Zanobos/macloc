# Macloc

> Macloc server and webapp

## Sources

- **webapp** :
    the dedicated web application. check the [relative instructions](webapp/README.md)
- **webserver** :
    the complete webserver. check the instructions[relative instructions](webserver/README.md) on how to setup the can interface

## Connection

Local connection with test device (remember to setup manual ipv4 addresses):
- 192.168.1.10
- pi
- macloc1234

## Setup raspberry

1) Install 2018-11-13-raspbian-stretch-lite in an ssd with rufus
2) Perform command "touch ssh" while being in boot partition (to enable ssh login on boot)
3) Connect with ssh pi/raspberrypi
4) Create a dedicated user
```
sudo adduser macloc
sudo usermod -aG sudo macloc
echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDo/lqJ5dK+pXu+hzMObW4zD/XiElCRF/5nFqA0WMpbaKA2g1arjwXI+8RJKJANzyWCTApxPkVobH4e0qdOzEK2r4qxp+RyWfDINmpYI/O44ulqbcD6ocowkDAXyLrM/UAWciljutQ1TMbcqNlGI2mSPxonIA158A9XvJ4J+4CgIJn/iHlgO4m0/hz6/NtHyunVcZeaDonCxpjQ5WoazBq/slesMTJiXUR5RgNjH14ylkl3IZzyR/R/gM+uVMFUiqT7uyFQ8a+TsDdxl+3Bga3K//aiDY14XjyAw0dqBh0YHNuzgHJ1+LIIHAuypcCEPV30+T4GHfiveolNXFHuYzrf macloc" > ~/.ssh/authorized_keys/macloc.pub
```
5) change default password (log in as pi, and launch command passwd)

6) remove access with root account and allow only ssh login
```
sudo vim "/etc/ssh/sshd_config"

PermitRootLogin no
PasswordAuthentication no
```
7) remove dhcp! And put right addresses!
```
sudo vim /etc/dhcpcd.conf

Here is an example which configures a static address, routes and dns.
interface eth0
static ip_address=10.1.1.30/24
static routers=10.1.1.1
static domain_name_servers=10.1.1.1
```
8) Install needed packages
```
sudo apt-get -y update
sudo apt-get -y install git vim python3 python3-venv python3-dev supervisor
```
9) Prepare the workspace:
```
cd ~
mkdir workspace
git clone https://github.com/Zanobos/macloc
cd macloc
python3 -m venv venv
source venv/bin/activate
pip install -r webserver/app/doc/requirements.txt
pip install gunicorn 
```
   
