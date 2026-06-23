import os
import requests
import pandas as pd

schemes = {
    "119551": "SBI_Bluechip",
    "120503": "ICICI_Bluechip",
    "118632": "Nippon_Large_Cap",
    "119092": "Axis_Bluechip",
    "120841": "Kotak_Bluechip"
}

output_folder = "data/raw"
os.makedirs(output_folder, exist_ok=True)

for scheme_code, scheme_name in schemes.items():

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    print("=" * 60)
    print(f"Fetching {scheme_name}")
    print("=" * 60)

    try:
        response = requests.get(url)

        if response.status_code == 200:

            data = response.json()

            print("API Scheme :", data["meta"]["scheme_name"])

            df = pd.DataFrame(data["data"])

            filename = os.path.join(output_folder, f"{scheme_name}.csv")

            df.to_csv(filename, index=False)

            print(f"Saved -> {filename}")

        else:
            print("Failed:", response.status_code)

    except Exception as e:
        print(e)

print("\nAll files downloaded successfully.")