import json
import shutil
import joblib


def lambda_handler(event, context):
    try:
        shutil.copy("/var/task/lr_stress_tfidf.joblib", "/tmp/lr_stress_tfidf.joblib")
        shutil.copy("/var/task/train_vectorizer.joblib", "/tmp/train_vectorizer.joblib")
        
        lr = joblib.load("/tmp/lr_stress_tfidf.joblib")        
        vectorizer = joblib.load("/tmp/train_vectorizer.joblib")
        
        # Parse input from API Gateway
        body = json.loads(event["body"])
        new_sentence = body.get("text", "")

        if not new_sentence:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "No text provided."}),
            }

        new_sentence_tfidf = vectorizer.transform([new_sentence])

        new_prediction = lr.predict(new_sentence_tfidf)

        predicted_label = "stress" if new_prediction[0] == 1 else "not stress"

        return {"statusCode": 200, "body": json.dumps({"prediction": predicted_label})}

    except Exception as e:
        return {"statusCode": 500, "body": json.dumps({"error": str(e)})}
