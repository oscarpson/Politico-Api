parties_list=[]
class PartyClass():
    def __init__(self,name,hqAddress,logoUrl):
        self.id=len(parties_list)+1
        self.name=name
        self.hqAddress=hqAddress
        self.logoUrl=logoUrl