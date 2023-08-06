import json

class BGPASN:
    def __init__(self):
        with open('resources/bgp_asn.json', 'r') as f:
            self.asn_dict = json.load(f)

    def get_asn(self, key):
        return self.asn_dict.get(str(key), "Invalid key")

