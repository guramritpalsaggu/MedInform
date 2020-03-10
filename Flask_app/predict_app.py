import base64
import numpy as np
import io
from PIL import Image
import keras
from keras import backend as K
from keras.models import Sequential
from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import img_to_array
from flask import request
from flask import jsonify
from flask import Flask

app = Flask(__name__)

  def load_tensorflow_shared_session(self):
        """ Load a Tensorflow/Keras shared session """
        # LP: create a config by gpu cpu backend
        if os.getenv('HAS_GPU', '0') == '1':
            config = tf.ConfigProto(
                device_count={'GPU': 1},
                intra_op_parallelism_threads=1,
                allow_soft_placement=True
            )
            config.gpu_options.allow_growth = True
            config.gpu_options.per_process_gpu_memory_fraction = 0.6
        else:
            config = tf.ConfigProto(
                intra_op_parallelism_threads=1,
                allow_soft_placement=True
            )
        # LP: create session by config
        self.tf_session = tf.Session(config=config)

        return self.tf_session

        

def get_model():
    global model
    set_session(session)
    model = load_model('VGG16_cats_and_dogs.h5')
    model._make_predict_function()
    print(" * Model loaded!")


def preprocess_image(image, target_size):
    if image.mode != "RGB":
        image = image.convert("RGB")
    image = image.resize(target_size)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    return image

print(" * Loading Keras model...")
get_model()

@app.route("/predict", methods=["POST"])
def predict():
    message = request.get_json(force=True)
    encoded = message['image']
    decoded = base64.b64decode(encoded)
    image = Image.open(io.BytesIO(decoded))
    processed_image = preprocess_image(image, target_size=(224, 224))
    
    prediction = model.predict(processed_image).tolist()
    console.log(prediction)
    response = {
        'prediction': {
            'dog': prediction[0][0],
            'cat': prediction[0][1]
        }
    }
    return jsonify(response)

  