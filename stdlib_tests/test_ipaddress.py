import ipaddress 

print(ipaddress.IPv4Address('192.168.0.1'))
print(ipaddress.IPv4Address(323223552))
print(ipaddress.IPv4Address(b'\xC0\xA8\x00\x01'))
print(ipaddress.IPv6Address('2001:db8::'))
print(ipaddress.ip_network('192.168.0.0/28'))
print(ipaddress.IPv4Address('127.0.0.2') > ipaddress.IPv4Address('127.0.0.1'))
print(ipaddress.IPv4Address('127.0.0.2') == ipaddress.IPv4Address('127.0.0.1'))
print(ipaddress.IPv4Address('127.0.0.2') != ipaddress.IPv4Address('127.0.0.1'))
print(ipaddress.IPv4Address('127.0.0.2') + 3)
print(ipaddress.IPv4Address('127.0.0.2') - 3)
print(list(ipaddress.ip_network('192.0.2.0/29').hosts()))
print(list(ipaddress.ip_network('192.0.2.0/24').subnets()))
print(ipaddress.ip_network('192.0.2.1/32').compare_networks(ipaddress.ip_network('192.0.2.0/32')))
for addr in ipaddress.IPv4Network('192.0.2.0/28'):
     print(addr)
print(ipaddress.IPv4Address('192.0.2.6') in ipaddress.IPv4Network('192.0.2.0/28'))

