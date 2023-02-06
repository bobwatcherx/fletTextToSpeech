from flet import *
from gtts import gTTS
import os
import random

def main(page:Page):

	mytext = TextField(label="insert text to speech")
	audio =  Audio(src=False)
	page.overlay.append(audio)

	# REMOVE FILE EVERY BUILD THE TEXT TO SPEECH
	# AND FILE new generated again
	def removeallfileinfolder():
		folder_path = "result/"
		# LIST FILE IN FOLDER result and REMOVE ALL FILE
		files = os.listdir(folder_path)
		for file in files:
			file_path = os.path.join(folder_path,file)
			# AND IF FOUND FILE IN FOLDER THEN REMOVE ALL
			if os.path.isfile(file_path):
				os.remove(file_path)
				print(f"YOU FILE IS REMOVE SUCESS {file_path}")



	def speaknow(e):
		try:
			removeallfileinfolder()
			obj = gTTS(
				text=mytext.value,
				lang="en"
				)
			# AND SAVE RESULT FILE SPEECH TO FOLDER RESULT
			obj.save(f"result/{random.randint(0,100)}.wav")
			# AND SET TO BLANK SRC OF AUDIO
			audio.src = ""
			page.update()


			folder_path = "result/"

			# CHECK FILE IN FOLDER RESULT IF FOUND THEN PLAY SOUND
			files = os.listdir(folder_path)
			for file in files:
				print("you file found ",file)
				# SET AUDIO SRC TO YOU RESULT SPEECH
				audio.src = folder_path + file
				audio.play()
				page.update()
		except Exception as e:
			print(e)
			print("CHECK ERROR , YOU SOUND FAILED TO PLAY !!!")
		page.update()






	page.add(
	Column([
	Text("Text TO speech",size=30,weight="bold"),
	mytext,
	ElevatedButton("speak",
	bgcolor="blue",color="white",
	on_click=speaknow

	),
	Text("Sorry I cannot show you sound result because Copyright",size=20,weight="bold")

	])
	)


flet.app(target=main,assets_dir="result")
