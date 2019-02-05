from flask import Blueprint,jsonify,request
from app.api.v1.views.partyv import parties 
prtInstance=parties()  #create party object and will initialize all blueprint 
#prty blueprint
party= Blueprint("party",__name__) 

@party.route('/parties',methods=['GET'])
def all_parties():
    all_parties=prtInstance.get() #get all parties using GET http verb
    return all_parties

@party.route('/parties',methods=['POST'])
def create_party():
    ptyResponse=prtInstance.post() #Post paty json data   
    return ptyResponse

@party.route('/parties',methods=['PUT'])
def update_party():
    ptyResponse=prtInstance.put() # Update party deatils using specified id
    return ptyResponse   

  





