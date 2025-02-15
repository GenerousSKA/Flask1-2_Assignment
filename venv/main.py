from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

posts = [
    {
        "id": 1,
        "title": "My First Post",
        "content": "This is the content of my first post.",
        "category": "Technology",
        "date_published": "2024-07-05" 
    },
    {
        "id": 2,
        "title": "Travel Blog",
        "content": "This is the content of my travel blog.",
        "category": "Travel",
        "date_published": "2024-08-10" 
    },
    {
        "id": 3,
        "title": "Cooking Recipes",
        "content": "This is the content of my cooking recipes post.",
        "category": "Food",
        "date_published": "2024-09-20" 
    }
]

def format_date(date_string):
    from datetime import datetime
    date_obj = datetime.strptime(date_string, "%Y-%m-%d")
    return date_obj.strftime("%B %d, %Y")

app.jinja_env.globals['format_date'] = format_date

@app.route('/')
def index():
    return render_template('index.html', posts=posts)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    for post in posts:
        if post['id'] == post_id:
            return render_template('post.html', post=post)
    return "Post not found", 404

@app.route('/add', methods=['GET', 'POST'])
def add_post():
    if request.method == 'POST':
        new_post = {
            "id": len(posts) + 1,
            "title": request.form['title'],
            "content": request.form['content'],
            "category": request.form['category'],
            "date_published": datetime.now().strftime("%Y-%m-%d") 
        }
        posts.append(new_post)
        return redirect(url_for('index'))
    return render_template('add_post.html')

@app.route('/category')
def filter_by_category():
    category = request.args.get('category')
    filtered_posts = [post for post in posts if post['category'] == category]
    return render_template('index.html', posts=filtered_posts)

if __name__ == '__main__':
    app.run(debug=True)