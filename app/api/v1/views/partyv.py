from flask import Flask, request, jsonify, make_response, json
from app.api.v1.models.Party import PartyClass as party
from app.api.errorHandler.party_validation import ValidateParty as validate
parties_list = []


class parties():
    def get(self, id=None):
        if id != None:
            if validate().validate_politico_partyid(id):
                return validate().validate_politico_partyid(id)
            partydata = [
                party for party in parties_list if party["id"] == int(id)
            ]

            if len(partydata) < 1:
                return make_response(
                    jsonify({
                        'status': 404,
                        'error': 'party does not exist'
                    }), 404)
            return jsonify({
                'status': 200,
                'data': {
                    'id': partydata[0]["id"],
                    'name': partydata[0]["name"],
                    'logoUrl': partydata[0]["logoUrl"]
                }
            })

        return make_response(
            jsonify({"status": 200}, {"data": parties_list}), 200)

    def post(self):
        if not request.json:
            return validate().validate_party_json_format()

        partyjson = request.get_json(force=True)
        name = partyjson["name"]
        hqAddress = partyjson["hqAddress"]
        logoUrl = partyjson["logoUrl"]
        if validate().validate_party_data(name, hqAddress, logoUrl):
            return validate().validate_party_data(name, hqAddress, logoUrl)

        _id = len(parties_list) + 1

        myparty = {
            "id": _id,
            "name": name,
            "hqAddress": hqAddress,
            "logoUrl": logoUrl
        }

        parties_list.append(myparty)
        return make_response(jsonify({"status": 201}, {"data": myparty}), 201)

    def delete(self, id):

        if validate().validate_politico_partyid(id):
            return validate().validate_politico_partyid(id)

        party_to_delete = [
            party for party in parties_list if party["id"] == int(id)
        ]
        if len(party_to_delete) < 1:
            return jsonify({'status': 400, 'error': 'party does not exist'})
        parties_list.remove(party_to_delete[0])
        return jsonify({'status': 200, 'data': 'deleted successfuly'})

    def patch(self, _id, name):
        if _id == None or name == None:
            return jsonify({
                'status': 400,
                'error': 'party id cannot be null'
            }), 400

        party_to_patch = [
            party for party in parties_list if party["id"] == int(_id)
        ]

        if len(party_to_patch) < 1:
            return jsonify({'status': 404, 'error': 'party does not exist'})

        party_to_patch[0]["name"] = name
        parties_list.append(party_to_patch)

        return jsonify({
            'status': 200,
            'data': {
                'id': party_to_patch[0]["id"],
                'name': party_to_patch[0]["name"]
            }
        })
