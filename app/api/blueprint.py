from flask import Blueprint,jsonify,request
from app.api.v1.views.partyv import parties 
prtInstance=parties()  #create party object and will initialize all blueprint 
party= Blueprint("party",__name__)

@party.route('/parties',methods=['GET'])
def all_parties():
    all_parties=prtInstance.get() #get all parties using GET http verb
    return all_parties

  





