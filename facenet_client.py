#!/usr/bin/env python

import xmlrpc.client
import argparse
parser = argparse.ArgumentParser("client.py")
parser.add_argument("image_path", help="The path to the face image.", type=str)
args = parser.parse_args()
print(args.image_path)

s = xmlrpc.client.ServerProxy('http://localhost:8000')
print(s.get_identity(args.image_path))
