from flask import Flask, render_template, request, jsonify
import numpy as np
import tensorflow as tf
from tensorflow import keras
from sklearn.preprocessing import MinMaxScaler

app = Flask(__name__)

# 📌 ⚡ Génération de données et entraînement de l'IA ⚡ 📌
num_data = 100000
historique = np.random.randint(0, 37, (num_data, 3))
resultats = np.random.randint(0, 37, (num_data, 1))

# Normalisation des données
scaler = MinMaxScaler()
historique_norm = scaler.fit_transform(historique)
resultats_norm = scaler.fit_transform(resultats)

# Création du modèle IA
model = keras.Sequential([
    keras.layers.Dense(32, activation='relu', input_shape=(3,)),
    keras.layers.Dense(64, activation='relu'),
    keras.layers.Dense(32, activation='relu'),
    keras.layers.Dense(1, activation='linear')
])

# Compilation et entraînement
model.compile(optimizer='adam', loss='mse')
model.fit(historique_norm, resultats_norm, epochs=10, batch_size=512, verbose=0)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    try:
        num1, num2, num3 = int(data['num1']), int(data['num2']), int(data['num3'])
        dernier_tirage = np.array([[num1, num2, num3]])
        dernier_tirage_norm = scaler.transform(dernier_tirage)
        prediction_norm = model.predict(dernier_tirage_norm)
        prediction = scaler.inverse_transform(prediction_norm.reshape(-1, 1))
        return jsonify({'prediction': int(prediction[0][0])})
    except:
        return jsonify({'error': 'Données invalides'}), 400

if __name__ == '__main__':
    app.run(debug=True)
