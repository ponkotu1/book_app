from datetime import datetime
from flask import render_template
from flask_book_manegement import app

@app.route('/')
@app.route('/')
def home():
    return render_template(
        'index.html',
        title = 'Home Page',
        year = datetime.now().year,
    )