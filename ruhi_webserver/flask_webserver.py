from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/')
def root():
    print "Calling handler"
    return app.send_static_file('static/index.html')

@app.route('/<path:path>')
def static_proxy(path):
    #send_static_file will guess the correct MIME type
    return app.send_static_file('static/'+path)

if __name__ == "__main__":
    app.run(host='', port=7885, debug=True)
