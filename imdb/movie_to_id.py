with open("movies.txt", "r") as infile:
  with open("movie_id.txt", "a") as outfile:
    for line in infile:
        import json, requests, urllib
      	data = {}
      	data['t'] = line
      	data['y'] = ""
      	data['plot'] = 'short'
      	data['r'] = 'json'
      	url_values = urllib.urlencode(data)
      	url = "http://www.omdbapi.com/"
      	full_url = url + '?' + url_values
      	response = requests.get(full_url)
      	metadata = json.loads(response.text)
      	imdb_id = (metadata ['imdbID'] + '\n')
      	outfile.write(imdb_id)
 
