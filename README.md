# Politico-Api      [![Build Status](https://travis-ci.org/oscarpson/Politico-Api.svg?branch=develop)](https://travis-ci.org/oscarpson/Politico-Api)        [![Coverage Status](https://coveralls.io/repos/github/oscarpson/Politico-Api/badge.svg?branch=develop)](https://coveralls.io/github/oscarpson/Politico-Api?branch=develop)        [![Maintainability](https://api.codeclimate.com/v1/badges/05a8750d2198c3bb504e/maintainability)](https://codeclimate.com/github/oscarpson/Politico-Api/maintainability)
Politico application  is a forum for politicians and citizens where citizens can express their voting rights  and politicians showing interest by running for pollical offices 

# Usage

## Heroku service
Heroku url - `https://thawing-atoll-30148.herokuapp.com/api/v1/`

## Installation
*	Clone politico-api from `https://github.com/oscarpson/Politico-Api.git`
*	Install api requirements from requirements file in root directory by running `pip install -r requirements.txt`
 
# run the app
*	To run the app enter ` export FLASK_APP=run.py `in terminal  shift to new line and add `flask run` in new line in terminal

# run tests
*	APi tests are run using unnittest `python -m tests.py`

# Features and endpoints 

###	Create a new party request
* `Api/v1/parties` with `POST` method  and  parameters are `{ "name" :" ", "hqAddress":"", "logoUrl":"image"`
}

###	Get all parties
* `api/v1/parties` using `GET` verb 

###	Get specific party
* `api/v1/parties/<party_id>` using GET verb 

###	Create a political office 
* `api/v1/offices` with post verb and parameters are `{ "type":"",  "name" :""}`

###	Get all political offices
* `api/v1/offices`

# Acknowledgment
 © 2019, Politico-forum, Released under [MIT 
License](http://www.opensource.org/licenses/mit-license.php).
 Politico forum is authored and  maintained by  [Oscar Muigai](https://github.com/oscarpson/Politico-Api)
