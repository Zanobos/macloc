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
4) Create a user
    1) sudo adduser macloc
    2) sudo usermod -aG sudo macloc
    3) add user ssh key in "~/.ssh/authorized_keys" with content "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDo/lqJ5dK+pXu+hzMObW4zD/XiElCRF/5nFqA0WMpbaKA2g1arjwXI+8RJKJANzyWCTApxPkVobH4e0qdOzEK2r4qxp+RyWfDINmpYI/O44ulqbcD6ocowkDAXyLrM/UAWciljutQ1TMbcqNlGI2mSPxonIA158A9XvJ4J+4CgIJn/iHlgO4m0/hz6/NtHyunVcZeaDonCxpjQ5WoazBq/slesMTJiXUR5RgNjH14ylkl3IZzyR/R/gM+uVMFUiqT7uyFQ8a+TsDdxl+3Bga3K//aiDY14XjyAw0dqBh0YHNuzgHJ1+LIIHAuypcCEPV30+T4GHfiveolNXFHuYzrf macloc"
    4) change default password (log in as pi, and launch command passwd)
5) remove access with root account, and allow only ssh login find the file "/etc/ssh/sshd_config" and add:
    1) PermitRootLogin no
    2) PasswordAuthentication no
6) sudo apt-get -y update
7) sudo apt-get -y install git vim python3 python3-venv python3-dev
8) 