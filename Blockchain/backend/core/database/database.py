import os
import json


class BaseDB:
    def __init__(self):
        self.basepath = 'data'
        self.filepath = '/'.join((self.basepath, self.filename))

    # def read(self):
    #     if not os.path.exists(self.filepath):
    #         print(f"File {self.filepath} not available")
    #         return False
        
    #     with open(self.filepath,'r') as file:
    #         raw = file.readline()

    #     if len(raw) > 0:
    #         data = json.loads(raw)
    #     else:
    #         data = []
    #     return data
    def read(self):
        if not os.path.exists(self.filepath):
            print(f"File {self.filepath} not available")
            return []
        
        with open(self.filepath, 'r') as file:
            raw = file.readline()

        if len(raw) > 0:
            try:
                data = json.loads(raw)
            except json.JSONDecodeError:
                data = []
        else:
            data = []
        return data

    def write(self, item):
        data = self.read()
        if data:
            data = data + item
        else:
            data = item

        with open(self.filepath, "w+") as file:
            file.write(json.dumps(data))

class BlockchainDB(BaseDB):
    def __init__(self):
        self.filename = 'blockchain'
        super().__init__()
        print("Database filepath:", self.filepath)  # Debug statement

    def lastBlock(self):
        data = self.read()

        if data:
            return data[-1]

    