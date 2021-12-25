import typer
import logging
# Disavle scapy warnings
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

import scapy.all as scapy
import socket

# Set verbose to 0
scapy.conf.verb = 0

app = typer.Typer()


@app.command()
def about():
    """
    About this program
    """    
    typer.echo("A pyhthon network scanner")


@app.command()
def scan(ip: str):
    """
    Scan the network to find the mac addresses
    Args:
        ip (str): The ip address
    """
    devices = network_scan(ip)
    typer.echo("IP\t\t\tMAC Address\t\t\tName")
    for ip in devices.keys():
            typer.echo(f"{ip}\t\t{devices[ip]['mac']}\t\t{devices[ip]['name']}")

def network_scan(ip: str):
    """
    Scan network to find mac addresses

    Args:
        ip (str): The ip address

    Returns:
        list: Devices list
    """
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answers =scapy.srp(arp_request_broadcast, timeout=1)[0]

    devices = {}
    for answer in answers:
        devices[answer[1].psrc] = {'name': get_device_name(answer[1].psrc), 'mac': answer[1].hwsrc}

    return devices    

def get_device_name(ip: str):
    """[summary]

    Args:
        ip (str): The ip address

    Returns:
        str: Name of the device
    """
    return socket.gethostbyaddr(ip)[0]


if __name__ == "__main__":
    app()