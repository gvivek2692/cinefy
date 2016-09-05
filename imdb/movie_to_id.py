with open("movies.txt", "r") as infile:
  with open("movie_id.txt", "a") as outfile:
    for line in infile:
      # write logic for getting id from OMDB API.
      # The id should be written in a new line in
      # the file movie_id.txt.
      print line
