import app


@app.app.route('/')
def hello():
    return "hello world"


if __name__ == '__main__':
    app.app.run()