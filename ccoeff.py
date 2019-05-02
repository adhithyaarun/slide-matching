'''Matching video lecture slides to the actual slides'''
import cv2 as cv
import numpy as np
import os
import sys

# Arguments
SLIDE = sys.argv[1]
FRAME = sys.argv[2]

# Filename as per rollnumber
FILE = os.path.join('.', '20171066_20171062.txt')

# Filenames
slide_names = sorted(os.listdir(SLIDE))
frame_names = sorted(os.listdir(FRAME))

# Variable Initializations
slides = []
frames = []
normxcorr = []
matches = []

# Read Slides
for name in slide_names:
    image = cv.imread(os.path.join(SLIDE, name), 0)
    slides.append({'name': name, 'image': cv.resize(image, (1398, 1080))})

# Read Frames
for name in frame_names:
    image = cv.imread(os.path.join(FRAME, name), 0)
    frames.append({'name': name, 'image': cv.resize(image, (1398, 1080))})


# Match Frames to Slides
for frame in frames:
    normxcorr = []
    for slide in slides:
        # corr = cv.matchTemplate(slide['image'], frame['image'], cv.TM_CCORR_NORMED)
        corr = cv.matchTemplate(slide['image'], frame['image'], cv.TM_CCOEFF)
        normxcorr.append(corr)
    matchVal = max(normxcorr)
    matchSlide = normxcorr.index(matchVal)

    matches.append((frame['name'], slides[matchSlide]['name']))

# Writing to a file
outfile = open(FILE, 'w')
for match in matches:
    outfile.write(match[0] + ' ' + match[1] + '\n')

outfile.close()

