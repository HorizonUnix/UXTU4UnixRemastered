import subprocess

from subprocess import PIPE


class Shell:
    def __init__(self, password: str) -> None:
        self.password = password.encode()

        if not self.password_is_correct():
            raise Exception("Incorrect Password")

    def run(self, command: str) -> str:
        with subprocess.Popen(f"sudo -S {command}", shell=True, stdin=PIPE, stdout=PIPE) as process:
            output, _ = process.communicate(input=self.password)
            return output.decode()

    def password_is_correct(self) -> bool:
        with subprocess.Popen("sudo -S echo", shell=True, stdin=PIPE) as process:
            process.communicate(input=self.password)

            return not process.returncode
