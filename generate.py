#!/usr/bin/env python
from json import loads

type_trans = {
    "analog_gauge": "GAUGE",
    "analog_dial": "DIAL",
    "limited_dial": "LIMITDIAL",
    "led": "LED",
    "selector": "SELECTOR",
    "display": "DISPLAY",
    "metadata": "METADATA",
    "3Pos_2Command_Switch_OpenClose": "3POS2"
}


source="/home/krorvik/win/OneDrive/Documents/code/dcs-bios/Scripts/DCS-BIOS/doc/json/F-16C_50.json"

fd = open(source, 'ro')

data = loads(fd.read())

for category, cdata in data.iteritems():
    for key, item in cdata.iteritems():
        if 'outputs' in item and len(item['outputs']) > 0:
            ident = item['identifier']
            ctype = item['control_type']
            for output in item['outputs']:
                if 'description' in output:
                    print "//\n// Category: %s\n// Item: %s  \n// Description: %s\n//" % (category, ident, output['description'])
                if 'address' in output:
                    print "#define %s_%s_ADDRESS %s" % (ident, type_trans[ctype], hex(output['address']))
                if 'mask' in output:
                    print "#define %s_%s_MASK %s" % (ident, type_trans[ctype], hex(output['mask']))
                if 'shift_by' in output:
                    print "#define %s_%s_SHIFTBY %s" % (ident, type_trans[ctype], hex(output['shift_by']))
