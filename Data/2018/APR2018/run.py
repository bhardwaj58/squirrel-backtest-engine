import os
import glob
import datetime
import pandas as pd
pop_colums = ["E","F","G","H"]
month_map = {
    "jan": "01",
    "feb": "02",
    "mar": "03",
    "apr": "04",
    "may": "05",
    "jun": "06",
    "jul": "07",
    "aug": "08",
    "sep": "09",
    "oct": "10",
    "nov": "11",
    "dec": "12"
}
#/Users/premagrawal/Desktop/PYTHON/Amit/JAN2020/run.py
def add_column_names(src, headers = ["name","date","time","D","E","F","G","H"]):
    df = pd.read_csv(src)
    if "date" in df.columns:
        # Columns exist. Do not add again
        return

    data = open(src,'r').read()
    # command = "cp -p {} {}".format(src, src.replace(".","-backup."))
    #os.system(command)
    with open(src, "w") as fp:
        fp.write(",".join(headers))
        fp.write("\n")
        fp.write(data)

def cleanup(path, add_headers = False):
    path = str(os.getcwd()) + "/" + path
    month = ""
    month_key = ""
    print(path)
    for key in month_map.keys():
        if key in path.lower():
            month = month_map[key];
            month_key = key.lower()
            # Found Month
            break

    assert (len(month) > 0), ("Invalid Month")

    # It's a good practise to convert everything to specific case when working with strings
    year = path.lower().split(month_key)[-1].split("/")[0]
    assert (int(year) > 1000), (f"Invalid year found {year}")
    start = f"{year}/{month}/01"

    if add_headers:
        add_column_names(path)
    df = pd.read_csv(path)
    df = df[df['date'] >= start]
    # Remove all columns
    for column in pop_colums:
        if column in df.columns:
            df.pop(column)
#Bhai ye side ka kaam toh hogaya shyd ab do min rukh me isko FEB2020 me bhi chalake dekhta hun
#Thik

    df.to_csv("{}".format(path), index = False)

if __name__ == "__main__":
    files = glob.glob("*.csv")
    for f in files:
        cleanup(f, add_headers=True)
