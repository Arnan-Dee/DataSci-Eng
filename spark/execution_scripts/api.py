from flask import Flask, request
from flask_restful import Resource, Api
import mlflow
import mlflow.pytorch
import torch

app = Flask(__name__)
api = Api(app)

model = torch.hub.load("ultralytics/yolov5", "yolov5x6", pretrained=True)
model_uri = "runs:/{}/model".format("880e41ecfff24fd8b0961f87e0560e06")
loaded_model = mlflow.pytorch.load_model(model_uri)

class Predict(Resource):
    def post(self):
        image_name = request.form['data']
        classes = loaded_model(str(image_name)).pandas().xyxy[0].name.value_counts()
        car_count = classes["car"] if "car" in classes else 0
        return {"car_count": int(car_count)}

api.add_resource(Predict, '/')

if __name__ == '__main__':
    app.run()