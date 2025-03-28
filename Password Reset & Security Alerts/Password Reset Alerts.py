import json
import boto3

# Initialize SNS client
sns = boto3.client('sns')

def lambda_handler(event, context):
    """
    Handles password reset or security alerts by sending notifications via SNS.
    """
    user_name = event.get('name', 'User')
    event_type = event.get('event_type')  # e.g., "Password Reset", "Suspicious Login Attempt"
    customer_email = event.get('email')
    customer_phone = event.get('phone')

    # Define alert message
    if event_type == "Password Reset":
        message = (f"Hello {user_name}, a password reset request was made for your account. "
                   "If this was not you, please contact support immediately.")
        subject = "Password Reset Request"
    elif event_type == "Suspicious Login Attempt":
        message = (f"Security Alert: A suspicious login attempt was detected on your account. "
                   "If this was not you, please change your password and enable two-factor authentication.")
        subject = "Suspicious Login Attempt"
    else:
        message = f"Security Alert: {event_type} detected on your account. Please review your account security."
        subject = "Account Security Alert"

    # Send Email Notification
    sns.publish(
        TopicArn='arn:aws:sns:your-region:your-account-id:notifications-topic',
        Message=message,
        Subject=subject,
    )

    # Send SMS Notification
    if customer_phone:
        sns.publish(
            PhoneNumber=customer_phone,
            Message=message
        )

    return {
        'statusCode': 200,
        'body': json.dumps(f'Security alert for {event_type} sent successfully!')
    }
