import boto
from boto.ec2.autoscale import LaunchConfiguration
from boto.ec2.autoscale import AutoScalingGroup
from boto.ec2.autoscale import ScalingPolicy
from boto.ec2.cloudwatch import MetricAlarm

# conf
conn = boto.connect_autoscale()
lc = LaunchConfiguration(name='my-launch_config', image_id='ami-7959d210',
    key_name='mykey',
    security_groups=['daas'])
conn.create_launch_configuration(lc)

# scaling group
ag = AutoScalingGroup(group_name='my-group', availability_zones=['us-east-1a'],
    launch_config=lc, min_size=1, max_size=2)
conn.create_auto_scaling_group(ag)

# scaling policy
scale_up_policy = ScalingPolicy(name='scale_up', adjustment_type='ChangeInCapacity',
    as_name='my-group', scaling_adjustment=1, cooldown=300)

scale_down_policy = ScalingPolicy(name='scale_down', adjustment_type='ChangeInCapacity',
    as_name='my-group', scaling_adjustment=-1, cooldown=300)
conn.create_scaling_policy(scale_up_policy)
conn.create_scaling_policy(scale_down_policy)


# cloudwatch alarm
cloudwatch = boto.connect_cloudwatch()
alarm_dimensions = {"AutoScalingGroupName": 'my-group'}
scale_up_alarm = MetricAlarm(
    name='scale_up_on_sqs', namespace='AWS/SQS',
    metric='ApproximateNumberOfMessagesVisible', statistic='Average',
    comparison='>', threshold='15',
    period='300', evaluation_periods='5',
    alarm_actions=[scale_up_policy],
    dimensions=alarm_dimensions)
cloudwatch.create_alarm(scale_up_alarm)

scale_down_alarm = MetricAlarm(
    name='scale_down_on_sqs', namespace='AWS/SQS',
    metric='ApproximateNumberOfMessagesVisible', statistic='Average',
    comparison='<', threshold='10',
    period='300', evaluation_periods='5',
    alarm_actions=[scale_down_policy],
    dimensions=alarm_dimensions)
cloudwatch.create_alarm(scale_up_alarm)

# conn.get_all_groups()[0].shutdown_instances()
# conn.delete_auto_scaling_group('my-group')
# conn.delete_launch_configuration('my-launch_config')
