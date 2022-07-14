from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.210xc.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta


movie = db.movies.find_one({'title':'가버나움'})
print(movie['star'])


same_movies = list(db.movies.find({'star':movie['star']},{'_id':False}))
for  same_movie in same_movies:
    print(same_movie['title'])


db.movies.update_one({'title':'가버나움'},{'$set':{'star':'0'}})