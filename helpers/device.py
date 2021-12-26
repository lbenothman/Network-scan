import socket

def get_device_name(ip: str):
    """
    Get the device name

    Args:
        ip (str): The ip address

    Returns:
        str: Name of the device
    """
    return socket.gethostbyaddr(ip)[0]