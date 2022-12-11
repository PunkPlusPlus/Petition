from app import app


@app.route('/test')
def test():
    return 'test'


@app.route('/test2')
def test2():
    return 'test2'