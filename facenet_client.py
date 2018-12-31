#!/usr/bin/env python

import xmlrpc.client
import argparse
parser = argparse.ArgumentParser('client.py')
parser.add_argument('image_path', help="The path to the face image.", type=str)
parser.add_argument('-v', '--verify', dest='name', help="Verify if the image has the face of the given name.", type=str)
args = parser.parse_args()
try:
    s = xmlrpc.client.ServerProxy("http://localhost:8000")
    if args.name:
        print(s.verify(args.image_path, args.name))
    else:
        print(s.get_identity(args.image_path))
except ConnectionRefusedError as e:
    print(e)
    print("The connection to facenet server has failed.")

