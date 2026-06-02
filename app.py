from flask import Flask, render_template

app = Flask(__name__)

# This is a temporary Python list acting as our database
initiatives = [
    {"title": "Beach Cleanup Drive", "location": "Local Coast", "date": "June 15, 2026"},
    {"title": "Community Food Bank", "location": "Downtown Center", "date": "June 20, 2026"},
    {"title": "Youth Tech Mentoring", "location": "Public Library", "date": "July 02, 2026"}
]

@app.route('/')
def home():
    return "<h1>Welcome to the Local Volunteer App!</h1>"

# Our new second page route
@app.route('/opportunities')
def opportunities():
    # This sends the 'initiatives' list over to an HTML file to display it
    return render_template('opportunities.html', opportunities_list=initiatives)

if __name__ == '__main__':
    app.run(debug=True)
