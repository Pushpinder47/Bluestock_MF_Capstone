import requests
import pandas as pd

scheme_codes = {
    "sbi_bluechip": 119551,
    "icici_bluechip": 120503,
    "nippon_large_cap": 118632,
    "axis_bluechip": 119092,
    "kotak_bluechip": 120841
}

for scheme_name in scheme_codes:

    code = scheme_codes[scheme_name]

    url = "https://api.mfapi.in/mf/" + str(code)

    response = requests.get(url)

    data = response.json()

    nav_data = pd.DataFrame(data["data"])

    nav_data.to_csv("data/raw/" + scheme_name + ".csv", index=False)

    print(scheme_name, "file saved")
    print("\n----- Simple Fund Recommender -----")

try:
    metrics = pd.read_csv("../data/processed/var_cvar_report.csv")

    # Temporary risk categories
    risk_levels = ["Low", "Moderate", "High"]
    metrics["risk_grade"] = [risk_levels[i % 3] for i in range(len(metrics))]

    risk = input("Enter Risk Appetite (Low/Moderate/High): ")

    result = metrics[metrics["risk_grade"].str.lower() == risk.lower()]

    print("\nTop 3 Recommended Funds")
    print(result.head(3))

except Exception as e:
    print("Error:", e)