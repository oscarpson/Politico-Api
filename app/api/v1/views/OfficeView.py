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