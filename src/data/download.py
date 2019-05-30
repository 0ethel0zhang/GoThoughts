import requests
url = 'https://www.cs.cornell.edu/people/pabo/movie-review-data/review_polarity.tar.gz'
filename = "../data/raw/review_polarity.tar.gz"
with open(filename, 'wb') as ofile:
   response = requests.get(url)
   file.write(response.content)
