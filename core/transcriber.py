from deepgram import Deepgram
import json
from django.http import JsonResponse
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import re


# The API key we created in step 3
DEEPGRAM_API_KEY = '3388eb878e642b2f5d1e9ee4abb1ee155230567b'


MIMETYPE = 'audio/wav'

def main(PATH_TO_FILE = ""):
    # Initializes the Deepgram SDK
    deepgram = Deepgram(DEEPGRAM_API_KEY)
    print(PATH_TO_FILE)
    with open(PATH_TO_FILE, 'rb') as audio:
        source = {'buffer': audio, 'mimetype': 'audio/wav'}
        options = { "smart_format": True, "model": "nova", "language": "en-US", "punctuate":False,
                   "start":False }
    
        print('Requesting transcript...')
        print('Your file may take up to a couple minutes to process.')
        

        try:
            # response = .transcription.sync_prerecorded(source, {'punctuate':True, 'verify':False})
            response = deepgram.transcription.sync_prerecorded(source, options)
            print(json.dumps(response, indent=4))
            

            text = response.values()

            # transcription_data = response.json()
            # transcribed_text = transcription_data.get('transcription', '')
            print(response)
        except Exception as err:
            text = "None"
            print(err)

    return text

