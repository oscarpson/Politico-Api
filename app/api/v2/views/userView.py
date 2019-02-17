from flask import Flask, request, jsonify, make_response, json
from flask_jwt_extended import (
    JWTManager, create_access_token, create_refresh_token, jwt_required,
    get_jwt_identity, jwt_refresh_token_required, get_raw_jwt)
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
                                        phoneNumber, passportUrl, True)

        access_token = create_access_token(identity=restp['id'], fresh=True)
        refresh_token = create_refresh_token(identity=restp['id'])
        user_list = {
            "firstname": restp['firstname'],
            "lastname": restp["lastname"],
            "othername": restp["othername"],
            "email": restp["email"],
            "phoneNumber": restp["phoneNumber"],
            "passportUrl": restp["passportUrl"],
            "isAdmin": restp["isAdmin"],
            "access-token": access_token,
            "refresh-token":refresh_token
        }

        return make_response(
            jsonify({"status": 201}, {"data": user_list}), 201)

    def signin(self):
        if not request.json:
            return validate().validate_user_json_format()

