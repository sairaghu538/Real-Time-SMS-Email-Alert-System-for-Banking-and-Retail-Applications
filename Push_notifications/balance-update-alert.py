def lambda_handler(event, context):
    customer_name = event.get('name')
    updated_balance = event.get('updated_balance')
    customer_phone = event.get('phone')

    # Send email notification
    sns.publish(
        TopicArn='arn:aws:sns:your-region:your-account-id:notifications-topic',
        Message=f'Hello {customer_name}, your account balance is now {updated_balance}.',
        Subject='Balance Update',
    )

    # Send SMS notification
    sns.publish(
        PhoneNumber=customer_phone,
        Message=f'Balance Update: Your account balance is now {updated_balance}.',
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Balance update alert sent successfully!')
    }
