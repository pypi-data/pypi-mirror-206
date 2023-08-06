import pandas as pd
import requests
import io

def load_nba_box_score_data():
    github_url = "https://raw.githubusercontent.com/MylesThomas/nba-box-score-predictions/main/nba_games_data.csv"
    download = requests.get(github_url).content
    df = pd.read_csv(io.StringIO(download.decode('utf-8')))
    return df