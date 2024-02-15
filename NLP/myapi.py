# From PyPI:

# Import
import paralleldots
# Setting your API key
# Get your API key here
# Viewing your API key
# Examples
class Api():
    
    def __init__(self):
        paralleldots.set_api_key('cCJzQfknlYIajvFJICtqVU5rN899jzLDCSklvZSqP8k')


    def sentiment(self, text):
        response = paralleldots.sentiment(text)
        return response
    
    
    def ner(self,text):
        response = paralleldots.ner(text)
        return response
    
    def emotions(self,text):
        response = paralleldots.emotion(text)
        return response
    
    