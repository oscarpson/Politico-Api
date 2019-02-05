from flask import Flask,request, jsonify, make_response
from app.api.v1.models.Party import PartyClass as party

#list of parties 
parties_list=[]
party1=party(1,"chama cha mtetezi","334 kwetu","images/govn.jpg")
party2=party(1,"chama cha wamama","Makwao street","images/govn.jpg")
parties_list.append(party1)
parties_list.append(party2)

class parties():
    def get(self,id=None):
        
        partyData=[]
        #loop through party data dictionary
        for party in parties_list:
            partyData.append({'status':200,'data':{'id':party.id,'name':party.name,'hqAddress':party.hqAddress,'logoUrl':party.logoUrl}})

        #return data in json form
        return jsonify(partyData)

    def post(self):
       # id=request.args['id']
        partyjson=request.get_json()
        id=partyjson["id"]
        name=partyjson['name']    
        hqAddress=partyjson['hqAddress']
        logoUrl=partyjson['logoUrl']

        #create new party object
        new_party=party(id,name,hqAddress,logoUrl)
        #add to data dictionary
        parties_list.append(new_party)
        
        return jsonify({'status':'201','data':{'id':id,'name':name,'hqAddress':hqAddress,'logoUrl':logoUrl}})



    