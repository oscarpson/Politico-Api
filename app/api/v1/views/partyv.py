from flask import Flask,request, jsonify, make_response
from app.api.v1.models.Party import PartyClass as party

#list of parties 
parties_list=[]
party1=party(1,"chama cha mtetezi","334 kwetu","images/govn.jpg")
party2=party(2,"chama cha wamama","Makwao street","images/govn.jpg")
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
        new_party=party(id,name,hqAddress,logoUrl)#create new party object
        #add to data dictionary
        parties_list.append(new_party)        
        return jsonify({'status':'201','data':{'id':id,'name':name,'hqAddress':hqAddress,'logoUrl':logoUrl}})

    def put(self,id):        
        if not request.json or 'id' not in request.json:
            return jsonify({'status':400,'error':'party details cannot be null'} )
        partyjson=request.get_json()        
        id=partyjson["id"]
        name=partyjson['name']    
        hqAddress=partyjson['hqAddress']
        logoUrl=partyjson['logoUrl']        
        edited_party=party(id,name,hqAddress,logoUrl)
        party_to_edit=[party for party in parties_list if party.id == id]  #get party which id matches id from post 
        if len(party_to_edit) < 1 :
            return jsonify({'status':400,'error':'party does not exist'})
        parties_list.remove(party_to_edit[0]) #remove party and append new party with specified details
        parties_list.append(edited_party)        
        return jsonify({'status':'200','data':{'id':party_to_edit[0].id,'name':party_to_edit[0].name,'hqAddress':party_to_edit[0].hqAddress,'logoUrl':party_to_edit[0].logoUrl}}),200

    def delete(self,id):

        if not 'id' :
            return jsonify({'status':400,'error':'party id cannot be null'} )        
        #partyjson=request.get_json()
        #self.id=id 
        party_to_delete=[party for party in parties_list if party.id == int(id)] 
        if len(party_to_delete) < 1 :
            return jsonify({'status':400,'error':'party does not exist'})  
        parties_list.remove(party_to_delete[0])
        return jsonify({'status':200,'data':'deleted successfuly'}) 

    def patch(self,id,name):
        if not request.json or 'id' not in request.json:
            return jsonify({'status':400,'error':'party id cannot be null'} )        
        partyjson=request.get_json()
        id=partyjson["id"] 
        name=partyjson['name']
        party_to_patch=[party for party in parties_list if party.id == id]
        
        if len(party_to_patch) < 1 :
            return jsonify({'status':404,'error':'party does not exist'}) 
        party_to_patch[0].name=name
        parties_list.append(party_to_patch) 
        return request.method 
        
        #return jsonify({'status':200,'data':'deleted successfuly'}) 



        






    