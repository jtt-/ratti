# AIKATAULUDATAN KÄSITTELY JA LASKENTA

from app import db_mongo
from datetime import datetime
import pandas as pd

collection = db_mongo["stopevents"]

def get_stops_tuple():
    stop_codes = collection.distinct('STOP_NAME')
    stop_menu = []

    for stop_code in stop_codes:
        stop_menu.append((stop_code, stop_code))

    return stop_menu

def get_events_by_stop(stop):

    query = {'STOP_NAME':stop}
    df = pd.DataFrame(list(collection.find(query)))
    return df
