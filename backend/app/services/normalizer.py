# Min-max scaling and weighting logic
def normalize(value, min_val, max_val):
    return (value - min_val) / (max_val - min_val) * 100

def composite(data):
    # TODO: apply weights 50/35/15
    pass
