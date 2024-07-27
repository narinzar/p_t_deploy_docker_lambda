import numpy as np

def handler(event, context):
    # Generate a random 3D array with dimensions 5x4x4
    arr = np.random.randint(1, 100, size=(5, 4, 4))
    
    return {
        'statusCode': 200,
        'body': {
            "message": "Welcome to Lambda! Your random array awaits.",
            "array": arr.tolist()
        }
    }
