import os
from unittest import result
import numpy as np
import pandas as pd
import seaborn as sns
import math
from scipy import stats
from pathlib import Path
from statistics import mean

def main():
    dirPathGen = (Path('..')/'camera_placement_coverage'/'exp12').glob('idF5*')
    savePath = Path('.')/'exp12'
    savePath.mkdir(parents=True,exist_ok=True)
    for dirPath in dirPathGen:
        print(dirPath.name)
        saveDirPath = (savePath/(dirPath.name))
        saveDirPath.mkdir(parents=True,exist_ok=True)
        copyDir = dirPath/'results'
        os.system(f'powershell mv {copyDir} {saveDirPath}')

if __name__ == '__main__':
    main()