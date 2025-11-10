def lambda_handler(event, context):
    print('hello')  # ここを変更
    return {
        'statusCode': 200,
        'body': 'hello'
    }
