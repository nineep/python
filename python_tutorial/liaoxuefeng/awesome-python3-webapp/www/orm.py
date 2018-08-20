#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio, logging
import aiomysql

def log(sql, args=()):
    logging.info('SQL: %s' % sql)



