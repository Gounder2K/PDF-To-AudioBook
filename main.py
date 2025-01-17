import pyttsx3
import PyPDF2
from tkinter.filedialog import *

book = askopenfilename()
pdfreader = PyPDF2.PdfReader(book)
print(pdfreader)
pages = len(pdfreader.pages) 

for num in range(0,pages):
    page = pdfreader.pages[num]
    text = page.extract_text()
    player = pyttsx3.init()
    player.say(text)
    player.save_to_file(text, 'test.mp3')
    player.runAndWait()
