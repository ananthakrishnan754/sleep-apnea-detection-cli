def ahi_proxy(pred_minutes, hours):
    if hours <= 0: return 0.0
    return pred_minutes / hours

def severity(ahi):
    if ahi < 5: return "Healthy"
    if ahi < 15: return "Mild"
    if ahi < 30: return "Moderate"
    return "Severe"
