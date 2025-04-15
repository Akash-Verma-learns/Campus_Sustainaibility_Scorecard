def calculate_score(data):
    # Each metric is scored out of 25
    electricity_score = max(0, 25 - (data['electricity'] / 1000))  # scale
    water_score = max(0, 25 - (data['water'] / 500))
    transport_score = 25 if data['green_transport_ratio'] >= 0.5 else data['green_transport_ratio'] * 50
    waste_score = 25 - min(data['waste'], 25)

    total = electricity_score + water_score + transport_score + waste_score
    return round(total, 2)

def get_grade(score):
    if score >= 85:
        return "A (Excellent)"
    elif score >= 70:
        return "B (Good)"
    elif score >= 55:
        return "C (Moderate)"
    elif score >= 40:
        return "D (Poor)"
    else:
        return "F (Critical)"