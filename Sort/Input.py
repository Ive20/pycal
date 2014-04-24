'''
Created on 2014.4.24

@author: maxwell
'''
class Input:
    @staticmethod
    def input():
        inputarr=[];
        file_object = open('input.txt');
        try:
            for line in file_object:
                line=line.strip('\n');
                inputarr.extend(line.split(' '));
        finally:
            file_object.close()  ;       
            return inputarr;
    