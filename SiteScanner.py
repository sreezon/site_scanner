import nmap
from collections import OrderedDict

class SiteScanner:
    def __init__(self):
        self.nm = nmap.PortScanner()

    def scan(self, site, ports):
        self.nm.scan(site, ports)
        res = []
        
        for host in self.nm.all_hosts():
            ports = []
            
            for proto in self.nm[host].all_protocols():
                lport = list(self.nm[host][proto].keys())
                lport.sort()
                for port in lport:
                    if self.nm[host][proto][port]['state'] == 'open':
                        ports.append(port)
            od = OrderedDict()
            od["Host"] = self.nm[host].hostname()
            od["Open ports"] = ports
            res.append(od)
        return res
