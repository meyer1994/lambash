import json
import shlex
import subprocess
from subprocess import PIPE

import boto3


def handler(event, context):
    cmd = event.get('cmd', 'echo')
    args = shlex.split(cmd)
    run = subprocess.run(args, stdout=PIPE, stderr=PIPE)
    return {'stdout': run.stdout, 'stderr': run.stderr}


if __name__ == '__main__':
    name = 'lambash-dev-function'
    client = boto3.client('lambda')

    while True:
        cmd = input('$ ')
        cmd = cmd.strip()

        payload = {'cmd': cmd}
        payload = json.dumps(payload)

        try:
            response = client.invoke(FunctionName=name, Payload=payload)
        except Exception as e:
            print(e)
            continue

        data = response['Payload']
        data = data.read()
        data = json.loads(data)

        stdout = data.get('stdout', '')
        stderr = data.get('stderr', '')

        print(stdout, end='')
        print(stderr, end='')
