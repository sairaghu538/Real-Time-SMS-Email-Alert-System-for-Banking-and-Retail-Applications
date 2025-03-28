import json
import boto3

sns = boto3.client('sns')

def lambda_handler(event, context):
    customer_name = event.get('name')
    customer_email = event.get('email')
    customer_phone = event.get('phone')

    # Send email notification
    sns.publish(
        TopicArn='arn:aws:sns:your-region:your-account-id:notifications-topic',
        Message=f'Welcome {customer_name}, your account has been successfully created!',
        Subject='Account Creation - Welcome!',
    )

    # Send SMS notification
    sns.publish(
        PhoneNumber=customer_phone,
        Message=f'Hello {customer_name}, your account has been created. Welcome!',
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Account creation notifications sent successfully!')
    }
