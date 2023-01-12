# Utlisation de netconf sur le c800v

Netconf utilise le model de donnée YANG pour communiquer avec les apareille resaux. Yang et un langage de modelisation de donnée.

## Coté router

Activation avec la commande "netconf-yang" dans le mode configuration terminal du router.

Pour obtenir le com du datasore dnetconf-yang il existe la commande "show netconf-yang datastores".

## Version CLI

Voici un exemple d'utilisation CLI de netconf.

Connexion au router :

```bash
ssh admin1@10.202.17.200 -p 830 -s netconf
```

Realiser le handshake :

```bash
<?xml version="1.0" encoding="UTF-8"?><hello xmlns="urn:ietf:params:xml:ns:netconf:base:1.0"><capabilities><capability>urn:ietf:params:netconf:base:1.0</capability></capabilities></hello>]]>]]>
```

Pour recuperer toutes les interface :

```bash
<rpc message-id="103" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0"> <get> <filter> <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces"/> </filter> </get></rpc>]]>]]>
```

Et finalement pour fermer la sesion :

```bash
<rpc message-id="9999999" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
<close-session/></rpc>]]>]]>
```

## Coté client

Coté du client (administrateur), on peut utiliser du pyhton pour realisaer notre adminisatration. (Le faire manuellement etant bien trop fastidieux)

### Initialisation du code

Code pour initier la conexion :

```python
from ncclient import manager
import xml.dom.minidom

m = manager.connect (
 host="10.202.17.200",
 port=830,
 username="admin1",
 password="Root123#",
 hostkey_verify=False
 )
```

### Recuperer la running-config

```python
netconf_filter = """
<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
 <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native"/>
</filter>
"""

netconf_reply = m.get_config(source="running", filter=netconf_filter) #conection et recuperation da la config du datastores

print (xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
```

[Retour du code](./conf-xml-c800v.xml)

### Changer le hostname

```python
#configuration du nouvaux nom
netconf_hostname = """
<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <hostname>c8000v-math</hostname>
    </native>
</config>
"""

netconf_reply = m.edit_config(target="running", config=netconf_hostname) #edtition de la configuration

print (xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml()) #affige du retour
```

Retour :

```xml
<?xml version="1.0" ?>
<rpc-reply xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="urn:uuid:1847ee8b-e768-4be2-a516-a3a0bcfeff24">
    <ok/>
</rpc-reply>
```

### Ajouter une loopback

```python
#ici est present la configuration de la lo que je veux rajouter
netconf_loopback = """
<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface>
            <Loopback>
                <name>1</name>
                <description>loopback</description>
                <ip>
                    <address>
                        <primary>
                            <address>1.1.1.1</address>
                            <mask>255.255.255.255</mask>
                        </primary>
                    </address>
                </ip>
            </Loopback>
        </interface>
    </native>
</config>
"""

netconf_reply = m.edit_config(target="running", config=netconf_loopback)

print (xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
```

On obtien le même retour que precedement.

Coté routeur la configuration a bien été prise :

![lo-router](./Capture%20d’écran%20du%202023-01-11%2016-10-09.png)
