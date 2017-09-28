from flask import Flask, render_template
from utils import percent

app = Flask(__name__)

@app.route('/occupations')
def occupations():
	o = percent.getOccupations()
	return render_template('index', 
		occupations=o, 
		randomOccupation=percent.getRandomOccupation(o))

if __name__ == "__main__":
	app.debug = True
	app.run()
