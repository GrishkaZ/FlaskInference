import numpy as np
from PIL import Image
import json
import onnxruntime as ort

with open('model/labels.json') as f:
    LABELS = json.load(f)

ort_session = ort.InferenceSession('model/resnet18_imagenet.onnx')

def _transform(img):
    img = np.array(img.resize([256,256]))
    img = np.float32(img)/255
#     img -= np.array([0.485, 0.456, 0.406])
#     img /= np.array([0.229, 0.224, 0.225])
    return img.transpose(2,0,1)[None]

def classify(pil_img):
    outputs = ort_session.run(None, {ort_session.get_inputs()[0].name : _transform(pil_img)})
    return {'text' : LABELS[outputs[0][0].argmax()]}

