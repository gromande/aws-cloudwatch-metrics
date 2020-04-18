import boto3, random
from datetime import datetime, timedelta

def publish_metric(metric, server, timestamp):
    metric.put_data(
        Namespace=metric.namespace,
        MetricData=[
            {
                'MetricName': metric.metric_name,
                'Value': random.randint(1, 50),
                'Timestamp': timestamp,
                'Dimensions': [
                    {
                        'Name': 'Server',
                        'Value': server
                    }
                ]
            }
        ]
    )


cloudwatch = boto3.resource('cloudwatch')
metric = cloudwatch.Metric('Custom', 'LoginAttempts')

elapsed_time = 60
interval = 5
now = datetime.utcnow()
for i in range(0, elapsed_time, interval):
    timestamp = now - timedelta(minutes=elapsed_time) + timedelta(minutes=(i))
    publish_metric(metric, 'server1', timestamp)
    publish_metric(metric, 'server2', timestamp)
    publish_metric(metric, 'server3', timestamp)