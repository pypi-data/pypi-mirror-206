import pyodbc
pyodbc.pooling = False
import sqlalchemy
import pandas as pd
import urllib
import json
from typing import Tuple

stx = sqlalchemy.text

defaultFile = "dblogs.json"
defaultName = "reader"

def createDummyFile(path : str = defaultFile):
    f = open(path, "w")
    f.write('[{\n')
    f.write('    "name": "an identifier incase you save multiple connections in one file",\n')
    f.write('    "server": "tcp:somefunnyurl.windows.net",\n')
    f.write('    "username": "johndoofus",\n')
    f.write('    "database": "veryprivatedata",\n')
    f.write('    "password": "dontsharethisplz"\n')
    f.write('}]\n')
    f.close()

def loadFile(path) -> Tuple[list, str]:
    msg = None
    data = None
    try:
        with open(path) as file:
            data = json.load(file)
    except json.decoder.JSONDecodeError as e:
        msg = "=> Invalid JSON in provided file"
    except FileNotFoundError as e:
        msg = "=> File was not found"

    if not isinstance(data, list):
        data = [data]

    if msg != None:
        return None, msg
    else:
        return data, None

def isDummyFile(path : str = defaultFile) -> bool   :
    data, msg = loadFile(path)

    isIt = False
    if data[0]['server'] == "tcp:somefunnyurl.windows.net":
        print("You didn't change the server address in the dummy file...")
        isIt = True
    if data[0]['database'] == "veryprivatedata":
        print("You didn't change the database name in the dummy file...")
        isIt = True
    if data[0]['username'] == "johndoofus":
        print("You didn't change the username in the dummy file...")
        isIt = True
    if data[0]['password'] == "dontsharethisplz":
        print("You didn't change the password in the dummy file...")
        isIt = True

    return isIt

def mostProbableDriver() -> str:
    ds = pyodbc.drivers()

    if len(ds) == 0:
        raise Exception("No PYODBC drivers avaliable")
    take = ds[0]
    bigTake = None

    for k in ds:
        entry = k.lower()
        if 'sql server' in entry:
            take = k
            if 'odbc' in entry:
                bigTake = k

    return bigTake if bigTake is None else take

class connect:
    def __init__(self, fileName : str = defaultFile, conn: str = defaultName):
        self.selectedConnIdx = 0

        self.data, msg = loadFile(fileName)
        if self.data == None:
            raise Exception(f'Could not load file {fileName} ' + msg)
        self.loadedFile = fileName

        id = self.setConnection(conn)
        if id == -1:
            print(f'Connection [{conn}] not found in loaded file [{self.loadedFile}]')

        self.verbose = False

        self.driver = mostProbableDriver()

        self.tempConn = None

    def setVerbose(self, givenBool: bool):
        self.verbose = givenBool

    def setDriver(self, givenDriver: str):
        self.driver = givenDriver

    def setConnection(self, name : str) -> int:
        id = self.__getIdx__(name)
        self.selectedConnIdx = id

        return id
    
    def getEngine(self, name : str = None) -> sqlalchemy.Engine:
        if name:
            id = self.__getIdx__(name)
        else:
            id = self.selectedConnIdx

        return self.__buildEngine__(self.data[id])

    def __getIdx__(self, connName : str) -> int:
        i = 0
        for k in self.data:
            if k['name'] == connName:
                return i
            i += 1
        return -1

    def __selectConnection__(self, name : str = defaultName) -> list:
        id = self.__getIdx__(name)
        if id < 0:
            return None
        return self.data[id]
    
    def __buildEngine__(self, conn : list) -> sqlalchemy.Engine:
        n = conn['name']
        if conn['server'] is None:
            raise Exception(f'Missing server URL in Connection [{n}]')
        if conn['database'] is None:
            raise Exception(f'Missing database in Connection [{n}]')
        if conn['username'] is None:
            raise Exception(f'Missing username in Connection [{n}]')
        if conn['password'] is None:
            raise Exception(f'Missing password in Connection [{n}]')

        if self.verbose:
            print(f"Connecting using [{self.driver}] driver")

        params = urllib.parse.quote_plus(f"Driver={self.driver};Server={conn['server']};DATABASE={conn['database']};UID={conn['username']};PWD={conn['password']};")
        engine = sqlalchemy.create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)

        return engine
    
    def query(self, qstr : str) -> pd.DataFrame:
        eg = self.getEngine()

        df = None
        with eg.begin() as conn:
            df = pd.read_sql(sqlalchemy.text(qstr), conn)
        return df
