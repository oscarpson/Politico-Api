from flask import jsonify, make_response

class ValidateData:
    @staticmethod
    def validate_office_data(officeType,officeName):
        if len(officeName) < 4:
            return make_response(jsonify({"status":404},{"Error":"Political office name cannot be empty"}),404)
