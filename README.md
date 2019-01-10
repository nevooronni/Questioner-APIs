# Questioner-APIs

## Badges
-------------------------

[![Build Status](https://travis-ci.org/nevooronni/Questioner-APIs.svg?branch=develop)](https://travis-ci.org/nevooronni/Questioner-APIs) [![Coverage Status](https://coveralls.io/repos/github/nevooronni/Questioner-APIs/badge.svg?branch=develop)](https://coveralls.io/github/nevooronni/Questioner-APIs?branch=develop) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)  [![PEP8](https://img.shields.io/badge/code%20style-pep8A-orange.svg)](https://www.python.org/dev/peps/pep-0008/)


## Summary 
-------------------------
Question is a crowd sourcing app for meetups, it allows the meetup organizer to priotirize questions to be answered by enabling other users to upvote/downvote on a question as it bubbles up and down the log.

This project is managed by pivotal tracker board. [view the board here](https://www.pivotaltracker.com/n/projects/2235272)

The site is hosted [here]()

The following are API endpoints enabling one to:
-------------------------
* Create account and log in
* Creat a meetup
* Post a question to a specific meetup
* Post a comment to a specific question
* Upvote or downvote a question
* RSVP for a specific meetup

Pre-requisites
--------------------------
- Postman
- Git
- Python3

Testing
-------------------------- 
- Clone this repository to your computer:
    ```
    git clone git@github.com:nevooronni/Questioner-APIs.git
    ```
- cd into this folder:
    ```
    Questioner-APIs
    ```
    
Installation
-------------------------- 
1. Create a virtual environment
    ```
      virtaulenv -p python3 ve```
      source venv/bin/activate
    ```nv
    ```

2. Activate the virtual environment
    ```
      source venv/bin/activate
    ```

3. Install git
    ```
      sudo apt-get install git-all
    ```

4. Switch to 'develop' branch
    ```
      git checkout develop
    ```
5. Install requirements
    ```
      pip install -r requirements.txt
    ```
6. Set environment variables
    ```
      mv .env.run .env 

      source .env   
    ```

7. Run app  
    ```
      flask run
    ```
8. Run tests
    ```
      py.test --cov=app --cov-config .coveragerc
    ```

Use Postman to test following working Endpoinsts
-------------------------

| Endpoint | Functionality |
----------|---------------
POST/meetups | Create a meetup record
GET/meetups/&lt;meetup-id&gt; | Fetch a specific meetup record
GET /meetups | Fetch all upcoming meetup records
POST /questions | Create a question for a specific meetup
PATCH /questions/&lt;question-id&gt;/upvote | Upvote (increases votes by 1) a specific question
PATCH /questions/&lt;question-id&gt;/downvote | Downvote (decrease votes by 1) a specific question
POST /meetups/&lt;meetup-id&gt;/rsvps | Respond to meetup RSVP

Authors
-------------------------
**Neville Oronni** - _Github_ -  [nevooronni](https://github.com/nevooronni)

License
----------
This project is licensed under the MIT license. See [LICENSE](https://github.com/nevooronni/Questioner-APIs/blob/master/LICENSE) for details.

Contribution
---------------
Fork this repository, contribute, and create a pull request to this repo's gh-pages branch.

Acknowledgements
-----------------
1. Andela workshops
2. Andela Bootcamp Team2 members
