# **RAT_project**

USBbola injection permettant de scanner la machine victime, puis envoie les infos sensibles tel que l'ip publique, la mac,un nmap du reseau... et toutes commandes possibles sur Linux ou Powershell par le biais d'un traffic DNS qui sera exfiltré par un Hidden Service Tor (Anonyme - server Web nginx) et recupéré sur le server Web.

**Eventualités d'evolution :**

- Reverse Shell (Netcat, Telnet, Ssh, Dns exfiltration...)
- "MITM : Man In The Middle" (DNS Spoofing...)
- .. Libre court aux possibilités des cmd ..


# **Etapes projet:**

## 1. **USBbola injection**
    - 
## 2. **Footprinting python**
    - Searched informations :
        - IP
        - OS
        - distrib
        - mac
        - user
    - Recursiv files scan
    - Environnement scan

## 3. **Exfiltration DNS (Scapy):**
    - Data exfiltration (target)
    - Request sniffing (server)

## 4. **Vulnerability scan:**
    - API check

- Spyware injection:
    - BadUSB usage
    - Daemoning
    - hide process