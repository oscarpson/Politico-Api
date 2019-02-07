from flask import Flask,request, jsonify, make_response
from app.api.v1.models.Office import OfficeClass as office

office_list=[]  #list of offices
#office1=office(1,'govt','Senate')
class Offices():
    def get(self,id=None):
        if id != None:
            specific_office=[office for office in office_list if office.id ==int(id)]
            if len(specific_office) < 1 :
                return jsonify({'status':401,'error':'office not found'})
            return jsonify({'status':200,'data':{'id':specific_office[0]["id"],'type':specific_office[0]["type"],'name':specific_office[0]["name"]}})

        return make_response(jsonify({"status":200},{"data":office_list}),200)

    def post(self):
        if not request.json:
            return jsonify({'status':400,'error':'office id cannot be null'})
        officejson=request.get_json()        
        type=officejson["type"]
        name=officejson["name"]
        id=len(office_list)+1
        new_office={"id":id,"type":type,"name":name}
        office_list.append(new_office)
        return make_response(jsonify({"status":"201"},{"data":new_office},{"msg":"office added"}),201)