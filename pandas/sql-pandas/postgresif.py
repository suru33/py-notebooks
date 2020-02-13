#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 07:48:23 2020

@author: surendra
"""

import json

import pandas as pd
import sqlalchemy


class PostgresIF:
    def __init__(self, config_file=None, user=None, pwd=None, host=None, db=None):
        if config_file:
            with open(config_file) as f:
                creds = json.load(f)
                user = creds['user']
                pwd = creds['pwd']
                host = creds['host']
                db = creds['db']

        assert user and pwd and host and db

        sql_alchemy_conn = f'postgresql+psycopg2://{user}:{pwd}@{host}/{db}'
        self.engine = sqlalchemy.create_engine(sql_alchemy_conn)

    def get_sql_df(self, sql):
        assert sql
        sql = sqlalchemy.text(sql)
        df = pd.read_sql(sql, self.engine)
        return df

    def run_sql(self, sql, as_dict=False):
        assert sql
        sql = sqlalchemy.text(sql)
        with self.engine.connect() as conn:
            rs = conn.execute(sql)
            data = rs.fetchall()
            if as_dict:
                keys = rs.keys()
                rv = []
                for row in data:
                    d = {}
                    for i, rd in enumerate(row):
                        d[keys[i]] = rd
                    rv.append(d)
                return rv
            return data
