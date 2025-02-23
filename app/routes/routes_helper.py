from flask import jsonify, make_response, request, abort

# handle error message
def error_message(message, status_code):
    abort(make_response(jsonify(dict(message=message)), status_code))

# handle invalid id 
def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        error_message(f"{cls.__name__} {model_id} not found", 400)
        
    model = cls.query.get(model_id)
    if not model:
        error_message(f"{cls.__name__} {model_id} not found", 404)

    return model


def validate_input_data(cls, request_body):
    try:
        return cls.from_dict(request_body)
    except KeyError:
        abort(make_response(jsonify(dict(details="Invalid data")), 400))


