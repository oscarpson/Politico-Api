from flask import Flask, request, jsonify, make_response, json
from app.api.v2.models.vote import VoteClass as vote
from app.api.errorHandler.vote_validation import ValidateVote as validate
from app.database.voteQuery import VoteQueries as votequery

class Votes():
    def post(self):
        if not request.json:
            return validate().validate_vote_json_format()

        votejson = request.get_json(force=True)
        createdOn = votejson["createdOn"]
        userId = votejson["userId"]
        officeId = votejson["officeId"]
        candidateId = votejson["candidateId"]
        

        #if validate().validate_vote(userId):
        #    return validate().validate_vote(userId)

        restp = votequery().vote(createdOn, userId, officeId, candidateId)
        return make_response(jsonify({"status": 201}, {"data": restp}), 201)