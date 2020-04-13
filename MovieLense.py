import numpy as np
import pandas as pd


movies = pd.read_csv("./ml-latest-small/movies.csv")
ratings = pd.read_csv("./ml-latest-small/ratings.csv")


#1) 사용자별 평균평점을 산출하여 제일 높은 사용자와, 제일 낮은 사용자 id 출력
user_rate = ratings.groupby('userId').mean()

user_rate_max = user_rate[user_rate['rating'] == user_rate['rating'].max()].index.tolist()
user_rate_min = user_rate[user_rate['rating'] == user_rate['rating'].min()].index.tolist()

print("1.최고평점 : " + user_rate_max.__str__())
print("1.최저평점 : " + user_rate_min.__str__())

#2. 영화별 평균평점을 산출하여 제일 높은 영화와 제일 낮은 영화의 제목을 출력
print()
movie_rate = ratings.groupby('movieId', as_index=False).mean()
movie_rate_max = movie_rate['rating'].max()
movie_rate_min = movie_rate['rating'].min()

#print(movie_rate_max)
#print(movie_rate_min)
#print(movie_rate)

merge = pd.merge(movie_rate, movies)
print("2.최고평점 : " + merge[merge['rating'] == movie_rate_max]['title'].values)
print("2.최저평점 : " + merge[merge['rating'] == movie_rate_min]['title'].values)


#3. 범죄스릴러(Crime, Thriller) 장르에서 최고 평점을 얻은 영화의 제목을 출력 :

genre_movie = movies[movies["genres"].str.contains("Crime") | movies["genres"].str.contains("Thriiler")]
genre_movie_rate = pd.merge(genre_movie, movie_rate)
print("3.범죄스릴러 장르 최고평점 : " + genre_movie_rate[genre_movie_rate['rating'] == genre_movie_rate['rating'].max()]['title'].values)
