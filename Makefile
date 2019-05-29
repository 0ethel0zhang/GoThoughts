.PHONY: all clean
all: data/raw/output_got.csv
clean:
	rm -f data/raw/*.csv
data/raw/output_got.csv:
	GotOldTweets3 --querysearch "#GameofThrones" --maxtweets 20000 --lang en --since 2019-05-20 --until 2019-05-21
