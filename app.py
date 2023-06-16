import os
from flask import Flask, jsonify, request
from classifier import classify
from PIL import Image

app = Flask(__name__)

@app.post('/predict')
def predict():
    # data = request. хз чо дальше
    ##тут какая-то хуйня чтоб картинку достать и засунуть в PIL.Image
    #try:
    #    class_json= jsonify(classify(img))
    #except Exception as e:
    #    #хуй знает как лучше экспетион вернуть
    #return class_json # дальше не знаю
    pass



if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port = port)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
