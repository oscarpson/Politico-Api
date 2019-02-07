from flask import Blueprint,jsonify,request
from app.api.v1.views.partyv import parties 
from app.api.v1.views.OfficeView import Offices
prtInstance=parties()  #create party object and will initialize all blueprint 
officeInstance= Offices()
#prty blueprint
party= Blueprint("parties",__name__,url_prefix="/api/v1/") 
office=Blueprint("offices",__name__,url_prefix="/api/v1/")

@party.route('/parties',methods=['GET'])
def all_parties():
    all_parties=prtInstance.get() #get all parties using GET http verb
    return all_parties

@party.route('/parties/<id>',methods=['GET'])
def all_specific_party(id):
    all_parties=prtInstance.get(id) #get all parties using GET http verb
    return all_parties

@party.route('/parties',methods=['POST'])
def create_party():
    ptyResponse=prtInstance.post() #Post paty json data   
    return ptyResponse
  
    
@party.route('/parties/<id>',methods=['DELETE']) 
def delete_party(id):
    ptyResponse=prtInstance.delete(id)    
    return ptyResponse 


@party.route('/parties/<id>/<name>',methods=['PATCH'])  
def update_viapatch(id,name):
    ptyResponse=prtInstance.patch(int(id), name)
    return ptyResponse 

#office blueprints start here
@office.route('/offices',methods=['GET'])
def get_office():
    officeResponse=officeInstance.get()
    return officeResponse  

@office.route('/offices/<id>',methods=['GET'])
def get_specific_office(id):
    officeResponse=officeInstance.get(id)
    return officeResponse

@office.route('offices',methods=['POST']) 
def post_office():
    officeResponse=officeInstance.post()
    return officeResponse     



