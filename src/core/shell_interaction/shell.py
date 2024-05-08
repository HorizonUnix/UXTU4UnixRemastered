import subprocess

from subprocess import PIPE


class Shell:
    def __init__(self, password: str) -> None:
        self.password = password.encode()

        with subprocess.Popen("sudo -S echo", shell=True, stdin=PIPE) as process:
            process.communicate(input=self.password)

            if process.returncode == 1:
                raise Exception("Incorrect Password")

    def run(self, command: str) -> str:
        with subprocess.Popen(f"sudo -S {command}", shell=True, stdin=PIPE, stdout=PIPE) as process:
            return process.communicate(input=self.password)[0].decode()
