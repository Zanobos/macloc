# macloc-webserver

## Raspberry setup

- In /boot/config.txt add the following lines:

>		dtparam=spi=on
>		dtoverlay=mcp2515-can0,oscillator=8000000,interrupt=25
>		dtoverlay=spi-bcm2835-overlay
	
- Use the following command to install can-utils (struct and socket are also needed, but should be already installed):

```console
    sudo apt-get install can-utils
```

- To set up the CAN interface manually:

```console
    sudo ip link set can0 up type can bitrate 500000
```	

- To set up the CAN interface automatically at startup, add the following lines to /etc/network/interfaces:

>		auto can0
>		iface can0 can static
>			bitrate 500000

- After a reboot, you can check if the interface is available using ifconfig.

# Python setup

- Install dependencies with

```console
    sudo pip install webserver/doc/requirements.txt
```