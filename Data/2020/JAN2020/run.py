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

base_path = "./Data/"
extentions = [".txt",".csv"]

## Please Structure your folder this way
"""
    Project/
        run.py
        Data/
            2018/
                JAN2018/
                FEB2018/
            2019/
                JAN2019
                FEB2019
            2020/
                JAN2020
                .
                .
"""
#ok
# Haan. Woh change kar leta hu. 2 mins
#problem ye hai ki 2018 ki month ki koi koi files ka format csv hona chaiye par .txt hai aur koi koi files ka format .csv hai toh unke naam wierd hai
#matlab jaise baki files ke the vese nahi hai toh jo nam hai wo bhi change karne hai aur .txt hoga toh .csv karna hai
#wait tuje screenshot share karta hun slack par thik hai
# But ek baat bol. The contents in those txt files are the same only, right? Cool hai fir toh. Haan. mai tab tak code change karta hu for txt files
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
    # path =  "/" + path
    month = ""
    month_key = ""
    print(path)
    for key in month_map.keys():
        if key in path.lower():
            month = month_map[key];
            month_key = key.lower()
            # Found Month
            break
#nai nai. It is independent of other directories. Farak nai padta
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
    df.to_csv("{}".format(path.replace(".txt", "")), index = False)

if __name__ == "__main__":
    for ext in []
    files = glob.glob("Data/*/*.csv")
    files += glob.glob("Data/*/*.txt")
    for f in files:
        cleanup(f, add_headers=True)
