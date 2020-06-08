import json
import os
import fasttext
from collections.abc import Iterable
from typing import List
import itertools

model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'data','model.bin')
lookup_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'data','gender_lookup.json')

model = fasttext.load_model(model_path)
with open(lookup_path) as json_file:
    gender_lookup = json.load(json_file)
    
name_set = set(gender_lookup.keys())

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
    
    # List of names that overlap with existing name dictionary
    intersection_ = list(set(clean_name_iter).intersection(name_set))
    # List of names that are not in existing dictionary. Model will predict gender for these names.
    difference_ = list(set(clean_name_iter).difference(name_set))
    
    ultrasound = {}
    
    # O(1) lookup of name->gender
    if intersection_:
        for name in intersection_:
            ultrasound[name] = gender_lookup[name]['gender']
    
    # Model predicts name->gender
    if difference_:
        predictions = itertools.chain.from_iterable(model.predict(difference_)[0])
        preds = zip(difference_, predictions)
        for k,v in preds:
            ultrasound[k] = v[-1]
    
    
    return ultrasound
