#!/usr/bin/env python3

"""Hacky way to start/stop all servers at once."""

import os
import subprocess


def kill_processes(processes):
    """Kill all process in a list of processes."""
    if not processes:
        return
    killed = []
    for proc in processes:
        try:
            print('Killing {}'.format(proc.pid))
            proc.terminate()
            killed.append(proc)
        except OSError as err:
            print(err)
            pass
    for killed_proc in killed:
        processes.remove(killed_proc)
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
    processes[0].wait()
except KeyboardInterrupt:
    kill_processes(processes)

# In case we get down here but didn't kill everything.
kill_processes(processes)
