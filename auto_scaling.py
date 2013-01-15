import boto
from boto.ec2.autoscale import LaunchConfiguration

conn = boto.connect_autoscale()
lc = LaunchConfiguration(name='my-launch_config', image_id='daas',
    key_name='mykey',
    security_groups=['daas'])
conn.create_launch_configuration(lc)

ag = AutoScalingGroup()

conn.get_all_groups()