import pyttsx3, PyPDF2
import random

# Here goes name of file
pdfreader = PyPDF2.PdfReader(open('Menschen-B1-Glosario-Aleman-Espanol.pdf', 'rb'))
speaker = pyttsx3.init()

print('Extracting text for voiceover')

for page_num in range(len(pdfreader.pages)):
	text = pdfreader.pages[page_num].extract_text()
	clean_text = text.strip().replace('\n', ' ')

print('Saving to file')
speaker.save_to_file(clean_text, f'story{random.randint(10, 999)}.mp3')
speaker.runAndWait()

print('Completing the process')
speaker.stop()
