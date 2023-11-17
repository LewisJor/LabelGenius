from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class LabelingScript(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    goal = db.Column(db.String(100), nullable=False)
    example = db.Column(db.String(500), nullable=False)
    questions = db.Column(db.String(500), nullable=True)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_script', methods=['POST'])
def create_script():
    data = request.get_json()
    goal = data['goal']
    example = data['example']
    questions = data['questions']
    new_script = LabelingScript(goal=goal, example=example, questions=questions)
    db.session.add(new_script)
    db.session.commit()
    return jsonify({'status': 'Script created'})


@app.route('/get_scripts', methods=['GET'])
def get_scripts():
    scripts = LabelingScript.query.all()
    return jsonify([{'goal': s.goal, 'example': s.example, 'questions': s.questions} for s in scripts])


if __name__ == '__main__':
    app.run(debug=True)
