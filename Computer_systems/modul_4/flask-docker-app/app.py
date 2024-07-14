from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World! I did it! 5000+5000"

# if __name__ == '__main__':
#     app.run()

if __name__ == '__main__':
  app.run(debug=False, host='0.0.0.0')
