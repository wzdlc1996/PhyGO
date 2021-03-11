#!/usr/bin/python

import os
import argparse

pars = argparse.ArgumentParser("Initialize the project with given name and user")
pars.add_argument(
    "-u",
    type=str,
    dest="username",
    nargs="+",
    default="Leonard",
    help="The username in this project. Can be a string or a series of strings"
)
pars.add_argument(
    "-p",
    type=str,
    dest="projName",
    help="The project name want to be initialize"
)
args = pars.parse_args()
print(args)

if args.projName is None:
    raise ValueError("The project name is required")
existFiles = os.listdir("./")
if args.projName in existFiles:
    raise ValueError("The project exists")
os.mkdir("./{}".format(args.projName))
os.mkdir("./{}/{}".format(args.projName, "Books"))
with open("./{}/{}/temp.txt".format(args.projName, "Books"), "w") as f:
    f.write("Waiting for knowledges")
if type(args.username) == str:
    usrs = [args.username]
elif type(args.username) == list:
    usrs = args.username
else:
    raise ValueError("Invalid username style, should be a list of string or a string")

for x in usrs:
    usrdir = "./{}/{}".format(args.projName, x)
    os.mkdir(usrdir)
    os.mkdir(usrdir + "/Base")
    for i in range(1, 3):
        baseChapDir = usrdir + "/Base/Chap_%0.2d" % i
        os.mkdir(baseChapDir)
        with open(baseChapDir + "/Note_%0.2d.md" % i, "w") as f:
            f.write("# Note Template")