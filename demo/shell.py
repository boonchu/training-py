import sh
import logging

logging.basicConfig(level=logging.INFO)
sh.ls('-la')
ls_cmd = sh.Command('ls')

logging.getLogger('sh').setLevel(logging.DEBUG)
ls_cmd('-la')

try:
    sh.cat('/etc/hosts')
except sh.ErrorReturnCode as e:
    print(f'Command {e.full_cmd} exited with {e.exit_code}')

curl = sh.curl(
    'https://google.com',
    _bg=True
)
try:
    curl.wait(timeout=3)
except sh.TimeoutException:
    print('Command time out..')
    curl.kill()