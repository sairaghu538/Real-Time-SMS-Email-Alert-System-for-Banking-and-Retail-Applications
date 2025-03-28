def lambda_handler(event, context):
    customer_name = event.get('name')
    transaction_type = event.get('transaction_type')
    transaction_amount = event.get('amount')
    customer_phone = event.get('phone')

    # Send email notification
    sns.publish(
        TopicArn='arn:aws:sns:your-region:your-account-id:notifications-topic',
        Message=f'You have successfully made a {transaction_type} of {transaction_amount}.',
        Subject='Transaction Alert',
    )

    # Send SMS notification
    sns.publish(
        PhoneNumber=customer_phone,
        Message=f'Transaction Alert: You made a {transaction_type} of {transaction_amount}.',
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Transaction alert sent successfully!')
    }
