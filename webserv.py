from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from collections import OrderedDict

import json

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

with open('config.json') as json_data_file:
    data = json.load(json_data_file)

class settings(Form):
    serial = TextField('serial', validators=[validators.required()])

@app.route("/", methods=['GET', 'POST'])
def index():
    form = settings(request.form)
    print form.errors
    if request.method == 'POST':
        serial=request.form['serial']
        if form.validate():
            flash(' Configuration Saved')
            outfile = open('config.json', "w")
            outfile.write(json.dumps(data, indent=4, sort_keys=False))
            outfile.close()
        else:
            flash(' Error: All Fields are Required to be Filled')

    return render_template('index.html', form=form, data=data)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=2048, debug=True)
