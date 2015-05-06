from flask import Flask, request, g, redirect, url_for
app = Flask(__name__)

from flaskext.auth import Auth, AuthUser, login_required, logout
auth = Auth(app, login_url_name='index')


#Set the WPA2 password here.
with open('WPA2.txt') as file:
    lines = file.read().splitlines()
WPA2Key = lines[0]

#Change the usernames, passwords, and salts!
#    -username is the username to log in with
#    -password is your password (change this to a secure password!)
#    -salt is a randomly generated salt for password hashing
#    -level is the user's authentication level. Valid options are control and dataOnly
creds = [{'username':'admin',   'password':'password', 'salt':'231', 'level':'control' },
         {'username':'control', 'password':'password', 'salt':'925', 'level':'control' },
         {'username':'data',    'password':'password', 'salt':'761', 'level':'dataOnly'}
        ]

@app.before_request
def init_users():
    g.control = {}
    g.dataOnly = {}
    for dict in creds:
        user = AuthUser(username=dict['username'])
        user.set_and_encrypt_password(dict['password'], salt=dict['salt'])
        if dict['level'] == 'control':
            g.control[dict['username']] = user
        if dict['level'] == 'dataOnly':
            g.dataOnly[dict['username']] = user

@login_required()
def admin():
    return '''Authenticated to control the drone. <br>
              To control the drone, connect to the network called DroneControl with the key: <code>''' + WPA2Key + '''</code> <br> 
              <a href="/logout/">Log Out</a>'''

@login_required()
def dataOnly():
    return '''Authenticated for data. <br>
              <a href="/logout/">Log Out</a>'''

def index():
    if request.method == 'POST':
        username = request.form['username']
        if username in g.control:
            if g.control[username].authenticate(request.form['password']):
                return redirect(url_for('admin'))
        if username in g.dataOnly:
            if g.dataOnly[username].authenticate(request.form['password']):
                return redirect(url_for('dataOnly'))
        return 'Authentication Failed'
    #if request method is not POST, then simply return the form
    return ''' 
            Please authenticate to control the AR Drone. 
            <form method="POST">
                Username: <input type="text" name="username"/><br/>
                Password: <input type="password" name="password"/><br/>
                <input type="submit" value="Log in"/>
            </form>
        '''

def logout_view():
    user_data = logout()
    if user_data is None:
        return 'No user to log out.'
    return 'Logged out user {0}.'.format(user_data['username'])

# URLs
app.add_url_rule('/', 'index', index, methods=['GET', 'POST'])
app.add_url_rule('/admin/', 'admin', admin)
app.add_url_rule('/dataOnly', 'dataOnly', dataOnly)
app.add_url_rule('/logout/', 'logout', logout_view)

# Secret key needed to use sessions.
app.secret_key = '9b9777081187a5254ac5a4c2018e775d'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
