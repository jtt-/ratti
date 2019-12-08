# NOUSUTIETOIHIN LIITTYVÄ LASKENTA JA DATAN KÄSITTELY

from app import db_mongo
from datetime import datetime
import pandas as pd

collection = db_mongo["aikaleimatesti"]

# HAKEE TUOTEKOHTAISET TAPAHTUMAT LINJOITTAIN HALUTULTA LINJALTA HALUTULLA AIKAVÄLILLÄ

#Haluttu aikaväli. Muodossa 'yyyy-mm-ddThh-mm'
def get_events_by_line(line, startdate, enddate):
    query = {'Tapahtumahetki':{ '$gte': datetime.strptime(str(startdate) + "T00:00", "%Y-%m-%dT%H:%M"), '$lte': datetime.strptime(str(enddate) + "T00:00", "%Y-%m-%dT%H:%M") }, 'Linja':line}
    #query = {'Tapahtumahetki':{ '$gt': startdate, '$lt' : enddate}, 'Linja':line}
    df = pd.DataFrame(list(collection.find(query)))
    return df.groupby("Tuote").size().to_frame("Total").reset_index()

# TEKEE PAREISTA KOOSTUVAN LISTAN LOMAKKEEN SELECTFIELDIÄ VARTEN

def get_lines_tuple():
    lines = collection.distinct("Linja")
    lines_tuple = []
    for line in list(lines):
        lines_tuple.append((line, line))

    return list(lines_tuple)

# HAKEE TAPAHTUMIEN MÄÄRÄN LINJALLA

def get_events(line):

    query = {'Linja':line}
    deps = collection.find(query)

    df_raw = pd.DataFrame(list(deps))


    return len(df_raw)
