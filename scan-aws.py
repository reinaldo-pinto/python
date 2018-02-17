import boto3

ec2 = boto3.client('ec2')

filtered = 'status'
status = 'available'

volume = ec2.describe_volumes(Filters=[{'Name': filtered, 'Values': [status]}])

#declaring list:
#vols = []
print("\nVolumes without association the none resource:\n")
for i in volume['Volumes']:
    print("ID: " + i['VolumeId'] + "\tSize: " + str(i['Size']) + "G" + "\tStatus: " + i['State'])
    #is possible use list: 
    #vols.append(i['VolumeId'])
    #vols.append(i['Size'])
