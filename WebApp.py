import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello2():
   return ('Hello There')

#if __name__ == "__main__":
 #  app.run()

