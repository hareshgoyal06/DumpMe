
from sklearn.ensemble import IsolationForest
import pandas as pd

def detect_anomalies(prices):
    df = pd.DataFrame(prices, columns=["Price"])
    model = IsolationForest(contamination=0.01, random_state=42)
    model.fit(df)
    df["Anomaly"] = model.predict(df)
    return df
