from dkany.data_hosts.sftp import SftpClient
import os 

# def test_akamai_sftp_client():

#     akamai_sftp_client = SftpClient(
#         host = "cmsstorage.upload.akamai.com",
#         username = "sshacs",
#         private_key_file = os.environ['DKAN_AKAMAI_PRIVATE_KEY'],
#         private_key_pass = os.environ['DKAN_AKAMAI_PRIVATE_KEY_PASSWORD']
#     )

#     output = akamai_sftp_client.connection.listdir('/399963/questions.medicaid.gov/production/wwwroot/data/scorecard')

#     print(output)