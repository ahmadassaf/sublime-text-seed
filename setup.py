import platform
import sys
import os
import signal
import subprocess

platform = platform.system()
app_path = ''
config_path = ''

def main():
  if platform == 'Darwin':
    print('OSX detected')
    # TODO: test this in OSX
    app_path = '/Applications/Sublime Text.app'
    # TODO: test this in OSX
    config_path = os.path.expanduser('~') + '/Library/Application Support/Sublime Text 3'
    if not is_installed(app_path):
      install_osx()
    config_osx(config_path)
    sys.exit(0)

  if platform == 'Linux':
    print('Linux detected...')
    app_path = 'sublime'
    config_path = os.path.expanduser('~') + '/.config/sublime-text-3'
    if not is_installed(app_path):
      install_linux(app_path)
    config_linux(config_path)
    sys.exit(0)

  if platform == 'Windows':
    print('Windows detected...')
    # TODO: do a windows instal to determine the default install location
    # app_path = ''
    # TODO: do a windows instal to determine the default config location
    # config_path = ''
    if not is_installed(app_path):
      install_windows(app_path)
    config_windows(config_path)
    sys.exit(0)

  else:
    raise Exception('Operating system not supported');
    sys.exit(1)

def is_installed(app_path):
  try:
    p = subprocess.Popen(app_path)
    os.kill(p.pid, signal.SIGTERM)
    print('Sublime is installed...')
    return True

  except OSError as e:
    print('Sublime not installed...')
    return False

def install_osx(app_path):
  # TODO: implement OSX installation
  return

def config_osx(config_path):
  # TODO: implement OSX config
  return

def install_linux(app_path):
  try:
    print('Updating apt-get...')
    subprocess.call(['apt-get', 'update'], stdout=subprocess.PIPE)
    print('Installing Sublime Text...')
    subprocess.call(['apt-get', 'install', 'sublime-text'], stdout=subprocess.PIPE)
    print('Installation complete...')

  except OSError as e:
    print('Install failed:')
    print(e)
    sys.exit(1)

def config_linux(config_path):
  # TODO: implement Linux config
  return

def install_windows(app_path):
  # TODO: implement Windows installation
  return

def config_windows(config_path):
  # TODO: implement Windows config
  return

if __name__ == '__main__':
  main()
