def lambda_handler(event, context):
    customer_name = event.get('name')
    promotion_details = event.get('promotion_details')
    customer_phone = event.get('phone')

    # Send email notification
    sns.publish(
        TopicArn='arn:aws:sns:your-region:your-account-id:notifications-topic',
        Message=f'Hello {customer_name}, check out our latest promotion: {promotion_details}.',
        Subject='Special Promotion Just for You!',
    )

    # Send SMS notification
    sns.publish(
        PhoneNumber=customer_phone,
        Message=f'Promo Alert: {promotion_details}',
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Promotion alert sent successfully!')
    }
