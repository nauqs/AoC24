def get_input(day:int=1, splitlines=True): 

    try:
      with open(f"input{str(day).zfill(2)}.txt") as fin:
        data = fin.read()
        if splitlines:
          data = data.strip().splitlines()
        return data 

    except:
        print(f"Failed to load input{day}.txt from disk")


def get_file(name, splitlines=True):

    try:
      with open(name) as fin:
          data = fin.read().strip()
          if splitlines: data = data.splitlines()
          return data 

    except:
        print(f"Failed to load {name} from disk")