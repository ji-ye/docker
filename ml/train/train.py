from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *
from pyspark.ml import Pipeline, PipelineModel
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.feature import StringIndexer, VectorAssembler

spark = SparkSession.builder \
        .appName('train_ml_model') \
        .getOrCreate()

# I am using an abridged subset of Cato's 2017 Human Freedom Index
# Source here: https://www.cato.org/human-freedom-index
df = spark.read.csv("cato_2017_personal_freedom.csv", header='true')


# Function below adapted from:
# https://www.datacamp.com/community/tutorials/apache-spark-tutorial-machine-learning#load
def convertColumn(df, names, newType):
  for name in names:
     df = df.withColumn(name, df[name].cast(newType))
  return df


# Assign all column names to `columns`
columns = [
 'PERSONAL FREEDOM (Score)',
 'Rule of Law',
 'Security & Safety',
 'Movement',
 'Religion',
 'Association Assembly & Civil Society',
 'Expression & Information',
 'Identity & Relationships']

# Conver the `df` columns to `FloatType()`
df = convertColumn(df, columns, FloatType())

df = df.select('Countries',
 'PERSONAL FREEDOM (Score)',
 'Rule of Law',
 'Security & Safety',
 'Movement',
 'Religion',
 'Association Assembly & Civil Society',
 'Expression & Information',
 'Identity & Relationships')

df = df.na.drop()

PERSONAL_FREEDOM_AVG = 7.07
df = df.withColumn('PERSONAL FREEDOM (ABOVE AVERAGE)',
              (df['PERSONAL FREEDOM (Score)'] > PERSONAL_FREEDOM_AVG).cast('integer'))

inputs = ['Rule of Law',
 'Security & Safety',
 'Movement',
 'Religion',
 'Association Assembly & Civil Society',
 'Expression & Information',
 'Identity & Relationships']

feature_assembler = VectorAssembler(inputCols=inputs, outputCol="features")
label_indexer = StringIndexer(inputCol='PERSONAL FREEDOM (ABOVE AVERAGE)', outputCol="label")

lr = LogisticRegression()
pipeline = Pipeline(stages=[feature_assembler, label_indexer, lr])

model = pipeline.fit(df)
model.save("lrmodel")
