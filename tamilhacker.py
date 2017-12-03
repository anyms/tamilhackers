from getpass import getpass
from cmd import Cmd
import requests
import os, sys


class TamilHackers(Cmd):
	prompt = "tamilhackers> "
	url = "http://localhost/projects/tamilhackers_media/manage/"

	def do_upload(self, line):
		f = open("last_uploaded.txt", "rt")
		name = f.read()
		username = raw_input("Username: ")
		password = getpass()
		title = raw_input("Your video title: ")
		description = raw_input("Your video description: ")
		thumb = raw_input("Your thumbnail location: ")
		video = raw_input("Your video location: ")

		os.rename(thumb, "{}.png".format(name))
		os.rename(video, "{}.mp4".format(name))
		f.close()

		f = open("last_uploaded.txt", "w")
		f.write(str(int(name) + 1))
		f.close()

		os.system("git add .")
		os.system('''git commit -m "{} video and thumb added"'''.format(name))
		os.system("git push origin master")

		thumb_url = "https://raw.githubusercontent.com/anyms/tamilhackers/master/{}.png".format(name)
		video_url = "https://raw.githubusercontent.com/anyms/tamilhackers/master/{}.mp4".format(name)

		res = requests.post(self.url, data={
			"username": username,
			"password": password,
			"title": title,
			"description": description,
			"thumb_url": thumb_url,
			"video_url": video_url
		})

		print(res.text)


if __name__ == "__main__":
	TamilHackers().cmdloop()