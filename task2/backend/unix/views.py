import subprocess

from django.shortcuts import render


COMMANDS = ['ls', 'ps', 'whoami', 'id']


def index(request):
    cmd_outputs = []

    for command in COMMANDS:
        res = subprocess.run([command], check=True, capture_output=True, text=True).stdout
        cmd_outputs.append({'name': command, 'output': res})

    return render(request, "unix.html", {'commands': cmd_outputs})
