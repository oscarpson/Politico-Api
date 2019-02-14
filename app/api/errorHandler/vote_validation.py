from flask import jsonify, make_response


class ValidateVote:
    @staticmethod
    def validate_vote(id):
        if not id.isdigit():
            return make_response(
                jsonify({"status": 400},
                        {"Error": "political party id must be a number"}), 400)

    @staticmethod
    def validate_vote_json_format():
        return make_response(
            jsonify(
                {"status": 400},
                {"Error": "political party post data must be in json format"}),
            400)
