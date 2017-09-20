from flask import Flask

my_app = Flask(__name__)

@my_app.route('/')
def root():
    return "hello world route"

@my_app.route('/route1')
def route1():
    return "you have reached route 1"

@my_app.route('/route2')
def route2():
    return "you have reached route 2"

if __name__ == '__main__':
    my_app.debug = True
    my_app.run()
