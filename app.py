from flask import Flask, redirect, url_for

app = Flask(__name__)
app.config.from_object('config')

@app.route('/posts/<slug>')
def posts(slug):
  return posts_data[slug]


posts_data = {
  'post-1' : {'name': 'This morning', 'date': '26.03.2025'},
  'post-2' : {'name': 'My evening', 'date': '25.03.2025'},
  'post-3' : {'name': 'My sisters birthday', 'date': '25.03.2025'},
  'post-4' : {'name': 'Holiday planning', 'date': '21.03.2025'},
  'post-5' : {'name': 'The struggle with my future', 'date': '07.03.2025'},
  'post-6' : {'name': 'Visited by friends', 'date': '11.03.2025'},
}


if __name__ == '__main__':
  app.run()