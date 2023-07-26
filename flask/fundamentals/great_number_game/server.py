import os
from flask import Flask, render_template, request, session, redirect
import random

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')
