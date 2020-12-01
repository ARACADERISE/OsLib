# file helper for the os module
from src.path_finder import RelPath

paths = RelPath()
paths_ = paths.rel_paths('s')
files = paths.rel_file('p','src')

try:
  paths.move('srcbruhfff','src')
except Exception or FileExistsError as err:
  pass

print(paths.move_to_rel('src/srcbruh',[1,5]))
print(paths_,files)