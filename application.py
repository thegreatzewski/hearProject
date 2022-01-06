from flask import Flask, render_template, request
from threading import Thread
#import RPi.GPIO as GPIO

app = Flask(__name__,static_url_path="/")

@app.route("/")
def root():
    return app.send_static_file('index.html')

@app.route("/publish", methods=["POST", "GET"])
def post_data():
    print("volume:", request.args.get("volume"))
    
    #do stuff here
    
    return {}
            

if __name__ == "__main__":
    '''
    This starts the server. You can safely put all of your global data
    in app.config (it behaves like a dict). The best thing to do is probably run either
    the server or the music service as a thread and use app.config as a go-between.
    
    '''
    app.run(debug=True, host='0.0.0.0')
