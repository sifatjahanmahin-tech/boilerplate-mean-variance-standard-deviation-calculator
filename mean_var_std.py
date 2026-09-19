import numpy as np

def calculate(list):
    if len(list) !=9:
        raise ValueError("List must contain nine numbers.")
    arr = np.array(list).reshape(3,3)

    def statistics(func):   
       return[
        func(arr,axis=0).tolist(),
        func(arr,axis=1).tolist(),
        func(arr).item(),
       ]


    return {
        'mean': statistics(np.mean),
        'variance': statistics(np.var),
        'standard deviation': statistics(np.std),
        'max': statistics(np.max),
        'min': statistics(np.min),
        'sum': statistics(np.sum),
    }