# Databricks notebook source

# ============================================
# CAMADA BRONZE
# Objetivo:
# Configuração inicial do ambiente Lakehouse,
# validação de catálogos e criação do volume
# Bronze para armazenamento dos dados brutos.
# ============================================

# COMMAND ----------

# DBTITLE 1,Listar catálogos disponíveis
print("Available catalogs:")
spark.sql("SHOW CATALOGS").display()

print("\nTo list files in a Volume, use a path like:")
print("/Volumes/<catalog>/<schema>/<volume>/")

# COMMAND ----------

# DBTITLE 1,Mostrar tabelas disponíveis
# MAGIC %sql
# MAGIC SHOW TABLES IN samples.nyctaxi

# COMMAND ----------

# DBTITLE 1,Mostrar catálogos
# MAGIC %sql
# MAGIC SHOW CATALOGS;

# COMMAND ----------

# DBTITLE 1,Definir catálogo workspace
# MAGIC %sql
# MAGIC USE CATALOG workspace;

# COMMAND ----------

# DBTITLE 1,Mostrar schemas disponíveis
# MAGIC %sql
# MAGIC SHOW SCHEMAS;

# COMMAND ----------

# DBTITLE 1,Definir schema default
# MAGIC %sql
# MAGIC USE SCHEMA default;

# COMMAND ----------

# DBTITLE 1,Validar catálogo e schema atuais
# MAGIC %sql
# MAGIC SELECT current_catalog(), current_schema();

# COMMAND ----------

# DBTITLE 1,Criar volume Bronze
# MAGIC %sql
# MAGIC CREATE VOLUME IF NOT EXISTS bronze;

# COMMAND ----------

# DBTITLE 1,Listar arquivos do volume Bronze
display(dbutils.fs.ls("/Volumes/workspace/default/bronze"))
