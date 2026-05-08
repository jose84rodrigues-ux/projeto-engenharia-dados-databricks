# Databricks notebook source

# ============================================
# MODELO DIMENSIONAL
# Objetivo:
# Construção das dimensões e tabela fato
# para modelagem analítica Star Schema.
# ============================================

# COMMAND ----------

from pyspark.sql.functions import *

# COMMAND ----------

df_modelo = spark.table("workspace.default.silver_vendas")

# COMMAND ----------

dim_cliente = (
    df_modelo
    .select("cliente")
    .distinct()
)

# COMMAND ----------

dim_produto = (
    df_modelo
    .select("produto")
    .distinct()
)

# COMMAND ----------

dim_tempo = (
    df_modelo
    .select("data_venda")
    .distinct()
)

# COMMAND ----------

fato_vendas = (
    df_modelo.select(
        "cliente",
        "produto",
        "data_venda",
        "valor_venda",
        "quantidade"
    )
)

# COMMAND ----------

(
    dim_cliente.write.format("delta")
    .mode("overwrite")
    .saveAsTable("workspace.default.dim_cliente")
)

# COMMAND ----------

(
    dim_produto.write.format("delta")
    .mode("overwrite")
    .saveAsTable("workspace.default.dim_produto")
)

# COMMAND ----------

(
    dim_tempo.write.format("delta")
    .mode("overwrite")
    .saveAsTable("workspace.default.dim_tempo")
)

# COMMAND ----------

(
    fato_vendas.write.format("delta")
    .mode("overwrite")
    .saveAsTable("workspace.default.fato_vendas")
)
