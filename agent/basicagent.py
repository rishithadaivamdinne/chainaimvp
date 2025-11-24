import pandas as pd
from pathlib import Path

print("Script is running...")  # diagnostic print


def load_sales_data(csv_path: str) -> pd.DataFrame:
    """Load sales data from a CSV file."""
    path = Path(csv_path)
    if not path.exists():
        raise FileNotFoundError(f"CSV file not found at: {csv_path}")
    df = pd.read_csv(path)
    # Expect columns: date, quantity
    if "quantity" not in df.columns:
        raise ValueError("CSV must contain a 'quantity' column.")
    return df

def moving_average_forecast(df: pd.DataFrame, window: int = 4) -> float:
    """Compute simple moving average forecast of the last `window` periods."""
    if len(df) < window:
        window = len(df)
    return df["quantity"].tail(window).mean()

def recommend_order(forecast: float, safety_factor: float = 1.1) -> int:
    """Return a rounded recommended order quantity."""
    recommended = forecast * safety_factor
    return int(round(recommended))

def run_agent(csv_path: str):
    df = load_sales_data(csv_path)
    forecast = moving_average_forecast(df, window=4)
    recommendation = recommend_order(forecast, safety_factor=1.1)

    print("=== Supply Chain Agent Recommendation ===")
    print(f"Last {len(df)} periods average (last 4 used if available).")
    print(f"Forecast for next period: {forecast:.2f} units")
    print(f"Recommended order (with safety factor): {recommendation} units")

if __name__ == "__main__":
    print("Calling run_agent...")  # diagnostic print
    try:
        run_agent("sales.csv")
    except Exception as e:
        print("Error:", e)

