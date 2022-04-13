from server.bo import BusinessObject as bo

class BreakBO (bo.BusinessObject):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return ""

    def from_dict(dictionary=dict()):
        obj = BreakBO()
        return obj