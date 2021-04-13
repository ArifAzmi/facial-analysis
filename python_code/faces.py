def show_faces(image_path, detected_faces, show_id=False):
    import matplotlib.pyplot as plt
    from PIL import Image, ImageDraw

    # Open an image
    img = Image.open(image_path)

    # Create a figure to display the results
    fig = plt.figure(figsize=(8, 6))

    if detected_faces:
        # If there are faces, how many?
        num_faces = len(detected_faces)
        prediction = ' (' + str(num_faces) + ' faces detected)'
        # Draw a rectangle around each detected face
        for face in detected_faces:
            r = face.face_rectangle
            bounding_box = ((r.left, r.top), (r.left + r.width, r.top + r.height))
            draw = ImageDraw.Draw(img)
            draw.rectangle(bounding_box, outline='magenta', width=5)
            if show_id:
                plt.annotate(face.face_id,(r.left, r.top + r.height + 15), backgroundcolor='white')
        #a = fig.add_subplot(1,1,1)
        fig.suptitle(prediction)

    plt.axis('off')
    plt.imshow(img)

def show_face_attributes(image_path, detected_faces):
    import matplotlib.pyplot as plt
    from PIL import Image, ImageDraw

    # Open an image
    img = Image.open(image_path)

    # Create a figure to display the results
    fig = plt.figure(figsize=(8, 6))

    if detected_faces:
        # If there are faces, how many?
        num_faces = len(detected_faces)
        prediction = ' (' + str(num_faces) + ' faces detected)'
        # Draw a rectangle around each detected face
        for face in detected_faces:
            r = face.face_rectangle
            bounding_box = ((r.left, r.top), (r.left + r.width, r.top + r.height))
            draw = ImageDraw.Draw(img)
            draw.rectangle(bounding_box, outline='magenta', width=5)

            # Annotate with face attributes (only age and emotion are used in this sample)
            detected_attributes = face.face_attributes.as_dict()
            age = 'age unknown' if 'age' not in detected_attributes.keys() else int(detected_attributes['age'])
            annotations = 'Person aged approximately {}'.format(age)
            txt_lines = 1
            if 'emotion' in detected_attributes.keys():
                for emotion_name in detected_attributes['emotion']:
                    txt_lines += 1
                    annotations += '\n - {}: {}'.format(emotion_name, detected_attributes['emotion'][emotion_name])
            plt.annotate(annotations,((r.left + r.width), (r.top + r.height + (txt_lines * 12))), backgroundcolor='white')

        # Plot the image
        #a = fig.add_subplot(1,1,1)
        fig.suptitle(prediction)

    plt.axis('off')
    plt.imshow(img)

def get_face_attributes(image_path, detected_faces, index):
    import matplotlib.pyplot as plt
    import os
    import cv2 as cv
    from PIL import Image, ImageDraw

    # Open an image
    img = Image.open(image_path)
    
    annotations = ''
    
    if detected_faces:
        # If there are faces, how many?
        num_faces = len(detected_faces)
        prediction = ' (' + str(num_faces) + ' faces detected)'
        for face in detected_faces:
            # Get anger, happiness and neutral attributes to put on HUD
            detected_attributes = face.face_attributes.as_dict()
            age = 'age unknown' if 'age' not in detected_attributes.keys() else int(detected_attributes['age'])
            annotations = 'Age: {}'.format(age)
            if 'emotion' in detected_attributes.keys():
                annotations += ' | Anger: {}'.format(detected_attributes['emotion']['anger'])
                annotations += ' | Happiness: {}'.format(detected_attributes['emotion']['happiness'])
                annotations += ' | Neutral: {}'.format(detected_attributes['emotion']['neutral'])
                
                #for emotion_name in detected_attributes['emotion']:
                #   if emotion_name == 'anger' or emotion_name == 'happiness' or emotion_name == 'neutral':
                #      annotations += '\n {}: {}'.format(emotion_name, detected_attributes['emotion'][emotion_name])
                
            # Get happiness score
            happinessScore = detected_attributes['emotion']['happiness']
            
            # Get all attributes to display
            txt_lines = 0
            attributeText = ''
            for attribute in detected_attributes:
                txt_lines += 1
                attributeText += '{}: {}\n'.format(attribute, detected_attributes[attribute])
                    
    return annotations, happinessScore, attributeText

def makeAttributesDisplay(i, attributeText):
    from PIL import Image, ImageDraw, ImageFont

    path = '.\\attributeImages'
    img = Image.new('RGB', (900, 175), color = (73, 109, 137))

    d = ImageDraw.Draw(img)
    fnt = ImageFont.truetype("arial.ttf", 15)
    d.text((10,10), attributeText, font=fnt, fill=(255, 255, 0))

    img.save(path + '/attributes' + str(i) + '.jpg', 'JPEG')
    
def makePlot(i, xList, yList, happinessAvg):
    import matplotlib.pyplot as plt
    import numpy as np

    path = '.\\plotImages'

    def makeFig():
        # plt.scatter(xList,yList) # I think you meant this
        plt.plot(xList, yList)
        plt.legend([str(happinessAvg)], loc = 'upper left')
        ax = fig.add_subplot(111)
        ax.set_title('Live Customer Happiness Score')
        ax.set_xlabel('Frame Number')
        ax.set_ylabel('Happiness Score')
        #ax.text(0, 0, str(happinessAvg), verticalalignment='top', horizontalalignment = 'right', transform=ax.transAxes)

    plt.ion() # enable interactivity
    fig=plt.figure() # make a figure

    makeFig()      #The drawnow(makeFig) command can be replaced
    # plt.draw()     #with makeFig(); plt.draw()
    plt.savefig(path + '/plot' + str(i))
    plt.pause(0.001)


def show_similar_faces(image_1_path, image_1_face, image_2_path, image_2_faces, similar_faces):
    import matplotlib.pyplot as plt
    from PIL import Image, ImageDraw

    # Create a figure to display the results
    fig = plt.figure(figsize=(16, 6))

    # Show face 1
    img1 = Image.open(image_1_path)
    r = image_1_face.face_rectangle
    bounding_box = ((r.left, r.top), (r.left + r.width, r.top + r.height))
    draw = ImageDraw.Draw(img1)
    draw.rectangle(bounding_box, outline='magenta', width=5)
    a = fig.add_subplot(1,2,1)
    plt.axis('off')
    plt.imshow(img1)

    # get the matching face IDs
    matching_face_ids = list(map(lambda face: face.face_id, similar_faces))

    # Draw a rectangle around each similar face in image 2
    img2 = Image.open(image_2_path)
    a = fig.add_subplot(1,2,2)
    plt.axis('off')
    for face in image_2_faces:
        r = face.face_rectangle
        bounding_box = ((r.left, r.top), (r.left + r.width, r.top + r.height))
        draw = ImageDraw.Draw(img2)
        if face.face_id in matching_face_ids:
            draw.rectangle(bounding_box, outline='lightgreen', width=10)
            plt.annotate('Match!',(r.left, r.top + r.height + 15), backgroundcolor='white')
        else:
            draw.rectangle(bounding_box, outline='red', width=5)
    plt.imshow(img2)
    plt.show()

def show_recognized_faces(image_path, detected_faces, recognized_face_names):
    import matplotlib.pyplot as plt
    from PIL import Image, ImageDraw

    # Open an image
    img = Image.open(image_path)

    # Create a figure to display the results
    fig = plt.figure(figsize=(8, 6))

    if detected_faces:
        # If there are faces, how many?
        num_faces = len(recognized_face_names)
        caption = ' (' + str(num_faces) + ' faces recognized)'
        # Draw a rectangle around each detected face
        for face in detected_faces:
            r = face.face_rectangle
            bounding_box = ((r.left, r.top), (r.left + r.width, r.top + r.height))
            draw = ImageDraw.Draw(img)
            draw.rectangle(bounding_box, outline='magenta', width=5)
            if face.face_id in recognized_face_names:
                plt.annotate(recognized_face_names[face.face_id],
                             (r.left, r.top + r.height + 15), backgroundcolor='white')
        #a = fig.add_subplot(1,1,1)
        fig.suptitle(caption)

    plt.axis('off')
    plt.imshow(img)