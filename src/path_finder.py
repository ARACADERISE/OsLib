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
  
  def move_to_rel(self, filename, accordance:list) -> str: # this will move a file to the most relative path according to the info you give it

    # path_max_length = max amount of directories to find
    # path_min_length = min amount of directories to find

    # if the program finds a directory path in bettween the path_max_length and the path_min_length, it will pick that path and return it as a string.

    path_max_length = -1
    path_min_length = -1 # both negative one for error checking
    if isinstance(accordance,list):
      assert len(accordance) == 2, Exception(f'List length too long. Expected 2 values, got {len(accordance)}')

      assert isinstance(accordance[0],int) and isinstance(accordance[1],int), Exception(f'Expected list of integers, instead got {type(accordance[0])}')

      if accordance[0] > accordance[1]:
        path_max_length = accordance[0]
        path_min_length = accordance[1]
      else:
        path_max_length = accordance[1]
        path_min_length = accordance[0]
      
      all_appended_paths = []
      index = 0

      for i in self.all_paths:

        curr = os.path.abspath(i).split('/')
        all_appended_paths.append(os.path.abspath(i))
        
        if len(curr) > path_max_length:
          del all_appended_paths[len(all_appended_paths)-1]
        if len(curr) <= path_max_length and len(curr) > path_min_length:
          # we will then loop through the paths to find most relative one
          pass
        if not len(curr) <= path_max_length or len(curr) < path_min_length:
          return '' # just return a empty string.