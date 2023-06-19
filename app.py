import os
import io
import uuid 
import re 
from flask import Flask, request, url_for, redirect, render_template
from classifier import classify
from PIL import Image

uploadFolder = 'static/upload'
app = Flask(__name__)
app.config['uploadFolder'] = uploadFolder


@app.get('/')
def index():
    return render_template("upload-form.html")

@app.route("/upload", methods=["POST"])
def upload():
    if 'image' not in request.files:
        return 'there is no image in form!'
    
    image = request.files['image'] 
    
    extension = re.search(r"\.(png|jpg|jpeg)", fileExtension(image.filename)) 
    
    if not extension[0]:
        return 'invalid Extension'
    
    filename = str(uuid.uuid1()) + extension[0]

    image.save(os.path.join(uploadFolder, filename))
    
    return redirect('class/'+filename.replace('.', '%2E'), 301)


@app.get('/class/<filename>')
def image(filename): 
    
    imageSrc = url_for('static', filename='upload/'+filename)
    
    try:
        pilImage = Image.open('.'+imageSrc)
        result = classify(pilImage)
        pilImage.close()
    except Exception:
        return 'not found'
    
    return render_template("result.html", data=result, imageSrc=imageSrc)

def fileExtension(name):
    (_, extension) = os.path.splitext(name)
    return extension.lower()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port = port)
