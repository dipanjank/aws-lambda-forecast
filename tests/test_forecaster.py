import pandas as pd
import numpy as np

from forecaster import prophet_forecast


def test_constant_forecast():
    train_data = [
        {
            'date': f'2020-01-{str(n).zfill(2)}',
            'data': 10.0
        }
        for n in range(1, 31+1)
    ]

    data_dict = {
        'train_data': train_data,
        'start_date': '2020-02-01',
        'end_date': '2020-02-29'
    }
    actual = pd.DataFrame(prophet_forecast(data_dict)).sort_index(axis=1)
    expected = pd.DataFrame([{
        'date': f'2020-02-{str(n).zfill(2)}',
        'data': 10.0
    } for n in range(1, 29+1)]).sort_index(axis=1)
    pd.testing.assert_frame_equal(actual, expected, atol=1E-4)


def test_seasonal_forecast():
    train_dates = [f'2020-01-{str(n).zfill(2)}' for n in range(1, 31 + 1)]
    train_data = np.sin(np.linspace(start=0, stop=8 * np.pi, num=31))
    train_data = [{'date': d, 'data': v} for d, v in zip(train_dates, train_data)]

    data_dict = {
        'train_data': train_data,
        'start_date': '2020-02-01',
        'end_date': '2020-02-04'
    }
    actual = pd.DataFrame(prophet_forecast(data_dict)).sort_index(axis=1)
    expected = pd.DataFrame(
        data=[
            ["2020-02-01", 0.64834],
            ["2020-02-02", 0.16212],
            ["2020-02-03", -0.5645],
            ["2020-02-04", -1.0507],
        ],
        columns=['date', 'data']).sort_index(axis=1)

    pd.testing.assert_frame_equal(actual, expected, atol=1E-3)
