import subprocess

new_mac = input("Enter new MAC address : ")
interface = input("Enter interface name : ")

try:
    print("[+] Turning interface down...")
    subprocess.run(["sudo","ip","link","set",interface,"down"],check=True)

    print("[+] Changing MAC address...")
    subprocess.run(["sudo","macchanger","-m",new_mac,interface],check=True)

    print("[+] Turning interface up...")
    subprocess.run(["sudo","ip","link","set",interface,"up"],check=True)

    print("[+] MAC address changed successfully!")

except subprocess.CalledProcessError:
    print("[-] Error while changing MAC address...")