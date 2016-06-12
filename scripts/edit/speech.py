# Copyright (C) 2016 Ross D Milligan
# GNU GENERAL PUBLIC LICENSE Version 3 (full notice can be found at https://github.com/rdmilligan/PyMovieStudio)

from speechtotext import SpeechToText
from threading import Thread
 
class Speech:
 
    def __init__(self):
        self.speech_to_text = SpeechToText()
        self.current_speech = None

    # create thread for capturing speech
    def start(self):
        Thread(target=self._update_speech, args=()).start()
 
    def _update_speech(self):
        while(True):
            self.current_speech = self.speech_to_text.convert()
                 
    # get the current speech
    def get_current_speech(self):
        return self.current_speech
