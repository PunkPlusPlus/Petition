from app import app
from app.models.User import User


@app.route('/api/users')
def getUsers():
    result = User.query.all()
    return str(len(result))

@app.route('/api/users/<id>')
def getUser(id):
    result = User.query.get_or_404(id)
    return result.email
