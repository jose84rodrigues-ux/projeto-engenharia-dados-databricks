# Databricks notebook source
# DBTITLE 1,List available catalogs
# Public DBFS root (/FileStore) is disabled in this workspace.
# Use Unity Catalog Volumes for file storage instead.

# Example: List catalogs and schemas to find available Volumes
print("Available catalogs:")
spark.sql("SHOW CATALOGS").display()

print("\nTo list files in a Volume, use a path like:")
print("/Volumes/<catalog>/<schema>/<volume>/")

# Example (replace with your actual volume path):
# display(dbutils.fs.ls("/Volumes/main/default/my_volume/"))

# COMMAND ----------

# DBTITLE 1,Show tables in main.default
# MAGIC %sql
# MAGIC SHOW TABLES IN samples.nyctaxi

# COMMAND ----------

# MAGIC %sql
# MAGIC SHOW CATALOGS;
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC USE CATALOG workspace;
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC SHOW SCHEMAS;
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC USE SCHEMA default;
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT current_catalog(), current_schema();
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE VOLUME IF NOT EXISTS bronze;
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE VOLUME bronze;
# MAGIC

# COMMAND ----------

display(dbutils.fs.ls("/Volumes/workspace/default/bronze"))
