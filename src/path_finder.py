"""
  path_finder will find all paths relative to what you give.

  rel_paths(key) -> returns all paths relative to key
  rel_file(key,dir) -> return all relative files inside the directory(dir) if it exists
  move(filename, to_dir) -> moves the file(filename), if it exists, into a directory(to_dir), if it exists
    - move will assert an Exception or a FileExistsError if either the directory was not found or the file was not found
"""
import os

class RelPath:

  def __init__(self):

    self.all_paths = os.listdir()
  
  def rel_paths(self,key) -> list:

    paths = []
    for i in self.all_paths:
      if key in i: paths.append(os.path.abspath(i))
    return paths
  
  def rel_file(self, key, dir) -> list: # find relative filenames depending on a directory

    files = []
    for i in self.all_paths:

      if i == dir:
        for (_,_,filenames) in os.walk(i):
          for x in filenames:
            if key in x: files.append(x)
      
    return files
  
  def move(self, filename, to_dir) -> bool: # this will move filename into to_dir if the directory exists

    for i in self.all_paths:

      if to_dir == i:
        assert os.path.isfile(filename), FileExistsError("ERROR")

        os.replace(os.path.abspath(filename), os.path.abspath(i)+'/'+filename)

      assert not i == self.all_paths[len(self.all_paths)-1], Exception('Error moving file\n')
    
    return True