import subprocess
from uuid import uuid4
import platform
import os

class psremoter(subprocess.Popen):
    _script_file: str = None
    output: str = None
    return_code: int = None
    status: bool = None
    linux: bool = False

    def __new__(cls, *args, **kwargs):
        system= str(platform.system()).lower()
        if system != "windows":
            cls.linux= True
        return super(psremoter, cls).__new__(cls)

    def __init__(self, hostname:str, command:str,username=None, password=None, powershell=False, domain=None):
        if domain:
            self.domain = domain + "\\"
        else:
            self.domain = ".\\"

        self.hostname = hostname
        self.username = username
        self.password = password
        self.command = command.strip()
        self.powershell = powershell

    def delete_file(self) -> None:
        os.remove(self._script_file)

    def build_powershell_command(self) -> None:
        if not self.powershell:
            return

        self._script_file= script =  str(uuid4())+ ".ps1"

        with open(script, 'a') as script_file:
            script_file.write("try{" + "\n")
            for line in self.command.splitlines():
                script_file.write(line + "\n")
            script_file.write("}catch{echo $_.exception.message; exit -1}")
            script_file.close()

    def local_execution(self):
        if self.powershell:
            self.build_powershell_command()

            if self.linux:
                self.command = f"pwsh -File {self._script_file}"
            else:
                self.command = f"%SystemRoot%\\System32\\WindowsPowerShell\\v1.0\\powershell.exe -ExecutionPolicy Bypass -File {self._script_file}"

        super().__init__(self.command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

        self.output= self.communicate()[0].decode('utf-8')
        self.return_code = self.returncode

        if self.return_code == 0:
            self.status= True
        else:
            self.status= False

        if self.powershell:
            self.delete_file()
        return self

    def remote_execution(self):
        if not self.powershell:
            raise Exception('remote_execution method working only as PowerShell script...\nPlease change your script to a PowerShell one.')
        elif not self.username:
            raise Exception(
                f'Please add remote host ({self.hostname}) username.')
        elif not self.password:
            raise Exception(
                f'Please add remote host ({self.hostname}) password.')
        self.command= """
            $User = "{}{}"
            $PWord = ConvertTo-SecureString -String "{}" -AsPlainText -Force
            $Credential = New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList $User, $PWord
            Invoke-Command -ComputerName {} -ScriptBlock {} -Credential $Credential -Authentication Negotiate -Verbose -ErrorAction Stop
        """.format(
            self.domain,
            self.username,
            self.password,
            self.hostname,
            "{" + self.command + "}"
        )

        return self.local_execution()

    def __str__(self):
        return f"Result ({self.status}), Return Code ({self.return_code}), Output ({self.output=})"
