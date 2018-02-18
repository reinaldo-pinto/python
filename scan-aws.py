import boto3
import os

bucket = os.environ['s3_bucket']
filtered = os.environ['type_filtered']
status = os.environ['status_disk']
region = os.environ['region']

ec2 = boto3.setup_default_session(region_name=region)
ec2 = boto3.client('ec2')
s3_service = boto3.resource('s3')

def lambda_handler(event, context):

    volume = ec2.describe_volumes(Filters=[{'Name': filtered, 'Values': [status]}])

    vol_list = []
    for i in volume['Volumes']:
        data_list = {"ID": i['VolumeId'],"Size": str(i['Size'])+"G", "Status": i['State']}
        vol_list.append(data_list)

    result = {"Volumes": vol_list}
    print("\nVolumes without association the none resource:\n")
    print(result)

    pathfile_add_region = '/tmp/' + region
    pathfile = pathfile_add_region+'_volumes.txt'
    arquivo = open(pathfile, 'w')
    arquivo.write(str(result))
    arquivo.close()

    s3_file = region + '_volumes.txt'
    s3_service.Bucket(bucket).upload_file(pathfile, s3_file)
