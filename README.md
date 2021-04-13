# Facial Analysis

Juptyer Notebook containing facial analysis and training models of images from: https://github.com/MicrosoftDocs/ai-fundamentals

Additions were made by adding real-time video analysis using OpenCV and Microsoft's Face Cognitive Service: https://azure.microsoft.com/en-ca/services/cognitive-services/face/

### Setup
"Face Analysis.ipynb" has all the details on how each code cell works and how to run it. The only thing you need to do is make a config.py file inside of the facial-analysis directory and add the 2 following lines:

`cog_key = 'YOUR_KEY'`

`cog_endpoint = 'YOUR_ENDPOINT'`

Replace **YOUR_KEY** and **YOUR_ENDPOINT** with the key and endpoint that can be found in the Azure portal, on the Keys and Endpoint page for your Face resource. 
Should you require more information, there are more details above the first code block in "Facial Analysis.ipynb"

The first four code cells need to be run before being able to run the **Video Analysis** section.
