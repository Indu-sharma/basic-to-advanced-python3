from netaddr import IPAddress, IPNetwork, IPRange, IPSet


class IpUtils (object):
    """Generic Utility for IPv4/IPv6 networks/addresses handling"""

    def __init__(self):
        pass

    def ips_in_range(self, start_ip, end_ip):
        """ Retruns all the IPs between two IPv4/v6 addresses; input Ips can be either in format 10.10.10.10/32 or just
        10.10.10.10 """
        try:
            ips = IPRange (IPNetwork (start_ip), IPNetwork (end_ip))
        except:
            ips=[start_ip,end_ip]
            print("Invalid", ips)
        return map (str, ips)

    def compare_ips(self, ip1, ip2):
        """Compare Two IPv6(Compressed or Uncompressed format) or IPv4 returns True if Logically same"""
        if IPNetwork (ip1) == IPNetwork (ip2):
            return True
        return False

    def match_in_set(self, ipaddress, myset):
        """ It returns the matched Equavalent Ip address from the list of various notations of same IP"""
        for ip in myset:
            if self.compare_ips (ipaddress, ip):
                return ip
        return None
