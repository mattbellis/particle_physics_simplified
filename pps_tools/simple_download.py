################################################################################
### Simplifies google drive download function to use one argument, using dictionaries ##########

def download_from_drive(filename):

    data = {}

    ## CLEO FILES ##
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
    data['Single_D0_to_phigamma_ISR_LARGE.hdf5']='1ekhDcNsiBLzoAgGk73np5IhN_og1OELGg'
    data['Single_D0_to_pipi_ISR_LARGE.hdf5']='1XYL_Tor7vG_iutTSi_cmjN7SM0cLduaV'
    data['Single_Dm_to_Kpipi_ISR_LARGE.hdf5']='13kpQ6cD_g7O3839x38h_ZLNEWZVNLJVg'
    data['Single_Dp_to_Kpipi_ISR_LARGE.hdf5']='1bYfk3WCPmHSyttmkmCbtBVoDbDGKlgQUg'
    data['data31_100k_LARGE.hdf5']='1LYmDkr4vzZGQDpo0cuQ2SVqnPAV16H7Q'
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

    download_file_from__google_drive(data[filename],'data/'+filename)
