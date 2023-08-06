from pybgpasn.bgp_asn_db import asn_data

class BGPASN:
    def __init__(self):
        self.asn_dict = asn_data
        

    def get_asn(self, key):
        return self.asn_dict.get(str(key), "Invalid key")

