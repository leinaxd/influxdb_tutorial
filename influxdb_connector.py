from influxdb_client import InfluxDBClient
from datetime import datetime

#Deprecated
#Setup database
# host        = 'localhost'
# port        = 8086
# user        = 'admin'
# password    = 'Password1'
# db_name     = 'dev'

# client = InfluxDBClient(host, port, user, password, db_name)


import os, time
from dotenv import load_dotenv
load_dotenv()

def get_client(verbose=False)->InfluxDBClient:
    INFLUXDB_TOKEN  = os.getenv('INFLUXDB_TOKEN')
    INFLUXDB_URL    = os.getenv('INFLUXDB_URL')
    org = 'tron'
    # client = InfluxDBClient(url=INFLUXDB_URL, 
    #                         token=INFLUXDB_TOKEN, 
    #                         org=org)
    client = InfluxDBClient.from_env_properties()

    if verbose:
        print(f'InfluxDB {client.version()}:')
        print(f'\t{client.url}')
        print(f'\t{client.org}')
    return client


from influxdb_client.client.write.point     import Point
from influxdb_client.domain.write_precision import WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
def write_data(client:InfluxDBClient):
    bucket = 'test'
    write_api  = client.write_api(write_options=SYNCHRONOUS)
    for value in range(5):
        point = (
            Point('Measurement_1')
            .tag('tagname_1', 'tagvalue_1')
            .field('field_1', value)
        )
        write_api.write(bucket=bucket, 
                        org='tron',
                        record=point)
        time.sleep(1) #separate points by 1 sec

def read_data(client:InfluxDBClient):
    read_api = client.query_api()
    query = '''from(bucket: "test")
                |> range(start: -30m)
                |> filter(fn: (r) => r._measurement=="Measurement_1")
            '''
    tables = read_api.query(query, org='tron')
    for table in tables:
        for record in table.records:
            print(record)

def aggregate_data(client:InfluxDBClient):
    read_api = client.query_api()
    query = '''from(bucket: "test")
                |> range(start: -30m)
                |> mean()
            '''
    tables = read_api.query(query, org='tron')
    for table in tables:
        for record in table.records:
            print(record)


def list_databases(client:InfluxDBClient):
    query   = 'SHOW DATABASES'
    # query   = 'SHOW BUCKETS'
    result  = client.query_api().query(query)
    return result

if __name__ == '__main__':
    DEBUG  = True
    client = get_client(verbose=DEBUG)
    # write_data(client)
    # read_data(client)
    # aggregate_data(client)


    # databases   = list_databases(client)
    # print(databases)
    