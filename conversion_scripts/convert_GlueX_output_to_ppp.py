import sys

# First dump the XML with something like....

# hddm-xml -n 10 -o this particle_gun012_001_rest.hddm

# Got this
# https://github.com/martinblech/xmltodict
# And to use it
# https://stackoverflow.com/questions/2148119/how-to-convert-an-xml-string-to-a-dictionary
import xmltodict

infile = open('this.xml')

xml = infile.read()

d = xmltodict.parse(xml)

a = d['HDDM'] 

a['reconstructedPhysicsEvent'][3]


