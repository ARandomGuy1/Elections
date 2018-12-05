from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json

app = Flask(__name__)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/p1")
def render_main():
    with open('election.json') as election_data:
        election = json.load(election_data)
    return render_template('page1.html', states = get_state_options(election), candidates = get_candidates())
    
@app.route("/p1")
def render_response();
    with open('election.json') as election_data:
        election = json.load(election_data)
    state = request.args["states"]
    candidate = request.args["candidates"]
    
    
def get_state_options(election):
    state = ""
    listOfStates = []
    for x in range(0, len(election)):
        state = election[x]["Location"]['State']
        if state not in listOfStates:
            listOfStates.append(election[x]["Location"]["State"])
    options = ""
    for x in listOfStates:
        options += Markup("<option value=\"" + x + "\">" + x + "</option>")
    return options

def get_candidates():
    listOfCandidates = []
    listOfCandidates.append("Rand Paul") 
    listOfCandidates.append("Rick Santorum") 
    listOfCandidates.append("Martin O'Malley") 
    listOfCandidates.append("Chris Christie") 
    listOfCandidates.append("Jeb Bush") 
    listOfCandidates.append("Hillary Clinton") 
    listOfCandidates.append("John Kasich") 
    listOfCandidates.append("Donald Trump") 
    listOfCandidates.append("Mike Huckabee") 
    listOfCandidates.append("Marco Rubio") 
    listOfCandidates.append("Bernie Sanders") 
    listOfCandidates.append("Carly Fiorina") 
    listOfCandidates.append("Ben Carson") 
    listOfCandidates.append("Ted Cruz") 
    for x in listOfCandidates:
        options += Markup("<option value=\"" + x + "\">" + x + "</option>")
    return options


if __name__=="__main__":
    app.run(debug=False, port=54321)
