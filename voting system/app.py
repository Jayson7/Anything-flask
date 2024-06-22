from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

votes = {'Candidate A': 0, 'Candidate B': 0, 'Candidate C': 0}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/vote', methods=['POST'])
def vote():
    candidate = request.form['candidate']
    if candidate in votes:
        votes[candidate] += 1
    return redirect(url_for('results'))

@app.route('/results')
def results():
    return render_template('results.html', votes=votes)

if __name__ == "__main__":
    app.run(debug=True)
