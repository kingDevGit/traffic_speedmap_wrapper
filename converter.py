'''
Author: Minhyung Joo
Version: 1.0
'''

import json
import math
import requests
import xml.etree.ElementTree as et

url = 'http://resource.data.one.gov.hk/td/speedmap.xml'

def get_speeds():
    response = requests.get(url)
    tree = et.fromstring(response.content)

    with open('converted_speedmap.xml', 'w') as converted_xml:
        converted_xml.write("<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>\n")
        converted_xml.write("""<jtis_speedlist
                            xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"
                            xmlns=\"http://data.one.gov.hk/td\"
                            xsi:schemaLocation=\"http://data.one.gov.hk/td
                            http://data.one.gov.hk/xsd/td/speedmap.xsd\">\n""")
        with open('nodes.json', 'r') as node_file:
            nodelist = json.load(node_file)

            for speedmap in tree:
                converted_xml.write("\t<jtis_speedmap>\n")
                link_id      = speedmap[0].text
                region       = speedmap[1].text
                road_type    = speedmap[2].text
                saturation   = speedmap[3].text
                speed        = speedmap[4].text
                capture_date = speedmap[5].text

                nodes      = link_id.split('-')
                start_node = nodes[0]
                end_node   = nodes[1]

                start_lat = nodelist[start_node][0]
                start_lng = nodelist[start_node][1]
                end_lat   = nodelist[start_node][0]
                end_lng   = nodelist[start_node][1]

                converted_xml.write("\t\t<LINK_ID>" + link_id + "</LINK_ID>\n")
                converted_xml.write("\t\t<START_LAT>" + str(start_lat) + "</START_LAT>\n")
                converted_xml.write("\t\t<START_LNG>" + str(start_lng) + "</START_LNG>\n")
                converted_xml.write("\t\t<END_LAT>" + str(end_lat) + "</END_LAT>\n")
                converted_xml.write("\t\t<END_LNG>" + str(end_lng) + "</END_LNG>\n")
                converted_xml.write("\t\t<REGION>" + region + "</REGION>\n")
                converted_xml.write("\t\t<ROAD_TYPE>" + road_type + "</ROAD_TYPE>\n")
                converted_xml.write("\t\t<ROAD_SATURATION_LEVEL>" + saturation + "</ROAD_SATURATION_LEVEL>\n")
                converted_xml.write("\t\t<TRAFFIC_SPEED>" + speed + "</TRAFFIC_SPEED>\n")
                converted_xml.write("\t\t<CAPTURE_DATE>" + capture_date + "</CAPTURE_DATE>\n")

                converted_xml.write("\t</jtis_speedmap>\n")
            # break
        converted_xml.write("</jtis_speedlist>")

def main():
    get_speeds()

if __name__ == '__main__':
    main()
