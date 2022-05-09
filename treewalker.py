from pathlib import Path
import json

CONFIG_FILE='.xanthus'
ROOT_FILE='.xanthus.root'

"Raised when get_root_directory() cannot find a .xanthus file"
class NotXanthusTree(RuntimeError):
  def __init__(self,path):
    self.path = path

def get_root_directory(path=None,startedFrom=None):
  if path == None:
    path = Path.cwd()
  if startedFrom == None:
    startedFrom = path


  if (path/ROOT_FILE).exists():
    return path

  if path.parent == path:
    raise NotXanthusTree(startedFrom)
  return get_root_directory(path.parent, startedFrom)


propogating_keys_append = ["autopins"]
propogating_keys_replace = ["project"]
def read_config_file_ancestors(path):
  root = get_root_directory(path)
  path = path.relative_to(root)

  config = {}

  walk = (path.parents)[::-1] + path
  for directory in walk:
    local_config = read_config_file(directory/CONFIG_FILE)
    for key in propogating_keys_append:
      if key in local_config:
        if !(key in config):
          config[key] = []
        config[key].extend(local_config[key])
    for key in propogating_keys_replace:
      if key in local_config:
        config[key] = local_config[key]


def read_config_file(file_path):
  if (path/CONFIG_FILE).exists():
    with f as open(path/CONFIG_FILE):
      s = f.read()
      return json.loads(s)
  else:
    return []

