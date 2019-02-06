from flask import Flask,request, jsonify, make_response
from app.api.v1.models.Office import OfficeClass as office

office_list=[]  #list of offices
office1=office(1,'govt','Senate')
office2=office(2,'county','Governor')
office_list.append(office1)
office_list.append(office2)

class Offices():
    def get(self,id=None):
        officeData=[]
        for office in office_list:
            officeData.append({'data':{'id':office.id,'type':office.type,'name':office.name}})

        officeData.append({'status':200})
        return jsonify(officeData),200    

    def post(self):
        if not request.json or 'id' not in request.json:
            return jsonify({'status':400,'error':'office id cannot be null'})
        officejson=request.get_json()
        id=officejson['id']
        type=officejson['type']
        name=officejson['name']
        new_office=office(id,type,name)
        office_list.append(new_office)
        return jsonify({'status':'201','data':{'id':id,'type':type,'name':name}})    