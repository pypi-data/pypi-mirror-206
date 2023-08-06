class BaseConfig(object):

    PROJECT_PATH = 'C:\\Users\\Mach1\\OneDrive\\Documents\\Projects\\Pro Door\\'
    SAMPLE_PATH = '%sResources\\cXML\\1.2.057\\Samples\\' % PROJECT_PATH 
    XML_SAMPLES = {
        'ProfileResponse' : '%sprofileresponse.xml' % SAMPLE_PATH,
        'ProfileResponseNoDTD' : '%sprofileresponsenodtd.xml' % SAMPLE_PATH,
        'ProfileResponseInvalidXML' : '%sprofileresponseinvalidxml.xml' % SAMPLE_PATH,
        'ProfileResponseInvalidDTD' : '%sprofileresponseinvaliddtd.xml' % SAMPLE_PATH,
    }
    
