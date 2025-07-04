from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

blog_posts = []

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('name')
def handle_name(username):
    emit('name', username, broadcast=True) 

@socketio.on('message')
def handle_message(msg):
    emit('message', msg, broadcast=True)

@socketio.on('blogPost')
def handle_blog_post(post):
    blog_posts.append(post)
    emit('blogPost', post, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
