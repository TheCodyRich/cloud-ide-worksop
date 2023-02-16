temp_cool_side = fetch_data['tempCoolSide1C']
temp_warm_side = fetch_data['tempWarmSide1C']
delta = abs(temp_cool_side - temp_warm_side)

return pd.DataFrame([{
    "datetime": str(datetime.now()),
    "temp_cool_side": temp_cool_side,
    "temp_warm_side": temp_warm_side,
    "delta": delta,
}])