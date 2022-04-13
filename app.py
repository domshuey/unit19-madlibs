from flask import Flask, request, render_template
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret1'

@app.route('/')
def fill_form():
    prompt = story.prompts
    return render_template('form.html', prompt=prompt)

@app.route('/story')
def read_story():
    text = story.generate(request.args)
    return render_template('story.html', text=text)