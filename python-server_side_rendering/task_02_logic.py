#!/usr/bin/python3

from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def display_items():
    # Load data from items.json
    try:
        with open('items.json') as f:
            data = json.load(f)
            items = data.get("items", [])
    except (FileNotFoundError, json.JSONDecodeError):
        items = []  # Default to an empty list if the file doesn't exist or can't be read

    # Pass items list to the template
    return render_template('items.html', items=items)
