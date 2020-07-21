#!/usr/bin/env python

import json
from datetime import datetime

import pandas as pd


def summarize_iterations():
    """Divide the issues csv by iteration and by whether it contains the `design` label.
    For dev and for design, summarize the story points and issues closed during
    the each iteration. Save the output json to the `data` dir as iteration-summary.json.
    """
    df = pd.read_csv('data/issues.csv')
    df['closed'] = [pd.to_datetime(x.split('T')[0]) if not pd.isna(x) else None for x in df['closed']]

    df_closed = df[~pd.isna(df['closed'])]
    mentions_design = df_closed['labels'].apply(lambda x: ('design' in x.split(';')) if not pd.isna(x) else False)
    df_design = df_closed[mentions_design]
    df_dev = df_closed[~mentions_design]

    with open('data/iterations.json') as f:
        iteration_data = json.load(f)

    # Build and save the summary CSV
    for iteration in iteration_data:
        # don't recalculate values that are already present
        if 'dev' in iteration:
            continue

        start_date = datetime.strptime(iteration['from'], '%Y-%m-%d')
        end_date = datetime.strptime(iteration['to'], '%Y-%m-%d')

        df_it = df_dev[(start_date <= df_dev['closed']) &
                       (df_dev['closed'] <= end_date)]
        iteration['dev'] = {
            'points': int(df_it['estimate'].sum()),
            'issues': int(df_it['closed'].count())
        }

        df_it = df_design[(start_date <= df_design['closed']) &
                          (df_design['closed'] <= end_date)]
        iteration['design'] = {
            'points': int(df_it['estimate'].sum()),
            'issues': int(df_it['closed'].count())
        }

    # calculate velocity
    for i, iteration in enumerate(iteration_data):
        if i < 2:
            continue
        iteration['dev']['velocity'] = '%.2f' % \
            (sum([i['dev']['points'] for i in iteration_data[i - 2:i]]) / 3.0)

        iteration['design']['velocity'] = '%.2f' % \
            (sum([i['design']['points'] for i in iteration_data[i - 2:i]]) / 3.0)

    with open('data/iteration-summary.json', 'w') as f:
        json.dump(iteration_data, f, indent=4)

if __name__ == '__main__':
    summarize_iterations()
