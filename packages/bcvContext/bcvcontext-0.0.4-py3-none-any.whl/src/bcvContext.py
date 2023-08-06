import json

def scriptContext(filename) :
    version = json.load(open(".config.json"))["scriptsVersion"]
    return "../../../data_flow/" + version + "/" + filename

def dayContext(m, filename) :
    day = json.load(open(".config.json"))["day"] + m
    if (day < 0) : raise Exception("No history at J", str(day))
    lastNotarization = json.load(open("../../Day" + str(day) + "/.dayConfig.json"))["lastNotarization"]
    return "../../Day" + str(day) + "/Notarization" + str(lastNotarization) + "/" + filename

def getRawfile():
    return "../rawFile.csv"