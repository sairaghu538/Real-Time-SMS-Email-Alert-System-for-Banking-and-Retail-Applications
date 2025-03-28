def lambda_handler(event, context):
    user_name = event.get('name')
    event_type = event.get('event_type')  # e.g., "Failed Login", "Password Reset"
    customer_phone = event.get('phone')

    # Send email notification
    sns.publish(
        TopicArn='arn:aws:sns:your-region:your-account-id:notifications-topic',
        Message=f'Alert: There was a {event_type} attempt for your account.',
        Subject='Security Alert',
    )

    # Send SMS notification
    sns.publish(
        PhoneNumber=customer_phone,
        Message=f'Security Alert: {event_type} attempt for your account.',
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Security alert sent successfully!')
    }
