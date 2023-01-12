from ncclient import manager
import xml.dom.minidom

m = manager.connect (host="10.202.17.200",port=830,username="admin1",password="Root123#",hostkey_verify=False)

netconf_loopback = """
<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface>
            <Loopback>
                <name>3</name>
                <description>loopback 3</description>
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
