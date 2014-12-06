'''
Created on 2014.4.24

@author: maxwell
'''
import os


class Input:
    @staticmethod
    def getinputarr(filename='input.txt'):
        inputarr=[]
        file_object = open(os.path.dirname(os.path.realpath(__file__))+'/'+filename)
        try:
            for line in file_object:
                line=line.strip('\n')
                inputarr.extend(map(int,line.split(' ')))
        finally:
            file_object.close()
            return inputarr