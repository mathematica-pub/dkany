from dkany.data_hosts.sftp import SftpClient

def test_akamai_sftp_client():
    akamai_sftp_client = SftpClient(
        host = "cmsstorage.upload.akamai.com",
        username = "sshacs",
        private_key_file = "path/to/file",
        private_key_pass = "pw"
    )

    cwd = akamai_sftp_client.connection.getcwd()
    assert cwd == "/"
    