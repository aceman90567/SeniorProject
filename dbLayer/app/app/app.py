from flask import Flask, render_template
from werkzeug import secure_filename
from app import app, db, models
import os, sys

@app.route('/')
def index():
        return 'Pred Pol Database Abstraction Layer'

