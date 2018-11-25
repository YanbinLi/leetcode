#encoding: utf-8

from multiprocessing import pool
from multiprocessing.dummy import Pool as ThreadPool
import os


class file_content_search:
    '''
    搜索文件内容
    '''
    def __init__(self, parallelism = 4 ):
        self.pool = ThreadPool(parallelism)

    def get_all_files(self, dir, file_type):
        all_files = []
        for (root, dirname, filenames) in os.walk(dir):
            for filename in filenames:
                fullname = os.path.join(root, filename)
                if fullname.endswith(file_type):
                    all_files.append(fullname)
        return all_files
    
    def search_file(self, filename):

        file = open(filename)
        for line in file:
            if self.search_str in line:
                file.close()
                return filename
        file.close()

    def search(self, dir, file_type, search_str):
        self.search_str = search_str
        all_files = self.get_all_files(dir, file_type )
        print("%d files found."%len(all_files))
       
        results = self.pool.map(self.search_file, all_files)
        self.pool.close()
        self.pool.join()
        
        return  [tmp for tmp in results if tmp != None]

if __name__ == "__main__":
    seacher = file_content_search(4)
    results = seacher.search(r"E:\下载\bt宅5.0.4\codecs", ".ini", '[Application]')
    print(results)

"""
JUST FOR REST
"""