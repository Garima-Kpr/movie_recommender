from recommender import recommend_random, recommend_test_nmf
from utils import movies, model, lookup_movie_name, print_movie_columns
from flask import Flask,render_template,request


app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html',name = 'GARIMA',movies=movies['title'].to_list())

@app.route('/recommendation')
def recommendation():
    print(request.args)
    titles = request.args.getlist('input')
    titles_id = lookup_movie_name(movies, titles)
    ratings = request.args.getlist('rating')
    ratings = map(float, ratings)
    user_rating = dict(zip(titles_id,ratings))
 #   recs = recommend_random(movies, user_rating,k=3)
    recs = recommend_test_nmf(movies, user_rating, model, k=5)
    return render_template('recommendation.html',recs=recs)

if __name__=='__main__': 
    app.run(debug=True, port = 5001)

