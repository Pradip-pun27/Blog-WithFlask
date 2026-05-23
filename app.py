from flask import Flask, render_template, request, redirect, url_for
import os
from datetime import datetime

app = Flask(__name__)

@app.template_filter('nl2br')
def nl2br_filter(s):
    return s.replace('\n', '<br>')

POSTS_FILE = 'posts.txt'

def load_posts():
    if not os.path.exists(POSTS_FILE):
        return []
    posts = []
    with open(POSTS_FILE, 'r', encoding='utf-8') as f:
        content = f.read().strip().split('---')
        for block in content:
            if block.strip():
                lines = block.strip().split('\n')
                post = {'title': '', 'date': '', 'content': ''}
                for line in lines:
                    if line.startswith('title:'):
                        post['title'] = line.split(':', 1)[1].strip()
                    elif line.startswith('date:'):
                        post['date'] = line.split(':', 1)[1].strip()
                    else:
                        post['content'] += line + '\n'
                post['content'] = post['content'].strip()
                if post['title']:
                    posts.append(post)
    return list(reversed(posts))

def save_post(title, content):
    with open(POSTS_FILE, 'a', encoding='utf-8') as f:
        f.write(f'---\ntitle: {title}\ndate: {datetime.now().strftime("%Y-%m-%d")}\n{content}\n')

@app.route('/')
def index():
    posts = load_posts()
    return render_template('index.html', posts=posts)

@app.route('/post/<int:post_id>')
def post(post_id):
    posts = load_posts()
    if 0 <= post_id < len(posts):
        return render_template('post.html', post=posts[post_id])
    return redirect(url_for('index'))

@app.route('/new', methods=['GET', 'POST'])
def new_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        save_post(title, content)
        return redirect(url_for('index'))
    return render_template('new.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)