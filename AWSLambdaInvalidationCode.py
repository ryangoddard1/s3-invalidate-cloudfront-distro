import boto3
import datetime  

def lambda_handler(event, context):
    cloudfront_client = boto3.client('cloudfront')
    distribution_id = 'distributionID' #replace distributionID


    timestamp = datetime.datetime.utcnow().strftime('%Y%m%d%H%M%S')

    invalidation_response = cloudfront_client.create_invalidation(
        DistributionId=distribution_id,
        InvalidationBatch={
            'Paths': {
                'Quantity': 1,
                'Items': ['/*']  
            },
            'CallerReference': timestamp
        }
    )

    return {
        'statusCode': 200,
        'body': 'Cache invalidation initiated with timestamp: {}'.format(timestamp)
    }