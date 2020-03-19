from keras.applications.imagenet_utils import preprocess_input, decode_predictions
from keras.models import load_model
from keras.preprocessing import image
from keras.applications.resnet50 import ResNet50
from starlette.applications import Starlette
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware
from pathlib import Path
import uvicorn, aiohttp, asyncio
import base64, sys, numpy as np
import cv2

path = Path(__file__).parent
model_file_url = 'https://github.com/guramritpalsaggu/Medical_Image_Analysis/blob/master/flask-app-live/app/models/malaria2.h5?raw=true' #DIRECT / RAW DOWNLOAD URL HERE!'
model_file_name = 'malaria2'


app = Starlette()
app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_headers=['X-Requested-With', 'Content-Type'])
app.mount('/static', StaticFiles(directory='static'))

MODEL_PATH = path/'models'/f'{model_file_name}.h5'
IMG_FILE_SRC = 'static/saved_image.png'
PREDICTION_FILE_SRC = path/'static'/'predictions.txt'

async def download_file(url, dest):
    if dest.exists(): return
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.read()
            with open(dest, 'wb') as f: f.write(data)

async def setup_model():
    #UNCOMMENT HERE FOR CUSTOM TRAINED MODEL
    # await download_file(model_file_url, MODEL_PATH)
    model = load_model(MODEL_PATH) # Load your Custom trained model
    model._make_predict_function()
    # model = ResNet50(weights='imagenet') # COMMENT, IF you have Custom trained model
    return model

# Asynchronous Steps
loop = asyncio.get_event_loop()
tasks = [asyncio.ensure_future(setup_model())]
model = loop.run_until_complete(asyncio.gather(*tasks))[0]
loop.close()

@app.route("/upload", methods=["POST"])
async def upload(request):
    data = await request.form()
    img_bytes = (data["img"])
    bytes = base64.b64decode(img_bytes)
    with open(IMG_FILE_SRC, 'wb') as f: f.write(bytes)
    return model_predict(IMG_FILE_SRC, model)

def model_predict(img_path, model):
    result = [];
    img = cv2.imread(img_path)
    img = cv2.resize(img, dsize=(125, 125), interpolation=cv2.INTER_CUBIC)
    kernel = np.array([[0,-1,0],[-1,6,-1],[0,-1,0]])
    img = cv2.filter2D(img, -1, kernel)
    img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
    img_yuv[:, :, 0] = cv2.equalizeHist(img_yuv[:, :, 0])
    x = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2RGB)
    x = np.expand_dims(x/255., axis=0)
    # x = preprocess_input(np.expand_dims(image.img_to_array(img), axis=0))
    # predictions = decode_predictions(model.predict(x), top=3)[0] # Get Top-3 Accuracy
    # for p in predictions: _,label,accuracy = p; result.append((label,accuracy))
    predictions = model.predict(x)
    if predictions <= 0.5:
        result.append('parasitic')
        result.append(str(1-predictions))
    else:
        result.append('normal')
        result.append(str(predictions))
    result_html1 = path/'static'/'result1.html'
    result_html2 = path/'static'/'result2.html'
    result_html = str(result_html1.open().read() +str(result) + result_html2.open().read())
    return HTMLResponse(result_html)

@app.route("/")
def form(request):
    index_html = path/'static'/'index.html'
    return HTMLResponse(index_html.open().read())

if __name__ == "__main__":
    if "serve" in sys.argv: uvicorn.run(app, host="0.0.0.0", port=8080)
