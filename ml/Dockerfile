FROM jupyter/pyspark-notebook
MAINTAINER Ji, Ye

RUN pip install flask

COPY . .

EXPOSE 5000
CMD ["python", "predict.py"]
