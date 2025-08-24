# keep_alive.py
from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ FlairX is alive!"

def run():
    # Debug disabled for safety, threaded enabled for responsiveness
    app.run(host="0.0.0.0", port=8080, debug=False, threaded=True)

def keep_alive():
    t = Thread(target=run)
    t.daemon = True  # ensures thread won’t block program exit
    t.start()
