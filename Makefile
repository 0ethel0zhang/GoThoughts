.PHONY: all clean

training_url = 'https://www.cs.cornell.edu/people/pabo/movie-review-data/review_polarity.tar.gz'

all: 
	data/raw/output_got.csv
	data/rar/review_polarity.tar.gz

clean:
	rm -f data/raw/*.csv

data/raw/output_got.csv:
	GetOldTweets3 --querysearch "#GameofThrones" --maxtweets 20000 --lang en --since 2019-05-20 --until 2019-05-21

data/rar/review_polarity.tar.gz:
	python src/data/download.py $(training_url) $@
