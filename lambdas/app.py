import random
import json
import boto3
from chalice import Chalice
from chalicelib.credentials import lambda_invoker_arn
from botocore.exceptions import ClientError


'''
Sample Event

event = {
    'operation': 'addition',
    'data': {
        'x': 5,
        'y': 10
    }
}
'''
app = Chalice(app_name='aws-state-machine')

# Add x + y from event
@app.lambda_function()
def addition(event, context):
    x, y = event['data']['x'], event['data']['y']
    result = x + y
    return json.dumps(
        {'result': result}
    )

# Subtract x - y from event
@app.lambda_function()
def subtraction(event, context):
    x, y = event['data']['x'], event['data']['y']
    result = x - y
    return json.dumps(
        {'result': result}
    )

# Multiply x - y from event
@app.lambda_function()
def multiplication(event, context):
    x, y = event['data']['x'], event['data']['y']
    result = x * y
    return json.dumps(
        {'result': result}
    )

# Dividide x - y from event
@app.lambda_function()
def division(event, context):
    x, y = event['data']['x'], event['data']['y']
    result = x / y
    return json.dumps(
        {'result': result}
    )


@app.route('/invoke', methods=['POST'])
def step_function_invoker():
    client = boto3.client('stepfunctions')

    function_input = json.dumps(app.current_request.json_body)

    try:
        step_function = client.start_execution(
            stateMachineArn=f'{lambda_invoker_arn}',
            name=f'invocation-{random.randint(1000, 9999)}',
            input=function_input
        )
    
    except ClientError as e:
        return json.dumps(
            {
                'Status Code': 500,
                'message':f'Step function invocation failed: {e}'
            }
        )

    return json.dumps(
        {
            'Status Code': 200, 
            'Response': f'{step_function}'
        }
    ) 

