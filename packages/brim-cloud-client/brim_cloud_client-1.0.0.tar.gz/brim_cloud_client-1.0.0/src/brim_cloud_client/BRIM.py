import requests
from loader import Loader

class TMB:
    """Client for BRIM cloud server"""

    def __init__(self, cm, cb, p, Rc, C, anneal=0.00011, seed=0):
        self.server_url = 'https://ord1.isingmodel.org/'
        self.api_key = ''
        self.cm = str(cm)
        self.cb = str(cb)
        self.p = str(p)
        self.Rc = str(Rc)
        self.C = str(C)
        self.anneal = str(anneal)
        self.seed = str(seed)


    def solve(self, file: str):
        """Send file to BRIM cloud server"""
        url: str = self.server_url + '/upload'
        files: dict = {'file': open(file, 'rb')}
        headers: dict = {'Authorization': self.api_key,
                         'cm': self.cm, 
                         'cb': self.cb, 
                         'p': self.p, 
                         'Rc': self.Rc, 
                         'C': self.C, 
                         'anneal': self.anneal, 
                         'seed': self.seed}
        print("file:", file)
        with Loader("Waiting for remote server..."):
            response = requests.post(url, files=files, headers=headers, timeout=1200)
        response_json = response.json()
        if response_json["error"] == "0":
            return response_json["final_stats"], response_json["final_status"], response_json["final_results"]
        return None, None, None
    
    def _system_status(self):
        """Get system status"""
        url: str = self.server_url + '/status'
        response = requests.get(url)
        return response.json()
    
    def print_system_status(self):
        """print system status"""
        status = self._system_status()
        print("Remote Server Status:")
        print("---------------------")
        for key, value in status.items():
            print(key, value)
        print("---------------------")
    
    def print_neofetch(self):
        url: str = self.server_url + '/neofetch'
        response = requests.get(url)
        print(response.text)
    
    def set_remote_server(self, server_url: str):
        self.server_url = server_url