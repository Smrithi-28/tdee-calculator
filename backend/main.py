import functions_framework
from flask import jsonify, request

@functions_framework.http
def tdee_calculator(request):
    # Handle CORS preflight
    if request.method == 'OPTIONS':
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST, OPTIONS',
            'Access-Control-Allow-Headers': 'Content-Type',
        }
        return ('', 204, headers)

    # Handle POST request
    data = request.get_json()

    try:
        weight = float(data['weight'])
        height = float(data['height'])
        age = int(data['age'])
        gender = data['gender'].lower()
        activity = float(data['activity'])

        # BMR and TDEE Calculation
        if gender == 'male':
            bmr = 10 * weight + 6.25 * height - 5 * age + 5
        else:
            bmr = 10 * weight + 6.25 * height - 5 * age - 161

        tdee = bmr * activity
        result = {'tdee': round(tdee, 2)}

    except:
        result = {'error': 'Invalid input. Please check all values.'}

    response = jsonify(result)
    response.headers.set('Access-Control-Allow-Origin', '*')
    return response

