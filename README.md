# handtrack-evaluation
Evaluation system for handtracking from RGB, in comparison with Leap Motion

## Leap Motion
### Dependencies
1. To get the Leap Motion set up, first sign up for a developer account on https://www.leapmotion.com.
2. Once you have an account, log in and navigate to the SDK tab and download the `V2 SDK` for Mac OS and Linux.

### Project Installation
Change the following lines in `leap_motion/leap_evaluation.py`

1. On Line 4, set `TEXT_FILENAME` to whatever you want to call the text file. The default is `leap_position.txt`. Unless you set it, it will create a textfile in the same directory as `leap_evaluation.py`.
2. On Line 5, set `PATH_TO_LEAP_SDK` to the absolute path to the Leap Motion SDK lib directory.
3. On Lines 5-6, set the `window_width` and `window_height` to the dimensions of the video you plan to pass into the PerPixel handtracker.

If you have a python distribution from MacPorts or Homebrew you will need to use the install name tool to point to the correct version of python. Follow the steps in this [tutorial] (https://developer.leapmotion.com/documentation/python/devguide/Project_Setup.html?proglang=python).

## Evaluation 
### Steps to run the evaluation script

1. The script can be found at evaluation/compare.py
2. Run `python compare.py <path to ground truth> <path to algorithm>` in the shell to compare the performace using the fingertip positions from two algorithms
3. The script outputs a mean-squared error (MSE) averaged across the number of frames used

## Ground Truth Labeler

To obtain ground truth (x,y) coordinates for the fingertip positions. 

1. The script can be found at label_tool/labeler.py
2. Run python labeler.py --input <InputDir> --output <OutputDir>, where the input directory contains the images to be labeled
3. Make sure to label the fingertips in the same order, as extracted using any tracking algorithms. Currently, the tracking algorithm finds the fingertips with the highest y-coordinate to the lowest
4. The script contains additional information for the labeler tool
