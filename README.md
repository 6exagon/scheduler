# Scheduler

A simple schedule editor designed for handling course scheduling written for Python 2 or 3.

## Setup

### Requirements

This project only uses Python 2/3 and the Standard Library, so no need for any building or installing of third-party software. This project is also cross-platform, and runs on Windows, macOS, and Linux.

Also, Tk 8.5+ is required, but this is usually bundled in preinstalled or first-party distributions of Python.

### Installation & Use

#### Basic Cross-Platform Setup

Download and extract the .zip file for this project, and the python package can easily be run from a command line:

`$ python3 scheduler` or `$ python scheduler`

If the above fail on Windows, try:

`$ py -3 scheduler` or `$ py -2 scheduler`

#### macOS Application Setup

Download and extract the .zip file for this project and run the build script:

`$ mac-build.sh`

A standalone macOS application will be created that can be moved to the Applications folder. It will use Python 3 if possible or Python 2 if this is unavailable. The original project files can be discarded at this point.
