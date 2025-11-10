def lambda_handler(event, context):
    print('hello')
    print('hello2')
    return {
        'statusCode': 200,
        'body': 'hello'
    }
