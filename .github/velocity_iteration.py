#!/usr/bin/env python
from datetime import datetime
from datetime import date
from collections import defaultdict
import csv
from datetime import date
import pandas as pd
import json


def aggregate_velocity():
    df = pd.read_csv('data/issues.csv')
    df['closed'] = [pd.to_datetime(x.split('T')[0]) if not pd.isna(x) else None for x in df['closed']]

    df_closed = df[~pd.isna(df['closed'])]
    mentions_design = df_closed['labels'].apply(lambda x: ('design' in x.split(';')) if not pd.isna(x) else False)
    df_design = df_closed[mentions_design]
    df_dev = df_closed[~mentions_design]

    with open('data/iterations.json') as f:
        iterations_json = json.load(f)

    # Build and save the summary CSV 
    output_l = []
    for iteration_d in iterations_json:
        row = {}
        
        start_date = datetime.fromisoformat(iteration_d['from'])
        end_date = datetime.fromisoformat(iteration_d['to'])
        row['from'] = iteration_d['from']
        row['to'] = iteration_d['to']

        df_it = df_dev[(start_date <= df_dev['closed']) & (df_dev['closed'] <= end_date)]
        row['dev'] = {
            'story_points': float(df_it['estimate'].sum()),
            'issues_closed': float(df_it['closed'].count())
        }
        
        df_it = df_design[(start_date <= df_design['closed']) & (df_design['closed'] <= end_date)]
        row['design'] = {
            'story_points': float(df_it['estimate'].sum()),
            'issues_closed': float(df_it['closed'].count())
        }

        output_l.append(row)

    with open('data/iteration-summary.json', 'w') as f:
        json.dump(output_l, f, indent=4)

if __name__ == '__main__':
    aggregate_velocity()
