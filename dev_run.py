#!/usr/bin/env python3

"""Hacky way to start/stop all servers at once."""

import os
import subprocess


def kill_processes(processes):
    """Kill all process in a list of processes."""
    print(processes)
    if not processes:
        return
    for i, proc in enumerate(processes):
        try:
            proc.terminate()
            processes.pop(i)
        except OSError:
            pass
    print('All servers have been murdered.')


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
    # for proc in processes:
    #     try:
    #         proc[0].wait()
    #     except Exception:
    #         pass
    processes[0].wait()
except KeyboardInterrupt:
    kill_processes(processes)

# Incase we get down here but didn't kill everything.
kill_processes(processes)
