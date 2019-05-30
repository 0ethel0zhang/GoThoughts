.PHONY: all clean

training_url = 'https://www.cs.cornell.edu/people/pabo/movie-review-data/review_polarity.tar.gz'

all: 
	data/raw/output_got.csv
	data/raw/review_polarity.tar.gz
	data/raw/twitter_input.csv
clean:
	rm -f data/raw/*.csv

data/raw/output_got.csv:
	GetOldTweets3 --querysearch "#GameofThrones" --maxtweets 20000 --lang en --since 2019-05-20 --until 2019-05-21

data/raw/twitter_input.csv:
	curl -o data/raw/twitter_input.csv https://d1p17r2m4rzlbo.cloudfront.net/wp-content/uploads/2016/03/Apple-Twitter-Sentiment-DFE.csv

data/rar/review_polarity.tar.gz:
	python src/data/download.py $(training_url) $@
