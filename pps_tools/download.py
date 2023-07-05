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
def download_file_from_google_drive(global_filename, local_filename):
    
    id = key_to_id_dictionary(global_filename)

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

################################################################################
### Simplifies google drive download function to use one argument, using dictionaries ##########

def key_to_id_dictionary(filename):

    data = {}

    ## CLEO FILES ##
    data['Single_D0B_to_KK_ISR_LARGE.hdf5']='1MC528teXmOHf53yvR7OQdfyWrcvwepQG'
    data['Single_D0B_to_Kenu_ISR_LARGE.hdf5']= '1TIFnXcArzTa33SIojUg6vu3CglWvxi6t'
    data['Single_D0B_to_Kpipi0_ISR_LARGE.hdf5']='1nCehurYp3U6TsoBAqrmBygePm24VNzAE'
    data['Single_D0B_to_Kstenu_ISR_LARGE.hdf5']='1N47ZmMrwSl9s3PjkvyyApYzsYEKehARk'
    data['Single_D0B_to_phigamma_ISR_LARGE.hdf5']='1yZG2fISiDZ66vB38xHs_DfwnHelupkSn'
    data['Single_D0B_to_pipi_ISR_LARGE.hdf5']='1YgAMjV1OqFIF4b1wVNwCTMit2qtS3Ear'
    data['Single_D0_to_KK_ISR_LARGE.hdf5']='1Cfce9iZFIMZcw91BuIzew2kpywXO6NzC'
    data['Single_D0_to_Kenu_ISR_LARGE.hdf5']='1RK_pAUG28WRsSzkIt6ZKoJYVUI-Wl3Y_'
    data['Single_D0_to_Kpi_LARGE.hdf5']='1ka_VfRtOUF77pXLNCLiRP9MLfTWHDFTs'
    data['Single_D0_to_Kpipi0_ISR_LARGE.hdf5']='1pWx79wKysdMKLtZZSnmAjkCY9gVH3Lhi'
    data['Single_D0_to_Kstenu_ISR_LARGE.hdf5']='1KwDImAdfXfD8y9dR3MR8RkQhP4Fo4GDT'
    data['Single_D0_to_phigamma_ISR_LARGE.hdf5']='1ekhDcNsiBLzoAgGk73np5IhN_og1OELG'
    data['Single_D0_to_pipi_ISR_LARGE.hdf5']='1XYL_Tor7vG_iutTSi_cmjN7SM0cLduaV'
    data['Single_Dm_to_Kpipi_ISR_LARGE.hdf5']='13kpQ6cD_g7O3839x38h_ZLNEWZVNLJVg'
    data['Single_Dp_to_Kpipi_ISR_LARGE.hdf5']='1bYfk3WCPmHSyttmkmCbtBVoDbDGKlgQU'
    data['data31_100k_LARGE.hdf5']='1LYmDkr4vzZGQDpo0cuQ2SVqnPAV16H7Q'
    data['small_CLEO_test_file.hdf5']='1zryK4QKZbAiRz4TQNbyA18fZwxZqtQxh'
    ## CMS FILES ##
    data['data.hdf5']='1bWHUZxDflq_Utdbm86wASyfi-N5VMhtQ'
    data['ttbar.hdf5']='17T9eFz2znHpr9bms3b9GJ_4rMFRBmiRf'
    data['wjets.hdf5']='1G6-mklbUEg2Dd3uDLERODPx0cmH8Ogd-'
    data['dy.hdf5']='1PZqqlWKE6qdeA50mJU5z2jVZ5bT_CNc7'
    data['ww.hdf5']='1wGxJ1SKGtUh3n7tqWJ12Sv-pBHjlmrqi'
    data['wz.hdf5']='1It4tQMhz_t-9dfPylaa1MMbvOg0gSqPS'
    data['zz.hdf5']='1Y3eFUb2gC6r1AGbcXQxLEBI39foO1etR'
    data['single_top.hdf5']='1UwYbWh6czZ6MTdWW9wTMph-tK_FkttzO'
    data['qcd.hdf5']='1J-97Viw5kKOlVZVHYmSFgZw4P8kJHAkG'
    data['dimuons_100k.hdf5']='13gCId3e815LUBsQvGz-MQHInAp8Fz8n2'
    data['dimuons_1000_collisions.hdf5']='1fU8bMs1ZOmTFePkmS_LmYZq9KfaqJG1z'
    data['small_cms_test_file.hdf5']='1GlysdzCZ3dpW2YXoJqqjte5TBOIwsVv2'
    ## BABAR FILES ##
    data['basicPID_R24-AllEvents-Run1-OnPeak-R24-38.hdf5']='1wpapCrJfKCHlgI2J9Av5OVsLueyhgj_k'
    data['basicPID_R24-AllEvents-Run1-OnPeak-R24-388.hdf5']='16cewG1_hO3H-_uSQZVBQ8cvlpT6Ezx4V'
    data['basicPID_R24-AllEvents-Run1-OnPeak-R24-1133.hdf5']='1-HPCb1d-NNnb6w6LzeOwxlG1iFcBO_cF'
    data['basicPID_R24-AllEvents-Run1-OnPeak-R24-1552.hdf5']='1js0sKXaDrJfCNIq7msatXZlOO9LSaUSW'
    data['basicPID_R24-AllEvents-Run1-OnPeak-R24-1694.hdf5']='19azB7SqT8OAKK8nyJlsEbLBZvn1NUXA6'
    data['basicPID_R24-AllEvents-Run1-OnPeak-R24-1920.hdf5']='1CSj0i6cm_A9VgO9ItaRnhmVnZvbdw1rS'
    data['basicPID_R24-AllEvents-Run1-OnPeak-R24-2026.hdf5']='1gT_SldMdsK_SKSiE2SYfMibbMND4vkGG'
    data['basicPID_R24-AllEvents-Run1-OnPeak-R24-2781.hdf5']='1OJJe8zDB0qVAc3IdR3ciedd9Bxk6oNLM'
    data['basicPID_R24-AllEvents-Run1-OnPeak-R24-2835.hdf5']='1zAlpzNtTCIV2WrEqwdcHYO-9di1dLdRO'
    data['small_BaBar_test_file.hdf5']='1kmmKqnhoGs7wnyVhwZrrlM0JSe8E13Oz'
    
    data['icecube_events_small.h5'] = '13eAyNzf4hI7i-y3d_Dr_-l2hnwPjQGqS'
    data['icecube_events_large.h5'] = '1HDPndeJDJxhScGsuF8shV_qKtKBj4z2M'
    data['icecube_Glashow_resonance_event.h5'] = '15vGHZSGMeLsbmTBaO8CIY9ptcJb2voAy'
    
    # SDSS
    data['SDSS_CMASS_north.dat'] = '18KiYS4jTvxl2tMQvcbzNx0xATDl1fvy2'
    data['SDSS_CMASS_north_small.dat'] = '11ieqxipjjasAoSOaYuQ2oSi_adK4zmjf'

    # CMS top quark
    data['data.h5'] = 'XXX'
    data['dy.h5'] = 'XXX'
    data['qcd.h5'] = 'XXX'
    data['single_top.h5'] = 'XXX'
    data['ttbar.h5'] = 'XXX'
    data['wjets.h5'] = 'XXX'
    data['ww.h5'] = 'XXX'
    data['wz.h5'] = 'XXX'  
    data['zz.h5'] = 'XXX'
    
    return(data[filename])

### simplified function to download files from Google Drive to COLAB ###
def download_from_drive(filename):
    
    download_file_from_google_drive(filename,'data/'+filename)

### simplified function to download files from Google Drive to LOCAL ###  
def download_drive_file(filename):
    download_file_from_google_drive(filename,'../data/'+filename)


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
