# onomancer
*onomancer* is an open source python package for inferring gender from first names for feature engineering. Name-Gender mappings are based on lookups in the `F.txt, M.txt, N.txt` files located in the `data` folder created from combining data provided from the [Social Security Administration](https://www.ssa.gov/oact/babynames/limits.html) and [World Intellectual Property Organization](https://ideas.repec.org/s/wip/eccode.html). If a Name-Gender mapping does not exist, the gender is predicted from a pre-trained model named `model.bin` also located in the `data` folder. 

## Requirements
onomancer requires:

- python >= 3.6.x.
- fasttext == 0.9.2 (to load pre-trained model)

## Installing
`$ pip install onomancer`

## Usage

```
$ python
>>> import onomancer as ono
>>> ono.predict(['GALADRIEL', 'GanDALF'])
{'GANDALF': 'M', 'GALADRIEL': 'F'}
```
