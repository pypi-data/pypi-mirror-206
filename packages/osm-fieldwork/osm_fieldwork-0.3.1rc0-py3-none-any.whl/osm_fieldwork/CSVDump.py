#!/usr/bin/python3

# Copyright (c) 2020, 2021, 2022, 2023 Humanitarian OpenStreetMap Team
#
# This file is part of OSM-Fieldwork.
#
#     OSM-Fieldwork is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     OSM-Fieldwork is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with OSM-Fieldwork.  If not, see <https:#www.gnu.org/licenses/>.
#

import argparse
import csv
import os
import logging
import sys
from sys import argv
from osm_fieldwork.convert import Convert
from osm_fieldwork.osmfile import OsmFile
from osm_fieldwork.xlsforms import xlsforms_path
from geojson import Point, Feature, FeatureCollection, dump

# set log level for urlib
log_level = os.getenv("LOG LEVEL", default="INFO")
logging.getLogger("urllib3").setLevel(log_level)

log = logging.getLogger(__name__)


class CSVDump(Convert):
    """A class to parse the CSV files from ODK Central"""

    def __init__(self, yaml=None):
        """"""
        self.fields = dict()
        self.nodesets = dict()
        self.data = list()
        self.osm = None
        self.json = None
        self.features = list()
        path = xlsforms_path.replace("xlsforms", "")
        if type(yaml) == str:
            file = f"{path}{xform}"
        else:
            file = f"{path}/xforms.yaml"
        self.config = super().__init__(yaml)

    def createOSM(self, filespec="tmp.osm"):
        """Create an OSM XML output files"""
        logging.debug("Creating OSM XML file: %s" % filespec)
        self.osm = OsmFile(filespec=filespec)
        self.osm.header()

    def writeOSM(self, feature):
        """Write a feature to an OSM XML output file"""
        out = ""
        if "id" in feature["tags"]:
            feature["id"] = feature["tags"]["id"]
        if "lat" not in feature["attrs"] or "lon" not in feature["attrs"]:
            return None
        if "refs" not in feature:
            out += self.osm.createNode(feature)
        else:
            out += self.osm.createWay(feature)
        self.osm.write(out)

    def finishOSM(self):
        """Write the OSM XML file footer and close it"""
        self.osm.footer()

    def createGeoJson(self, file="tmp.geojson"):
        """Create a GeoJson output file"""
        logging.debug("Creating GeoJson file: %s" % file)
        self.json = open(file, "w")

    def writeGeoJson(self, feature):
        """Write a feature to a GeoJson output file"""
        # These get written later when finishing , since we have to create a FeatureCollection
        if "lat" not in feature["attrs"] or "lon" not in feature["attrs"]:
            return None
        self.features.append(feature)

    def finishGeoJson(self):
        """Write the GeoJson FeatureCollection to the output file and close it"""
        features = list()
        for item in self.features:
            poi = Point((float(item["attrs"]["lon"]), float(item["attrs"]["lat"])))
            if "private" in item:
                props = {**item["tags"], **item["private"]}
            else:
                props = item["tags"]
            features.append(Feature(geometry=poi, properties=props))
        collection = FeatureCollection(features)
        dump(collection, self.json)

    def parse(self, filespec=None, data=None):
        """Parse the CSV file from ODK Central and convert it to a data structure"""
        all_tags = list()
        if not data:
            open(filespec, newline="")
            reader = csv.DictReader(filespec, delimiter=",")
        else:
            reader = csv.DictReader(data, delimiter=",")
        for row in reader:
            tags = dict()
            # logging.info(f"ROW: {row}")
            for keyword, value in row.items():
                if keyword is None or len(keyword) == 0:
                    continue

                base = self.basename(keyword).lower()
                # There's many extraneous fields in the input file which we don't need.
                if (
                    base is None
                    or base in self.ignore
                    or value is None
                    or len(value) == 0
                ):
                    continue
                # if base in self.multiple:
                #     epdb.st()
                #     entry = reader[keyword]
                #     for key, val in entry.items():
                #         print(key)
                #         if key == "name":
                #             tags['name'] = val
                #     continue
                else:
                    items = self.convertEntry(base, value)
                    if len(items) > 0:
                        if type(items[0]) == str:
                            tags[items[0]] = items[1]
                        elif type(items[0]) == dict:
                            for entry in items:
                                for k, v in entry.items():
                                    tags[k] = v
                    else:
                        tags[base] = value
                # logging.debug(f"\tFIXME1: {tags}")
            all_tags.append(tags)
        return all_tags

    def basename(self, line):
        """Extract the basename of a path after the last -"""
        tmp = line.split("-")
        if len(tmp) == 0:
            return line
        base = tmp[len(tmp) - 1]
        return base

    def createEntry(self, entry=None):
        """Create the feature data structure"""
        # print(line)
        feature = dict()
        attrs = dict()
        tags = dict()
        priv = dict()
        refs = list()

        logging.debug("Creating entry")
        # First convert the tag to the approved OSM equivalent
        for key, value in entry.items():
            attributes = (
                "id",
                "timestamp",
                "lat",
                "lon",
                "uid",
                "user",
                "version",
                "action",
            )
            # When using existing OSM data, there's a special geometry field.
            # Otherwise use the GPS coordinates where you are.
            if key == "geometry":
                geometry = value.split(" ")
                if len(geometry) == 4:
                    attrs["lat"] = geometry[0]
                    attrs["lon"] = geometry[1]
                continue

            if key is not None and len(key) > 0 and key in attributes:
                attrs[key] = value
                logging.debug("Adding attribute %s with value %s" % (key, value))
            else:
                if key in self.multiple:
                    for item in value:
                        if key in item:
                            for entry in item[key].split():
                                vals = self.getValues(key)
                                if entry in vals:
                                    if vals[entry].find("="):
                                        tmp = vals[entry].split("=")
                                        tags[tmp[0]] = tmp[1]
                                else:
                                    tags[entry] = "yes"
                    continue

                if value is not None and value != "no" and value != "unknown":
                    if key == "track" or key == "geoline":
                        refs.append(tag)
                        logging.debug("Adding reference %s" % tag)
                    elif len(value) > 0:
                        if self.privateData(key):
                            priv[key] = value
                        else:
                            tags[key] = value
            if len(tags) > 0:
                feature["attrs"] = attrs
                feature["tags"] = tags
            if len(refs) > 0:
                feature["refs"] = refs
            if len(priv) > 0:
                feature["private"] = priv

        return feature


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="convert CSV from ODK Central to OSM XML"
    )
    parser.add_argument("-v", "--verbose", action="store_true", help="verbose output")
    parser.add_argument("-y", "--yaml", help="Alternate YAML file")
    parser.add_argument(
        "-i", "--infile", help="The input file downloaded from ODK Central"
    )
    args = parser.parse_args()
    
    #logging
    logging.basicConfig(
        level=log_level,
        format=(
            "%(asctime)s.%(msec)03d [%(levelname)s]"
            "%(name)s | %(funcName)s:%(lineno)d | %(message)s"
        ),
        datefmt="%y-%m-%d %H:%M:%S",
        stream=sys.stdout,
    )

    # if verbose, dump to the terminal.
    if args.verbose is not None:
        root = logging.getLogger()
        root.setLevel(logging.DEBUG)

        ch = logging.StreamHandler(sys.stdout)
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        ch.setFormatter(formatter)
        root.addHandler(ch)

    if args.yaml:
        csvin = CSVDump(args.yaml)
    else:
        csvin = CSVDump()
    osmoutfile = os.path.basename(args.infile.replace(".csv", ".osm"))
    csvin.createOSM(osmoutfile)

    jsonoutfile = os.path.basename(args.infile.replace(".csv", ".geojson"))
    csvin.createGeoJson(jsonoutfile)

    logging.debug("Parsing csv files %r" % args.infile)
    data = csvin.parse(args.infile)
    # This OSM XML file only has OSM appropriate tags and values
    for entry in data:
        feature = csvin.createEntry(entry)
        # Sometimes bad entries, usually from debugging XForm design, sneak in
        if len(feature) == 0:
            continue
        if len(feature) > 0:
            if "lat" not in feature["attrs"]:
                logging.warning("Bad record! %r" % feature)
                continue
            csvin.writeOSM(feature)
            # This GeoJson file has all the data values
            csvin.writeGeoJson(feature)
            # print("TAGS: %r" % feature['tags'])

    csvin.finishOSM()
    csvin.finishGeoJson()
    logging.info("Wrote OSM XML file: %r" % osmoutfile)
    logging.info("Wrote GeoJson file: %r" % jsonoutfile)
