from ScannerDao import ScannerDao
from SiteScanner import SiteScanner
from flask import jsonify
from datetime import datetime

class ScannerService:
    def __init__(self):
        self.dao = ScannerDao()
        self.scanner = SiteScanner()
        self.ports = '0-1000'
        
    def scan_sites(self, domains):
        scanned_domains = []
        for domain in domains:
            scan_res = self.scanner.scan(domain, self.ports)
            if not scan_res or len(scan_res) > 1:
                scanned_domains.append({"Host": domain, "Error":"Invalid ip or hostname, please go back and try again"})
                continue
            domain_name = scan_res[0]["Host"]
            history = self.scan_history(domain_name)
            self.save_scan(scan_res)
            self.add_history(scan_res, history)
            scanned_domains.extend(scan_res)
        if not domains:
            return jsonify("Please go back and enter an ip or hostname to scan")
        return jsonify(scanned_domains)

    def scan_history(self, domain):
        return self.dao.get_port_history(domain)

    def save_scan(self, scan_res):
        for res in scan_res:
            host = res["Host"]
            open_port_list = res["Open ports"]
            open_ports = ','.join(map(str, open_port_list))
            self.dao.save_port_history(host, open_ports)

    def add_history(self, scan_res, host_history):
        new_open_ports_key = "Newly open ports since last scan"
        new_closed_ports_key = "Newly closed ports since last scan"
        for res in scan_res:
            host = res["Host"]
            res[new_open_ports_key] = []
            res[new_closed_ports_key] = []
            res["Open ports from past scans"] = host_history
            timestamps = list(host_history.keys())
            if timestamps:
                new_open_ports = []
                new_closed_ports = []
                timestamps.sort(reverse = True, key=lambda date: datetime.strptime(date, "%Y-%m-%d %H:%M:%S"))
                prev_scan_ports = set(host_history[timestamps[0]].split(','))
                current_ports = set(res["Open ports"])
                print(timestamps)
                print(prev_scan_ports)
                print(current_ports)
                for port in current_ports:
                    if str(port) not in prev_scan_ports:
                        new_open_ports.append(port)
                for port in prev_scan_ports:
                    if int(port) not in current_ports:
                        new_closed_ports.append(port)
                res[new_open_ports_key] = new_open_ports
                res[new_closed_ports_key] = new_closed_ports
            

                
            
    
