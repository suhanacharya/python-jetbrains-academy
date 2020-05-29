def tracklist(**kwargs):
	for artist, album in kwargs.items():
		print(artist)
		for k, v in album.items():
			print("ALBUM: {} TRACK: {}".format(k, v))
