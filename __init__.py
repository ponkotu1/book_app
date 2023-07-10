import os
from flask import Flask

app = Flask(__name__)
app.config.from_mapping(
    SELECT_KEY = 'dev',
    DATABASE = os.path.join(app.instance_path,'')
)