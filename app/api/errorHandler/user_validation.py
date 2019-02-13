from flask import jsonify, make_response

class ValidateUser:
    @staticmethod
    def validate_user_data(firstname, lastname, othername, email,phoneNumber, passportUrl):
        if len(firstname) <3 :
             return make_response(jsonify({"status":400},{"Error":"Party name is too short"}),400)
        elif len(lastname) < 4:
             return make_response(jsonify({"status":400},{"Error":"party address is too short"}),400)  
        elif len(othername) < 4:
            return  make_response(jsonify({"status":400},{"Error":"logo name is too short"}),400)

    @staticmethod
    def validate_user_json_format():
        return  make_response(jsonify({"status":400},{"Error":"political party post data must be in json format"}),400)     
                 