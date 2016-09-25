import os
from string import ascii_uppercase;
import threading;
from queue import Queue;
import glob;



class TfileFinder(object):
    def __init__(self,fileType):
        if "." not in fileType:
            fileType="."+fileType;
        self.fileType=fileType;
        self.allFiles=[];
        self.allDrive=self.getAllDrive();
        self.Que=Queue();
        self.Lock=threading.Lock();

    def getAllDrive(self):
        result=[];
        for d in ascii_uppercase:
            if os.path.exists(d+":\\") and (d!="C"):
                result.append(d+":\\");
        return result;

    def getAllFiles(self):
        for d in self.allDrive:
            t=threading.Thread(target=self.threadWorker,args=());
            t.daemon=True;
            t.start();

        for d in self.allDrive:
            #print("start work on ",d);
            self.Que.put(d);

        self.Que.join();

    def threadWorker(self):
        while True:
            d=self.Que.get();
            self.getAllFilesInDrive(d);
            with self.Lock:
                #print("drive ",d," is done ")
                self.Que.task_done();

    def getAllFilesInDrive(self,drive):
        for root, dirs, files in os.walk(drive):
                 for file in files:
                    if str(file).endswith(self.fileType):
                         with self.Lock:
                             if os.path.exists(root+"\\"+file):
                                self.allFiles.append(root+"\\"+file);

def main():
    ''''
    for root,dirs,files in os.walk('D:\\test'):
            for file in files:
                print(root+"\\"+file);'''
    test = TfileFinder(".jpg");
    test.getAllFiles()

    for f in test.allFiles:
         print(f);


if (__name__)==("__main__"):
    main();

