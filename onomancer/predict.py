import os
import fasttext
from collections.abc import Iterable
from typing import List
import itertools

model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'data','model.bin')
F_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'data','F.txt')
M_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'data','M.txt')
N_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'data','N.txt')

model = fasttext.load_model(model_path)
F_set = set(open(F_path, "r").read().split("\n"))
M_set = set(open(M_path, "r").read().split("\n"))
N_set = set(open(N_path, "r").read().split("\n"))
full_name_set = F_set.union(M_set).union(N_set)

def predict(name_iter:List[str]):
    
    if isinstance(name_iter, Iterable):    
        # Defend against single string non-iterable 
        if isinstance(name_iter, str):
            clean_name_iter = [name_iter.upper().strip()]
            
        # Defend against tuples of len 1
        elif len(name_iter) == 1:
            clean_name_iter = [name_iter[0].upper().strip()]
        
        else:
            clean_name_iter = list(map(lambda x: x.upper().strip(), name_iter))
    
    else:
        raise ValueError("Invalid iterable passed to name_iter argument of predict function. Please provide a valid iterable of strings.")
    
    # Set of names that overlap with existing name dictionary
    F_intersection_ = set(clean_name_iter).intersection(F_set)
    M_intersection_ = set(clean_name_iter).intersection(M_set)
    N_intersection_ = set(clean_name_iter).intersection(N_set)
    # List of names that are not in existing dictionary. Model will predict gender for these names.
    difference_ = list(set(clean_name_iter).difference(full_name_set))
    
    ultrasound = {}
    # O(1) lookup of name->gender
    if F_intersection_:
        for name in F_intersection_:
            ultrasound[name] = "F"
    if M_intersection_:
        for name in M_intersection_:
            ultrasound[name] = "M"
    if N_intersection_:
        for name in N_intersection_:
            ultrasound[name] = "N"

    # Model predicts name->gender
    if difference_:
        predictions = itertools.chain.from_iterable(model.predict(difference_)[0])
        preds = zip(difference_, predictions)
        for k,v in preds:
            ultrasound[k] = v[-1]
    
    
    return ultrasound
