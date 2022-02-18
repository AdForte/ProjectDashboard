import pandas as pd


def process_missions():
    missions = pd.read_excel("../data/data_gw.xlsx", sheet_name="Missions")
    # donjons = pd.read_excel("../data/data_gw.xlsx", sheet_name="Donjons").to_dict()
    return missions

def process_donjons():
    # missions = pd.read_excel("../data/data_gw.xlsx", sheet_name="Missions").to_dict()
    donjons = pd.read_excel("../data/data_gw.xlsx", sheet_name="Donjons")
    return donjons