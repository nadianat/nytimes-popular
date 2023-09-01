import requests
from flask import Flask, render_template, request

app = Flask(__name__)

#API
nyt_api_key = "ijYRQQdongRQO823wVhDQbFeimolNAch"
nyt_api = f"http://api.nytimes.com/svc/mostpopular/v2/mostviewed/all-sections/7.json?api-key={nyt_api_key}"

#get articles from nyt api
@app.route('/')
def index():
    response = requests.get(nyt_api)
    if response.status_code == 200:
        data = response.json()
        articles = data.get('results', [])
        return render_template('index.html', articles=articles)
    else:
        error_message = f'Error fetching data from the API: {response.status_code}'
        return render_template('error.html', error_message=error_message)

@app.route('/article/<int:article_id>')
def article_details(article_id):
    articles = index()
    if article_id > 0 and article_id <= len(articles):
        article = articles[article_id - 1]
        return render_template('article.html', article=article)
    else:
        return "Article not found."

if __name__ == '__main__':
    app.run(debug=True)



#print(response.status_code)
#response = requests.get(nyt_api)
#articles = response.get("posts", [])
#print(response.json())