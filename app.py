import json

from chalice import Chalice

from forecaster import prophet_forecast

app = Chalice(app_name='prophet_forecaster')


@app.route('/prophet_forecast', methods=['POST'])
def forecast():
    forecast_data = app.current_request.json_body
    data_dict = json.loads(forecast_data)
    result = prophet_forecast(data_dict)
    return json.dumps(result)
