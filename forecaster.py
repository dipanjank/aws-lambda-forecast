from fbprophet import Prophet
import pandas as pd


def make_forecast(data_dict):
    """
    Take daily data to train a Prophet model and return the forecast from
    ``data_dict['start_date']`` and ``data_dict['end_date']``. Dates expected in YYYY-MM-DD
    format.

    :param data_dict: The train data and the predict start and end dates.
    :return: The prediction result as a list of dictionaries, with keys 'date' and 'data'.
    """
    train_df = pd.DataFrame(data_dict['train_data'])
    if 'date' not in train_df.columns:
        raise ValueError('No "date" column provided.')
    if 'data' not in train_df.columns:
        raise ValueError('No "data" column provided.')

    # Prophet expects standard column names: "ds" for dates and "y" for data.
    train_df = train_df.rename({'data': 'y', 'date': 'ds'}, axis=1)

    predict_dates = pd.date_range(
        start=data_dict['start_date'],
        end=data_dict['end_date'],
        freq='D'
    )

    model = Prophet()
    model.fit(train_df)

    # DataFrame with just the "ds" column for the prediction dates.
    predict_df = pd.Series(data=predict_dates.values, name='ds').to_frame()
    predict_df = model.predict(predict_df)
    predict_cols = predict_df.loc[:, ['ds', 'yhat']]

    return [
        {'date': row['ds'].strftime('%Y-%m-%d'), 'data': row['yhat']}
            for _, row in predict_cols.iterrows()
    ]
