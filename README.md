#  Projeto de Engenharia de Dados com Databricks

##  Objetivo
Desenvolver um pipeline de dados completo utilizando arquitetura medalhão (Bronze, Silver e Gold), com foco em boas práticas de engenharia de dados.

---

##  Arquitetura

O projeto segue o modelo:

CSV → Bronze → Silver → Gold → BI

---

##  Camadas

###  Bronze (Dados Brutos)
- Ingestão de arquivo CSV
- Armazenamento em Delta Lake
- Inclusão de metadados (ingestion_timestamp, source_file)

---

###  Silver (Dados Tratados)
- Remoção de duplicidades
- Tratamento de valores nulos
- Padronização de colunas
- Conversão de tipos
- Criação de coluna derivada (total_value)

---

###  Gold (Dados Analíticos)
- Criação de KPIs:
  - Faturamento total
  - Ticket médio
  - Quantidade vendida
- Agregações por tempo e produto

---

##  Modelagem Dimensional

Criação de modelo Star Schema:

- Fato: fato_vendas
- Dimensões:
  - dim_produto
  - dim_cliente
  - dim_tempo

---

##  Tecnologias Utilizadas

- Databricks
- Apache Spark
- Delta Lake
- Unity Catalog

---

##  Diferenciais

- Uso de arquitetura medalhão
- Implementação de carga incremental (MERGE)
- Otimização com OPTIMIZE e ZORDER
- Boas práticas de engenharia de dados

---

##  Possível uso

Os dados podem ser consumidos por ferramentas como Power BI para análise de vendas.

---

##  Autor

José Rodrigues


