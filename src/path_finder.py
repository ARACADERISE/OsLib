"""
  path_finder will find all paths relative to what you give.

  rel_paths(key) -> returns all paths relative to key
  rel_file(key,dir) -> return all relative files inside the directory(dir) if it exists
  move(filename, to_dir) -> moves the file(filename), if it exists, into a directory(to_dir), if it exists
    - move will assert an Exception or a FileExistsError if either the directory was not found or the file was not found
"""
import os, random

class RelPath:

  def __init__(self):

    self.all_paths = os.listdir()
  
  def rel_paths(self,key) -> list:

    paths = []
    for i in self.all_paths:
      if key in i: paths.append(os.path.abspath(i))
    return paths
  
  def rel_file(self, key, dir, retDirPath = False) -> list: # find relative filenames depending on a directory

    files = []
    for i in self.all_paths:

      if i == dir:
        for (_,_,filenames) in os.walk(i):
          for x in filenames:
            if key in x:
              if retDirPath == False: files.append(x)
              else: files.append(os.path.abspath(x))
      
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
      
      dir_depth_info = {}
      

      for i in self.all_paths:

        curr = os.path.abspath(i).split('/')

        if len(curr) <= path_max_length and len(curr) >= path_min_length:
          full_path = ""
          for i in range(len(curr)):
            if i == len(curr)-1:
              full_path += f"{curr[i]}"
              break
            full_path += f"{curr[i]}/"
          
          dir_depth = 0
          for i in range(len(full_path)):
            if full_path[i] == '/':dir_depth+=1
          
          dir_depth_info.update({full_path:dir_depth})
          #if dir_depth > 0:
           # if dir_depth <= path_max_length and dir_depth >= path_min_length:
           #   return full_path
        if len(curr) > path_max_length or len(curr) < path_min_length:
          return '' # just return a empty string.
      
      most_rel_lengths = []
      index = 0
      for i in dir_depth_info:
        if index != len(dir_depth_info)-1:
          if index == 1:
            if dir_depth_info[i] < most_rel_lengths[index-1]:
              continue
            if dir_depth_info[i] > most_rel_lengths[index-1]:
              del most_rel_lengths[index-1]
              most_rel_lengths.append(dir_depth_info[i])
          else:
            most_rel_lengths.append(dir_depth_info[i])
      
      if len(most_rel_lengths) > 0:
        all_ = []
        for i in dir_depth_info:
          if index != len(dir_depth_info)-1:
            if dir_depth_info[i] == most_rel_lengths[0]:
              all_.append(i)
              if index > 0:
                if len(i) > all_[index-1]:
                  return all_[index-1]
                else:
                  index += 1
                  continue