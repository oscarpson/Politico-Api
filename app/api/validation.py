from flask import jsonify, make_response

class ValidateData:
    @staticmethod
    def validate_office_data(officeType,officeName):
        if len(officeName) < 4:
            return make_response(jsonify({"status":400},{"Error":"Political office is too short"}),400)
        elif len(officeType) < 4:
             return make_response(jsonify({"status":400},{"Error":"Political office type is too short"}),400) 
    @staticmethod
    def validate_party_data(name,hqAddress,logoUrl):
        if len(name) <4 :
             return make_response(jsonify({"status":400},{"Error":"Party name is too short"}),400)
        elif len(hqAddress) < 4:
             return make_response(jsonify({"status":400},{"Error":"party address is too short"}),400)  
        elif len(logoUrl) < 4:
            return  make_response(jsonify({"status":400},{"Error":"logo name is too short"}),400)   

    @staticmethod
    def validate_politicoid(id,errormessage):
        if not id.isdigit()  :            
            return  make_response(jsonify({"status":400},{"Error":errormessage}),400)

    @staticmethod
    def validate_json_format(errormessage):
        return  make_response(jsonify({"status":400},{"Error":errormessage+" post data must be in json format"}),400)     
