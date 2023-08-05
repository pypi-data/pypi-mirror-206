from .write import writeJSON2File

def write(filename:str, data, formatted=False) -> None:
    writeJSON2File.writeJSON2File(filename, data, formatted)
