from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json

app = Flask(__name__)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/p1")
def render_page1():
    with open('election.json') as election_data:
        election = json.load(election_data)
    return render_template('page1.html', states = get_state_options(election), candidates = get_candidates())
    

@app.route("/response")
def render_response():
    print(1)
    with open('election.json') as election_data:
        election = json.load(election_data)
    state = request.args["states"]
    candidate = request.args["candidates"]
    states = {}
    statesR = {}
    statesD = {}
    candidateInState = {}
    listOfCandidates = get_candidates_list()
    listOfCandidatesR = get_candidates_list_R()
    listOfCandidatesD = get_candidates_list_D()
    pop = 0
    popR = 0
    popD = 0
    for x in range(0, len(election)):
        if election[x]["Location"]["State"] not in states:
            for y in listOfCandidates:
                pop += election[x]["Vote Data"][y]["Number of Votes"]
            for y in listOfCandidatesR:
                popR += election[x]["Vote Data"][y]["Number of Votes"]
            for y in listOfCandidatesD:
                popD += election[x]["Vote Data"][y]["Number of Votes"]
            states[election[x]["Location"]["State"]] = pop
            statesR[election[x]["Location"]["State"]] = popR
            statesD[election[x]["Location"]["State"]] = popD
            pop = 0
            popR = 0
            popD = 0
            candidateInState[election[x]["Location"]["State"]] = election[x]["Vote Data"][candidate]["Number of Votes"]
        else:
            for y in listOfCandidates:
                states[election[x]["Location"]["State"]] += election[x]["Vote Data"][y]["Number of Votes"]
            for y in listOfCandidatesR:
                statesR[election[x]["Location"]["State"]] += election[x]["Vote Data"][y]["Number of Votes"]
            for y in listOfCandidatesD:
                statesD[election[x]["Location"]["State"]] += election[x]["Vote Data"][y]["Number of Votes"]
            candidateInState[election[x]["Location"]["State"]] += election[x]["Vote Data"][candidate]["Number of Votes"]
    fact = 0
    fact2 = 0
    for x in states:
        if x == state:
            fact = (candidateInState[x]/states[x])*100
    for x in listOfCandidates:
        if x == candidate:
            if x in listOfCandidatesD:
                for y in states:
                    if y == state:
                        fact2 = (candidateInState[y]/statesD[y])*100
            if x in listOfCandidatesR:
                for y in states:
                    if y == state:
                        if statesR[y] > 0:
                            fact2 = (candidateInState[y]/statesR[y])*100
                        else:
                            fact2 = 0
                
    print(0)            
    return render_template("page1.html", response = candidate + " got " + str(fact) + "% of the vote in " + state, response2 = candidate + " got " + str(fact2) + "% of the vote in their party in " + state, states = get_state_options(election), candidates = get_candidates())
    
        
    
    
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
    options = ""
    for x in listOfCandidates:
        options += Markup("<option value=\"" + x + "\">" + x + "</option>")
    return options
    
def get_candidates_list_R():
    listOfCandidates = []
    listOfCandidates.append("Rand Paul") 
    listOfCandidates.append("Rick Santorum") 
    listOfCandidates.append("Martin O'Malley") 
    listOfCandidates.append("Chris Christie") 
    listOfCandidates.append("Jeb Bush") 
    listOfCandidates.append("John Kasich") 
    listOfCandidates.append("Donald Trump") 
    listOfCandidates.append("Mike Huckabee") 
    listOfCandidates.append("Marco Rubio") 
    listOfCandidates.append("Carly Fiorina") 
    listOfCandidates.append("Ben Carson") 
    listOfCandidates.append("Ted Cruz") 
    return listOfCandidates 


def get_candidates_list_D():
    listOfCandidates = []
    listOfCandidates.append("Hillary Clinton") 
    listOfCandidates.append("Bernie Sanders") 
    return listOfCandidates     


def get_candidates_list():
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
    return listOfCandidates 


if __name__=="__main__":
    app.run(debug=False, port=54321)
