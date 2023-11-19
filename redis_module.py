import redis
import pickle

# Connect to Redis
r = redis.Redis(host='localhost', port=6379)

# Store a trained machine learning model in Redis
model = trained_machine_learning_model()
model_bytes = pickle.dumps(model)
r.set('ml_model', model_bytes)

# Retrieve the model from Redis
model_bytes = r.get('ml_model')
if model_bytes:
    model = pickle.loads(model_bytes)
    prediction = model.predict(data)
    print(f"Prediction: {prediction}")
