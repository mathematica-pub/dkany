import pysftp

class SftpClient(object):
    def __init__(
            self,
            host=None,
            username=None,
            private_key_file=None,
            private_key_pass=None,
            remote_working_dir=None,
            hostkeys=None
        ):
        
        self.remote_working_dir = remote_working_dir
        cnopts = pysftp.CnOpts()
        # Attempted to get a valid hostkey from Akamai with a waka ticket,
        # but because of details of their setup it seems like it might not be possible
        # to get a relevent one
        cnopts.hostkeys = hostkeys

        self.connection = pysftp.Connection(
            host,
            username,
            private_key=private_key_file,
            private_key_pass=private_key_pass,
            cnopts = cnopts
        )