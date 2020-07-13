from ncclient import manager
import xml.dom.minidom

# IOS XE Settings
ios_xe_host = "10.10.0.20"
ios_xe_port = 830
ios_xe_username = "admin"
ios_xe_password = "123"

m = manager.connect(
    host=ios_xe_host,
    port=ios_xe_port,
    username=ios_xe_username,
    password=ios_xe_password,
    hostkey_verify=False,
    look_for_keys=False
)
netconf_interface_template = """
<config>
        <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
                <interface operation="delete">
                        <name>Loopback1</name>
                </interface>
        </interfaces>
</config> """

netconf_reply = m.edit_config(netconf_interface_template, target = "running")

print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

m.close_session()
