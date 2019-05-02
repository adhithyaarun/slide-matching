'''Matching video lecture slides to the actual slides'''
import cv2 as cv
import numpy as np
import os
import sys
from skimage.measure import compare_ssim

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
# normxcorr = []
similarity = []
# corrMatches = []
simMatches = []

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
    # normxcorr = []
    similarity = []
    for slide in slides:
        # corr = cv.matchTemplate(
        #     slide['image'], frame['image'], cv.TM_CCORR_NORMED)
        sim = compare_ssim(slide['image'], frame['image'])
        similarity.append(sim)
        # normxcorr.append(corr)
    # corrMatchVal = max(normxcorr)
    # corrMatchSlide = normxcorr.index(corrMatchVal)
    simMatchVal = max(similarity)
    simMatchSlide = similarity.index(simMatchVal)

    # corrMatches.append((frame['name'], slides[corrMatchSlide]['name']))
    simMatches.append((frame['name'], slides[simMatchSlide]['name']))

# Writing to a file
outfile = open(FILE, 'w')
for match in simMatches:
    outfile.write(match[0] + ' ' + match[1] + '\n')

outfile.close()
