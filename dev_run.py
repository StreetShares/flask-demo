#!/usr/bin/env python3

"""Hacky way to start all servers at once."""

import os
import subprocess


dirpath = os.path.dirname(os.path.realpath(__file__))

SERVICE_NAME = 'flask_demo'

SERVERS = [
    'private/server.py',
    'public/server.py',
]

processes = []

for server in SERVERS:
    server_path = os.path.join(dirpath, SERVICE_NAME, server)
    processes.append(subprocess.Popen(['python', server_path]))

try:
    processes[0].wait()
except KeyboardInterrupt:
    for proc in processes:
        try:
            proc.terminate()
        except OSError:
            pass
    print('All servers have been murdered.')
