from modules.api_functions import *
import pandas as pd
from datetime import datetime

def create_top_100_coin_df():
    
    data = get_top_100_coins()

    df = pd.DataFrame(data)

    return df