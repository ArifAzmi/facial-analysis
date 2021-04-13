# Facial Analysis

Juptyer Notebook containing facial analysis and training models of images from: https://github.com/MicrosoftDocs/ai-fundamentals
Additions were made by adding real-time video analysis using OpenCV and Microsoft's Face Cognitive Service: https://azure.microsoft.com/en-ca/services/cognitive-services/face/

### Setup
Face Analysis.ipynb has all the details on how each code cell works and how to run it. The only thing you need to do is make a config.py file inside of the facial-analysis directory. This is done to keep Face resource's keys and endpoint private. In config.py add the following 2 lines:

`cog_key = 'YOUR_KEY'`

`cog_endpoint = 'YOUR_ENDPOINT'`

The key and endpoint can be found in the Azure portal, on the Keys and Endpoint page for your Face resource.

To simply run the Video Analysis section, the first four code cells need to be run.
