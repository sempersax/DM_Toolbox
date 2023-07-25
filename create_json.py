import json
import numpy as np
import os

"""
Way to format data for jsons and create the jsons
"""


def fileMaker(data, file_name, path = os.getcwd()):
    with open(path + f"/{file_name}.json", "w") as f:
        try:
            json.dump(data, f)
        except TypeError:
            if type(data) == np.ndarray:
                json.dump(np.ndarray.tolist(data), f)
                print("Converted numpy array to list")
            else:
                try:
                    json.dump(np.ndarray.tolist(np.asarray(data)), f)
                    print("Converted list to numpy array back to list")
                except:
                    raise

    f.close()
    return


def multiJSON(data, path=os.getcwd()):
    for key in data.keys():
        fileMaker(data[key], key.lower(), path)
    return


if __name__ == '__main__':
    print('yo')