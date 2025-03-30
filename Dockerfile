FROM python:3.12-slim AS builder

RUN pip install --no-cache-dir joblib scikit-learn

FROM public.ecr.aws/lambda/python:3.12

COPY --from=builder /usr/local/lib/python3.12/site-packages /var/task

COPY lr_stress_tfidf.joblib /var/task/
COPY train_vectorizer.joblib /var/task/
COPY stress_model.py /var/task/

CMD ["stress_model.lambda_handler"]
