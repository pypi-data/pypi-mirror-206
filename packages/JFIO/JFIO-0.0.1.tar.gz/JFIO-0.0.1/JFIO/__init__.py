from .write import writeJSON2File

def write(filename:str, data:Any, formatted=False) -> None:
    writeJSON2File.write(filename, data, formatted)
