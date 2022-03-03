from google.cloud import bigquery
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file(
    'config/foodpanda-342717-228e3e11ac49.json')

table_id = 'foodpanda-342717.Foodpanda_dataset.Foodpanda_Q2'

client = bigquery.Client(credentials=credentials)

job_config = bigquery.QueryJobConfig(destination=table_id)
job_config.write_disposition = "WRITE_TRUNCATE"

QUERY = (
    'SELECT country,COUNT(port_name) AS port_count '
    'FROM `bigquery-public-data.geo_international_ports.world_port_index` '
    'WHERE cargo_wharf = true '
    'GROUP BY country '
    'ORDER BY port_count DESC '
    'LIMIT 1 ')

query_job = client.query(QUERY,job_config=job_config)
rows = query_job.result()

for row in rows:
    print(row)

print("Query results loaded to the table {}".format(table_id))
