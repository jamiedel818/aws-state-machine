from chalice import Chalice

'''
event = {
    "operation": "addition",
    "data": {
        "x": 5,
        "y": 10
    }
}
'''
app = Chalice(app_name='aws-state-machine')

@app.lambda_function()
def addition(event, context):
    x, y = event['data']['x'], event['data']['y']
    result = x + y
    return {"result": result}

@app.lambda_function()
def subtraction(event, context):
    x, y = event['data']['x'], event['data']['y']
    result = x - y
    return {"result": result}

@app.lambda_function()
def multiplication(event, context):
    x, y = event['data']['x'], event['data']['y']
    result = x * y
    return {"result": result}

@app.lambda_function()
def division(event, context):
    x, y = event['data']['x'], event['data']['y']
    result = x / y
    return {"result": result}