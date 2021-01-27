# aws-lambda-forecast
Demonstration of aws lambda: HTTP based time series forecasting service.

## Local Setup

```bash
 python3 -m venv venv
 source venv/bin/activate
 pip install -r requirements.txt
```

## Packaging for AWS Lambda

```bash
pip uninstall -y matplotlb

find "$VIRTUAL_ENV/lib64/python3.7/site-packages" -name "test" | xargs rm -rf
find "$VIRTUAL_ENV/lib64/python3.7/site-packages" -name "tests" | xargs rm -rf
rm -rf "$VIRTUAL_ENV/lib64/python3.7/site-packages/pystan/stan/src"
rm -rf "$VIRTUAL_ENV/lib64/python3.7/site-packages/pystan/stan/lib/stan_math/lib"
find "$VIRTUAL_ENV/lib64/python3.7/site-packages" -name "*.so" | xargs strip --strip-debug
```

Now prepare the "vendor" subdirectory:

```bash
mkdir vendor
cp -r $VIRTUAL_ENV/lib64/python3.7/site-packages/* vendor/
```