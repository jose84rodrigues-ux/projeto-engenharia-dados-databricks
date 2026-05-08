# Databricks notebook source

# ============================================
# CAMADA GOLD
# Objetivo:
# Criar agregações e KPIs analíticos para
# consumo em dashboards e análises.
# ============================================

# COMMAND ----------

from pyspark.sql.functions import *

# COMMAND ----------

df_gold = spark.table("workspace.default.silver_vendas")

# COMMAND ----------

gold_vendas_produto = (
    df_gold.groupBy("produto")
    .agg(
        sum("valor_venda").alias("total_vendas"),
        sum("quantidade").alias("total_quantidade")
    )
)

# COMMAND ----------

gold_vendas_cliente = (
    df_gold.groupBy("cliente")
    .agg(
        sum("valor_venda").alias("total_vendas_cliente")
    )
)

# COMMAND ----------

gold_vendas_tempo = (
    df_gold.groupBy("data_venda")
    .agg(
        sum("valor_venda").alias("total_vendas_dia")
    )
)

# COMMAND ----------

(
    gold_vendas_produto.write.format("delta")
    .mode("overwrite")
    .saveAsTable("workspace.default.gold_vendas_produto")
)

# COMMAND ----------

(
    gold_vendas_cliente.write.format("delta")
    .mode("overwrite")
    .saveAsTable("workspace.default.gold_vendas_cliente")
)

# COMMAND ----------

(
    gold_vendas_tempo.write.format("delta")
    .mode("overwrite")
    .saveAsTable("workspace.default.gold_vendas_tempo")
)
