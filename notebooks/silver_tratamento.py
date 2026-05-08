# Databricks notebook source

# ============================================
# CAMADA SILVER
# Objetivo:
# Realizar limpeza, padronização e tratamento
# dos dados da camada Bronze.
# ============================================

# COMMAND ----------

from pyspark.sql.functions import *
from pyspark.sql.types import *

# COMMAND ----------

df_silver = spark.table("workspace.default.bronze_vendas")

# COMMAND ----------

df_silver = (
    df_silver
    .dropDuplicates()
    .dropna()
)

# COMMAND ----------

df_silver = (
    df_silver
    .withColumn("valor_venda", col("valor_venda").cast("double"))
    .withColumn("quantidade", col("quantidade").cast("integer"))
    .withColumn("data_venda", to_date(col("data_venda")))
)

# COMMAND ----------

df_silver = df_silver.filter(col("valor_venda") >= 0)

# COMMAND ----------

display(df_silver)

# COMMAND ----------

(
    df_silver.write.format("delta")
    .mode("overwrite")
    .saveAsTable("workspace.default.silver_vendas")
)

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM workspace.default.silver_vendas;
