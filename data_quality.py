# -*- coding: utf-8 -*-

import pathlib as pl

lib_dir = pl.Path(__file__).resolve().parent

class DataQuality:
    
    def __init__(self,dataset,year):
        self.dataset= dataset
        self.year = year
        self.fix_specific_issue()
    
    def fix_specific_issue(self):
        if (self.dataset == 'fuel_mix_5m') and (self.year<=2017):
            DataQuality().issue_fuelmix_2017()
        #add other specific issues
    
    @staticmethod
    def fix_all_issues():
        #check which datasets are present and then fix them
        DataQuality().issue_fuelmix_2017()
    
    @staticmethod
    def issue_fuelmix_2017():
        fuel_mix_dir = pl.Path(lib_dir,'raw_datafiles','fuel_mix_5m').glob('*/')
        fuel_mix_dirs = [int(folder.name) for folder in fuel_mix_dir if int(folder.name)<=2017]
        #unfinished
        print(fuel_mix_dirs)
        return
    
if __name__ == '__main__':
    DataQuality().fix_all_issues()