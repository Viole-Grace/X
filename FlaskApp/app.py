from flask import Flask, request, jsonify, render_template

import os
import re

# from save_to_pdf import single_image2pdf, multiple_images2pdf
# from scanner import calling_card

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/index.html')
def index():
	return render_template('index.html')

@app.route('/upload.html')
def upload():
	return render_template('upload.html')


if __name__ == '__main__':

	app.run(port=3000)