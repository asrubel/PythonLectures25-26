from flask import Flask, request

from lecture_27_db import check_user

app = Flask('example-project')

@app.route('/')
def index():
    return 'Hello guys!'


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        template = """
                    <form method='POST'>
                    <input type='text' name='login' placeholder='Login...'>
                    <input type='password' name='password' placeholder='Password...'>
                    <input type='submit' value='Sign In'>
                    </form>
                    """
        return template

    elif request.method == 'POST':
        params = request.form
        user_login = params['login']
        user_password = params['password']
        user = check_user(user_login, user_password)
        print(user)
        if user:
            return "You are logged in!"
        else:
            return "Login failed!"

    return None


if __name__ == '__main__':
    app.run()
