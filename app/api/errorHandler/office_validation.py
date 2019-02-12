from flask import jsonify, make_response

class ValidateOffice:
    @staticmethod
    def validate_office_data(officeType,officeName):
        if len(officeName) < 4:
            return make_response(jsonify({"status":400},{"Error":"Political office is too short"}),400)
        elif len(officeType) < 4:
             return make_response(jsonify({"status":400},{"Error":"Political office type is too short"}),400)

    @staticmethod
    def validate_politico_officeid(id):
        if not id.isdigit()  :            
            return  make_response(jsonify({"status":400},{"Error":"political office id must be a number"}),400)

    @staticmethod
    def validate_office_json_format():
        return  make_response(jsonify({"status":400},{"Error":"Office post data must be in json format"}),400)     
         