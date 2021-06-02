import pandas as pd
import json
import os
import numpy as np
from .folders_tb import read_json_to_dict
from .mysql_driver import MySQL
from sqlalchemy import create_engine

def nflcleantomysql(csvname):
    SEP = os.sep
    dir = os.path.dirname
    csv_fullpath = dir(os.getcwd()) + SEP + "data" + SEP + csvname
    json_fullpath = (os.getcwd()) + SEP + "utils" + SEP + "sql_server_settings.json"
    json_readed = read_json_to_dict(json_fullpath)
    IP_DNS = json_readed["IP_DNS"]
    USER = json_readed["USER"]
    PASSWORD = json_readed["PASSWORD"]
    BD_NAME = json_readed["BD_NAME"]
    PORT = json_readed["PORT"]
    engine = create_engine(f'mysql+pymysql://{USER}:{PASSWORD}@{IP_DNS}:{PORT}/{BD_NAME}')
    NFL = pd.read_csv(csv_fullpath, index_col=None)
    NFL['Date'] = pd.to_datetime(NFL['Date'])
    NFL.to_sql('NFLtest', con = engine, index=False, if_exists='append')
    return f'{csvname} appended to NFLtest table in {BD_NAME}'

def nbacleantomysql(csvname):
    SEP = os.sep
    dir = os.path.dirname
    csv_fullpath = dir(os.getcwd()) + SEP + "data" + SEP + csvname
    json_fullpath = (os.getcwd()) + SEP + "utils" + SEP + "sql_server_settings.json"
    json_readed = read_json_to_dict(json_fullpath)
    IP_DNS = json_readed["IP_DNS"]
    USER = json_readed["USER"]
    PASSWORD = json_readed["PASSWORD"]
    BD_NAME = json_readed["BD_NAME"]
    PORT = json_readed["PORT"]
    engine = create_engine(f'mysql+pymysql://{USER}:{PASSWORD}@{IP_DNS}:{PORT}/{BD_NAME}')
    NBA = pd.read_csv(csv_fullpath, index_col=None)
    NBA['Date'] = pd.to_datetime(NBA['Date'])
    NBA.to_sql('NBAtest', con = engine, index=False, if_exists='append')
    return f'{csvname} appended to NBAtest table in {BD_NAME}'

def footballcleanandsendtomysql(COUNTRY, LEAGUE, SEASON, csvname):
    SEP = os.sep
    dir = os.path.dirname
    csv_fullpath = dir(os.getcwd()) + SEP + "data" + SEP + csvname
    json_fullpath = (os.getcwd()) + SEP + "utils" + SEP + "sql_server_settings.json"
    json_readed = read_json_to_dict(json_fullpath)
    IP_DNS = json_readed["IP_DNS"]
    USER = json_readed["USER"]
    PASSWORD = json_readed["PASSWORD"]
    BD_NAME = json_readed["BD_NAME"]
    PORT = json_readed["PORT"]
    df = pd.read_csv(csv_fullpath, index_col=None)
    df = df[['Date','HomeTeam','FTHG','AwayTeam','FTAG','B365H','B365D','B365A']]
    df['Country'] = COUNTRY
    df['League'] = LEAGUE
    df['Season'] = SEASON
    df['Homeoraway'] = "Home"
    df.rename(columns={'HomeTeam':'Team', 'FTHG':'TeamGoals', 'AwayTeam':'Opponent', 'FTAG':'OpponentGoals', 'B365H':'TeamOdds', 'B365D':'DrawOdds',        'B365A':'OpponentOdds'}, inplace=True)
    awaydf = df.rename(columns={'Team':'Opponentt', 'TeamGoals':'OpponentGoalst', 'Opponent':'Teamt', 'OpponentGoals':'TeamGoalst', 'TeamOdds':'OpponentOddst', 'OpponentOdds':'TeamOddst'})
    awayt = awaydf.rename(columns={'Opponentt':'Opponent', 'OpponentGoalst':'OpponentGoals', 'Teamt':'Team', 'TeamGoalst':'TeamGoals', 'OpponentOddst':'OpponentOdds', 'TeamOddst':'TeamOdds'})
    awayt["Homeoraway"].replace({"Home": "Away"}, inplace=True)
    awayt = awayt[["Date", "Team", "TeamGoals", "Opponent", "OpponentGoals", "TeamOdds", "DrawOdds", "OpponentOdds", "Country", "League", "Season", "Homeoraway"]]
    df = df.append(awayt)
    conditions = [(df['TeamGoals'] > df['OpponentGoals']), 
    (df['TeamGoals'] == df['OpponentGoals']),
    (df['TeamGoals'] < df['OpponentGoals'])]
    values = ['Win', 'Draw', 'Lose']
    df['Result'] = np.select(conditions, values)
    conditions = [(df['Result'] == "Win"),
    (df['Result'] != "Win")]
    values = [(df['TeamOdds']-1), -1]
    df['ResultBetWin'] = np.select(conditions, values)
    conditions = [(df['Result'] == "Draw"),
    (df['Result'] != "Draw")]
    values = [(df['DrawOdds']-1), -1]
    df['ResultBetDraw'] = np.select(conditions, values)
    conditions = [(df['Result'] == "Lose"),
    (df['Result'] != "Lose")]
    values = [(df['OpponentOdds']-1), -1]
    df['ResultBetLose'] = np.select(conditions, values)
    conditions = [(df['TeamOdds'] <= df['OpponentOdds']),
    (df['TeamOdds'] > df['OpponentOdds'])]
    values = ["Favourite", "NotFavourite"]
    df['Favourite'] = np.select(conditions, values)
    df['TotalGoals'] = df['TeamGoals'] + df['OpponentGoals']
    df = df[["Country", "League", "Season", "Date", "Homeoraway", "Team", "TeamGoals", "Opponent", "OpponentGoals", "Favourite", "Result", "TotalGoals", "TeamOdds", "DrawOdds", "OpponentOdds", "ResultBetWin", "ResultBetDraw", "ResultBetLose"]]
    df['Date'] = pd.to_datetime(df['Date'])
    engine = create_engine(f'mysql+pymysql://{USER}:{PASSWORD}@{IP_DNS}:{PORT}/{BD_NAME}')
    df.to_sql('Futboltest', con = engine, index=False, if_exists='append')
    print(csvname, "Cleaned and uploaded to mysql")
    return df