import socket

def get_device_name(ip: str):
    """[summary]

    Args:
        ip (str): The ip address

    Returns:
        str: Name of the device
    """
    return socket.gethostbyaddr(ip)[0]