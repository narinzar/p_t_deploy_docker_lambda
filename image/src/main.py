import numpy as np

def handler(event, context):
    arr = np.random.rand(10, 3, 3)   
    return {
        'statusCode': 200,
        'body': {
            "message": 'Hello from Lambda!',
            "array": arr.tolist()
        }
    }
