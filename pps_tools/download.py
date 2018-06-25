import requests
import os

################################################################################
# Grabbed the following snippet from 
# http://stackoverflow.com/questions/16694907/how-to-download-large-file-in-python-with-requests-py
#
# Works with just giving it the url, and assumes that the url contains in it a good filename,
#o# unless you pass in something else.
def download_file(url,local_filename=None):
    # Just assume that they will want a data directory

    if not os.path.exists('./data'):
            os.makedirs('./data')

    if local_filename is None:
        local_filename = "%s" % (url.split('/')[-1])

    # NOTE the stream=True parameter
    r = requests.get(url, stream=True)
    print("Downloading %s....." % (local_filename))
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
                f.flush()

    return local_filename
################################################################################

################################################################################
# Got this from here
# https://stackoverflow.com/questions/25010369/wget-curl-large-file-from-google-drive/39225039#39225039
# 
# id is the url "stub"
def download_file_from_google_drive(id, local_filename):

    if not os.path.exists('./data'):
            os.makedirs('./data')

    def get_confirm_token(response):
        for key, value in list(response.cookies.items()):
            if key.startswith('download_warning'):
                return value

        return None

    def save_response_content(response, local_filename):
        CHUNK_SIZE = 32768

        with open(local_filename, "wb") as f:
            for chunk in response.iter_content(CHUNK_SIZE):
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)

    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    save_response_content(response, local_filename)    
################################################################################


'''
if __name__ == "__main__":
    import sys
    if len(sys.argv) is not 3:
        print("Usage: python google_drive.py drive_file_id local_filename")
    else:
        # TAKE ID FROM SHAREABLE LINK
        file_id = sys.argv[1]
        # DESTINATION FILE ON YOUR DISK
        local_filename = sys.argv[2]
        download_file_from_google_drive(file_id, local_filename)
'''
