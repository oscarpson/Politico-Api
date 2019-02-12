from flask import jsonify, make_response

class ValidateParty:
    @staticmethod
    def validate_party_data(name,hqAddress,logoUrl):
        if len(name) <4 :
             return make_response(jsonify({"status":400},{"Error":"Party name is too short"}),400)
        elif len(hqAddress) < 4:
             return make_response(jsonify({"status":400},{"Error":"party address is too short"}),400)  
        elif len(logoUrl) < 4:
            return  make_response(jsonify({"status":400},{"Error":"logo name is too short"}),400)

    @staticmethod
    def validate_politico_partyid(id):
        if not id.isdigit()  :            
            return  make_response(jsonify({"status":400},{"Error":"political party id must be a number"}),400)

    @staticmethod
    def validate_party_json_format():
        return  make_response(jsonify({"status":400},{"Error":"political party post data must be in json format"}),400)     
         