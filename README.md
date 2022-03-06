# Project: Detecting the Text of Users and Bots Using Machine Learning

Team Members:
    - Luckandlogic
    - Spoon
    - Butters
    - George


# isitabot
isitabot is an adversarial model to detect the likelyhood text being machine generated. Our text analysis tool can be used via a locally hosted application, or directly through its API.

## How to install
Requirements:
- Python version 3.9
    - Python 3.10 is not compatible with pytorch
    - Python 3.8 is not compatible with type hinting
To install the isitabot program:
- Clone the git repository
- Create a virtual environemt within the project directory with `python3.9 -m venv env`
- Enter the virtual environemt `source env/bin/activate`
- Install the required pip packages `pip3 install -r requirements.txt`
    - If your system is CUDA capable, verify you have the appropriate pytorch version at [the pytorch website](https://pytorch.org/get-started/locally/)
- Start the application with `./run.sh`. It will be hosted at `localhost:5000` by default

## API Usage
todo once setup on app
