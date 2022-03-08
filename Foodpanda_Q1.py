from google.cloud import bigquery
from google.oauth2 import service_account

# Change the path to the location of the service account key .json file
credentials = service_account.Credentials.from_service_account_file(
    'path_of_service_account_key.json')

client = bigquery.Client(credentials=credentials)

# Change the table_id accordingly
table_id = 'Bigqueryconnection.test-project.table1'

job_config = bigquery.QueryJobConfig(destination=table_id)
job_config.write_disposition = "WRITE_TRUNCATE"

# Example of a query below
QUERY = (
    'SELECT * '
    'FROM `bigquery-public-data.geo_international_ports.world_port_index` '
    'WHERE port_name<>"JURONG ISLAND"'
    'ORDER BY country ASC '
    'LIMIT 1')

query_job = client.query(QUERY, job_config=job_config)
rows = query_job.result()

# To print the results on your python IDE for referencing
for row in rows:
    print(row)

# To import the data into your Bigquery project with the table_id
print("Query results loaded to the table {}".format(table_id))
