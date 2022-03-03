from google.cloud import bigquery
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file(
    'config/foodpanda-342717-228e3e11ac49.json')

table_id = 'foodpanda-342717.Foodpanda_dataset.Foodpanda_Q1'

client = bigquery.Client(credentials=credentials)

job_config = bigquery.QueryJobConfig(destination=table_id)
job_config.write_disposition = "WRITE_TRUNCATE"

# An initial query seen below in the comments was run to determine the port_latitude and port_longitude of the "JURONG ISLAND" port that is in country "SG".
# For "JURONG ISLAND" port, the longitude=103.733333 and latitude=1.283333. These values were then used as the origin location to find other ports that are nearby.
#
# QUERY = (
#     'SELECT port_name,country,port_latitude,port_longitude '
#     'FROM `bigquery-public-data.geo_international_ports.world_port_index` '
#     'WHERE port_name = "JURONG ISLAND" AND country = "SG" ') 

QUERY = (
    'SELECT port_name,SQRT(POW((1.283333-port_latitude),2)+POW((103.733333-port_longitude),2)) AS distance_in_meters '
    'FROM `bigquery-public-data.geo_international_ports.world_port_index` '
    'WHERE port_name<>"JURONG ISLAND"'
    'ORDER BY distance_in_meters ASC '
    'LIMIT 5')

query_job = client.query(QUERY, job_config=job_config)
rows = query_job.result()

for row in rows:
    print(row)

print("Query results loaded to the table {}".format(table_id))
