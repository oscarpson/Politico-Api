from flask import Flask, request, jsonify, make_response, json
from app.api.v2.models.user import UserClass as user
from app.api.errorHandler.user_validation import ValidateUser as validate
from app.database.userQuery import UserQueries as userquery


class Users():
    def post(self):
        if not request.json:
            return validate().validate_user_json_format()

        userjson = request.get_json(force=True)
        firstname = userjson["firstname"]
        lastname = userjson["lastname"]
        othername = userjson["othername"]
        email = userjson["email"]
        phoneNumber = userjson["phoneNumber"]
        passportUrl = userjson["passportUrl"]
        isAdmin = userjson["isAdmin"]

        if validate().validate_user_data(firstname, lastname, othername, email,
                                         phoneNumber, passportUrl):
            return validate().validate_user_data(firstname, lastname,
                                                 othername, email, phoneNumber,
                                                 passportUrl, isAdmin)

        restp = userquery().create_user(firstname, lastname, othername, email,
                                         phoneNumber, passportUrl,True)
        return make_response(jsonify({"status": 201}, {"data": restp}), 201)
