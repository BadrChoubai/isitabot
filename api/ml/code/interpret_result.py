import numpy as np
def mod_sigmoid(x: float) -> float:
    return(2/(1+np.exp(-0.29*x)))-1

def weight(token: list) -> int:
    return np.power(np.floor(np.log10(token[0])), 2)

def estimate_model(model: list) -> float:
    return np.mean([mod_sigmoid(weight(token)) for token in model])

def estimate_sample(sample: list) -> float:
    base = np.mean([estimate_model(model) for model in sample])
    if base < 0.5:
        base = np.power(base, 2)
    else:
        base = np.sqrt(base)
    return base

def interpret_result(prob: float) -> str:
    if prob < 0.5:
        return(f"I am {round((100*(1-prob)), 2)}% sure that this text was written by a bot.")
    else:
        return(f"I am {round((100*prob), 2)}% sure that this text was written by a human.")
