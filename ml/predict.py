from pyspark.sql import SparkSession
from pyspark.ml import PipelineModel
from flask import Flask, request

spark = SparkSession.builder \
        .appName('prediction') \
        .getOrCreate()

model = PipelineModel.load("./train/lrmodel")
app = Flask(__name__)


@app.route('/', methods=['POST'])
def predict():
    f1 = float(request.form.get('feature1'))
    f2 = float(request.form.get('feature2'))
    f3 = float(request.form.get('feature3'))
    f4 = float(request.form.get('feature4'))
    f5 = float(request.form.get('feature5'))
    f6 = float(request.form.get('feature6'))
    f7 = float(request.form.get('feature7'))

    input_df = spark.createDataFrame(
        [["unknown", f1, f2, f3, f4, f5, f6, f7, ]],
        ['result',
         'Rule of Law',
         'Security & Safety',
         'Movement',
         'Religion',
         'Association Assembly & Civil Society',
         'Expression & Information',
         'Identity & Relationships'])

    prediction = model.transform(input_df).select("prediction").first()[0]

    if prediction == 1:
        return "This country is predicted to have a personal freedom score BELOW the world average (7.07), given the inputs."

    if prediction == 0:
        return "This country is predicted to have a personal freedom score ABOVE the world average (7.07), given the inputs."


if __name__ == "__main__":
    app.run(host="0.0.0.0")
