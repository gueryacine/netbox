# IP address families
AF_CHOICES = ((4, "IPv4"), (6, "IPv6"))

# Prefix statuses
PREFIX_STATUS_CONTAINER = 0
PREFIX_STATUS_ACTIVE = 1
PREFIX_STATUS_RESERVED = 2
PREFIX_STATUS_DEPRECATED = 3
PREFIX_STATUS_CHOICES = (
    (PREFIX_STATUS_CONTAINER, "Container"),
    (PREFIX_STATUS_ACTIVE, "Active"),
    (PREFIX_STATUS_RESERVED, "Reserved"),
    (PREFIX_STATUS_DEPRECATED, "Deprecated"),
)

# IP address statuses
IPADDRESS_STATUS_ACTIVE = 1
IPADDRESS_STATUS_RESERVED = 2
IPADDRESS_STATUS_DEPRECATED = 3
IPADDRESS_STATUS_DHCP = 5
IPADDRESS_STATUS_CHOICES = (
    (IPADDRESS_STATUS_ACTIVE, "Active"),
    (IPADDRESS_STATUS_RESERVED, "Reserved"),
    (IPADDRESS_STATUS_DEPRECATED, "Deprecated"),
    (IPADDRESS_STATUS_DHCP, "DHCP"),
)

# IP address roles
IPADDRESS_ROLE_LOOPBACK = 10
IPADDRESS_ROLE_SECONDARY = 20
IPADDRESS_ROLE_ANYCAST = 30
IPADDRESS_ROLE_VIP = 40
IPADDRESS_ROLE_VRRP = 41
IPADDRESS_ROLE_HSRP = 42
IPADDRESS_ROLE_GLBP = 43
IPADDRESS_ROLE_CARP = 44
IPADDRESS_ROLE_CHOICES = (
    (IPADDRESS_ROLE_LOOPBACK, "Loopback"),
    (IPADDRESS_ROLE_SECONDARY, "Secondary"),
    (IPADDRESS_ROLE_ANYCAST, "Anycast"),
    (IPADDRESS_ROLE_VIP, "VIP"),
    (IPADDRESS_ROLE_VRRP, "VRRP"),
    (IPADDRESS_ROLE_HSRP, "HSRP"),
    (IPADDRESS_ROLE_GLBP, "GLBP"),
    (IPADDRESS_ROLE_CARP, "CARP"),
)

IPADDRESS_ROLES_NONUNIQUE = (
    # IPAddress roles which are exempt from unique address enforcement
    IPADDRESS_ROLE_ANYCAST,
    IPADDRESS_ROLE_VIP,
    IPADDRESS_ROLE_VRRP,
    IPADDRESS_ROLE_HSRP,
    IPADDRESS_ROLE_GLBP,
    IPADDRESS_ROLE_CARP,
)

# VLAN statuses
VLAN_STATUS_ACTIVE = 1
VLAN_STATUS_RESERVED = 2
VLAN_STATUS_DEPRECATED = 3
VLAN_STATUS_CHOICES = (
    (VLAN_STATUS_ACTIVE, "Active"),
    (VLAN_STATUS_RESERVED, "Reserved"),
    (VLAN_STATUS_DEPRECATED, "Deprecated"),
)


# PORT statuses
PORT_STATUS_ACTIVE = 1
PORT_STATUS_RESERVED = 2
PORT_STATUS_DEPRECATED = 3
PORT_STATUS_CHOICES = (
    (PORT_STATUS_ACTIVE, "Active"),
    (PORT_STATUS_RESERVED, "Reserved"),
    (PORT_STATUS_DEPRECATED, "Deprecated"),
)

# PORT types
PORT_TYPES_ETHERNET = 1
PORT_TYPES_VIRTUAL = 2
PORT_TYPES_LAG = 3
PORT_TYPES_CHOICES = (
    (PORT_TYPES_ETHERNET, "Ethernet"),
    (PORT_TYPES_VIRTUAL, "Virtual"),
    (PORT_TYPES_LAG, "Link Aggregation Group (LAG)"),
)

IFACE_MODE_ACCESS = 100
IFACE_MODE_TAGGED = 200
IFACE_MODE_TAGGED_ALL = 300
IFACE_MODE_CHOICES = [
    [IFACE_MODE_ACCESS, "Access"],
    [IFACE_MODE_TAGGED, "Tagged"],
    [IFACE_MODE_TAGGED_ALL, "Tagged All"],
]


# Bootstrap CSS classes
STATUS_CHOICE_CLASSES = {
    0: "default",
    1: "primary",
    2: "info",
    3: "danger",
    4: "warning",
    5: "success",
}
ROLE_CHOICE_CLASSES = {
    10: "default",
    20: "primary",
    30: "warning",
    40: "success",
    41: "success",
    42: "success",
    43: "success",
    44: "success",
}

# IP protocols (for services)
IP_PROTOCOL_TCP = 6
IP_PROTOCOL_UDP = 17
IP_PROTOCOL_CHOICES = ((IP_PROTOCOL_TCP, "TCP"), (IP_PROTOCOL_UDP, "UDP"))
