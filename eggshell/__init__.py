import subprocess
import io

def run(command, cwd=None):
    proc = subprocess.Popen(
        command,
        shell=True,
        universal_newlines=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        close_fds=True,
        cwd=cwd
    )
    stdout, stderr = proc.communicate()
    return (proc.returncode, stdout.strip(' \n'), stderr.strip(' \n'))
