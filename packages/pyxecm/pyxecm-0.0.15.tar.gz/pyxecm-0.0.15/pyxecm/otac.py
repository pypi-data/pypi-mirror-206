"""
OTAC Module to implement functions to apply Archive Center settings

Class: OTAC
Methods:

__init__ : class initializer
config : returns config data set
execCommand: exec a command on Archive Center

"""

__author__ = "Dr. Marc Diefenbruch"
__copyright__ = "Copyright 2023, OpenText"
__credits__ = ["Kai-Philip Gatzweiler"]
__maintainer__ = "Dr. Marc Diefenbruch"
__email__ = "mdiefenb@opentext.com"

import requests
import os
import logging

from suds.client import Client

logger = logging.getLogger(os.path.basename(__file__))

requestHeaders = {"Content-Type": "application/x-www-form-urlencoded"}


class OTAC:
    """Used to automate stettings in OpenText Archive Center."""

    _config = None
    _soap_token: str = ""

    def __init__(
        self,
        protocol: str,
        hostname: str,
        port: int,
        ds_username: str,
        ds_password: str,
        admin_username: str,
        admin_password: str,
    ):
        """Initialize the OTAC object

        Args:
            protocol (string): Either http or https.
            hostname (string): The hostname of the Archive Center  to communicate with.
            port (integer): The port number used to talk to the Archive Center .
            username (string): The admin user name of Archive Center (dsadmin).
            password (string): The admin password of Archive Center (dsadmin).
            admin_username (string): The admin user name of Archive Center (otadmin@otds.admin).
            admin_password (string): The admin password of Archive Center (otadmin@otds.admin).
        """

        otacConfig = {}

        if hostname:
            otacConfig["hostname"] = hostname
        else:
            otacConfig["hostname"] = ""

        if protocol:
            otacConfig["protocol"] = protocol
        else:
            otacConfig["protocol"] = "http"

        if port:
            otacConfig["port"] = port
        else:
            otacConfig["port"] = 80

        if ds_username:
            otacConfig["ds_username"] = ds_username
        else:
            otacConfig["ds_username"] = "dsadmin"

        if ds_password:
            otacConfig["ds_password"] = ds_password
        else:
            otacConfig["ds_password"] = ""

        if admin_username:
            otacConfig["admin_username"] = admin_username
        else:
            otacConfig["admin_username"] = "admin"

        if admin_password:
            otacConfig["admin_password"] = admin_password
        else:
            otacConfig["admin_password"] = ""

        otacBaseUrl = protocol + "://" + otacConfig["hostname"]
        if str(port) not in ["80", "443"]:
            otacBaseUrl += ":{}".format(port)
        otacExecUrl = otacBaseUrl + "/archive/admin/exec"
        otacConfig["execUrl"] = otacExecUrl
        otacConfig["baseUrl"] = otacBaseUrl

        self._config = otacConfig

    def config(self):
        return self._config

    def hostname(self):
        return self.config()["hostname"]

    def setHostname(self, hostname: str):
        self.config()["hostname"] = hostname

    def setCredentials(
        self,
        ds_username: str = "",
        ds_password: str = "",
        admin_username: str = "",
        admin_password: str = "",
    ):
        if ds_username:
            self.config()["ds_username"] = ds_username
        else:
            self.config()["ds_username"] = "dsadmin"

        if ds_password:
            self.config()["ds_password"] = ds_password
        else:
            self.config()["ds_password"] = ""

        if admin_username:
            self.config()["admin_username"] = admin_username
        else:
            self.config()["admin_username"] = "admin"

        if admin_password:
            self.config()["admin_password"] = admin_password
        else:
            self.config()["admin_password"] = ""

    def baseUrl(self):
        return self.config()["baseUrl"]

    def execUrl(self):
        return self.config()["execUrl"]

    def execCommand(self, command: str):
        payload = {
            "command": command,
            "user": self.config()["ds_username"],
            "passwd": self.config()["ds_password"],
        }

        requestUrl = self.execUrl()
        logger.info(
            "Execute command -> {} on Archive Center (user -> {}); calling -> {}".format(
                command, payload["user"], requestUrl
            )
        )
        execResponse = requests.post(requestUrl, data=payload, headers=requestHeaders)
        if not execResponse.ok:
            logger.error(
                "Failed to execute command -> {}; error -> {}".format(
                    command, execResponse.text.replace("\n", " ")
                )
            )

        return execResponse

    def putCert(
        self,
        authId: str,
        contRep: str,
        certPath: str,
        permissions: str = "rcud",
    ):
        """put Certificate to Archive Center

        Args:
            authId (str): ID of Certification
            contRep (str): ArchiveID
            certPath (str): local path to certificate (base64)
            permissions (str, optional): _description_. Defaults to "rcud".

        Returns:
            _type_: _description_
        """

        with open(certPath, "r") as file:
            data = file.read()

        requestUrl = (
            self.baseUrl()
            + f"/archive?putCert&pVersion=0046&authId={authId}&contRep={contRep}&permissions={permissions}"
        )
        logger.info(f"Execute putCert -> {certPath} on Archive ; calling -> {contRep}")
        execResponse = requests.put(requestUrl, data=data, headers=requestHeaders)

        if not execResponse.ok:
            logger.error(
                "Failed to execute putCert -> {}; error -> {}".format(
                    authId, execResponse.text.replace("\n", " ")
                )
            )

        return execResponse

    def _soapLogin(self):
        """Authenticate via SOAP with admin User

        Returns:
            string: soap_token
        """
        url = self.baseUrl() + "/archive/services/Authentication?wsdl"
        client = Client(url)
        self._soap_token = client.service.Authenticate(
            username=self.config()["admin_username"],
            password=self.config()["admin_password"],
        )
        return self._soap_token

    def enableCert(self, authId: str, contRep: str, enable: bool = True):
        """enable Certitifacate

        Args:
            authId (str): ClientID
            contRep (str): ArchiveID
            enable (bool, optional): Enable or Disable certificate. Defaults to True.
        """

        if self._soap_token == "":
            self._soapLogin()

        if enable == True:
            enabled: int = 1
        else:
            enabled: int = 0

        url = self.baseUrl() + "/ot-admin/services/ArchiveAdministration?wsdl"
        client = Client(url)

        token_header = client.factory.create("ns0:OTAuthentication")
        token_header.AuthenticationToken = self._soap_token
        client.set_options(soapheaders=token_header)

        response = client.service.invokeCommand(
            command="SetCertificateFlags",
            parameters=[
                {"key": "CERT_TYPE", "data": f"@{contRep}"},
                {"key": "CERT_NAME", "data": authId},
                {"key": "CERT_FLAGS", "data": enabled},
            ],
        )

        return response


# end method definition
