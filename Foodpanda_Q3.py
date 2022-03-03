from google.cloud import bigquery
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file(
    'config/foodpanda-342717-228e3e11ac49.json')

table_id = 'foodpanda-342717.Foodpanda_dataset.Foodpanda_Q3'

client = bigquery.Client(credentials=credentials)

job_config = bigquery.QueryJobConfig(destination=table_id)
job_config.write_disposition = "WRITE_TRUNCATE"

QUERY = (
    'SELECT temptable.country, temptable.port_name, temptable.port_latitude, temptable.port_longitude FROM ('
    '   SELECT country, port_name, port_latitude, port_longitude, '
    '   SQRT(POW((port_latitude-32.610982), 2)+POW((port_longitude - (-38.706256)), 2)) AS distance '
    '   FROM `bigquery-public-data.geo_international_ports.world_port_index`'
    '   WHERE provisions = true AND water = true AND fuel_oil = true AND diesel = true'
    '   ORDER BY distance ASC)temptable '
    'LIMIT 1 ')

query_job = client.query(QUERY, job_config=job_config)
rows = query_job.result()

for row in rows:
    print(row)

print("Query results loaded to the table {}".format(table_id))
