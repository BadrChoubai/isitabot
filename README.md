# Project: Detecting the Text of Users and Bots Using Machine Learning

Team Members:
    - Max
    - Spoon
    - Butters
    - George


# isitabot
isitabot is an adversarial model to detect the likelihood of text being machine generated. Our text analysis tool can be used graphically or headlessly via a locally hosted application web application.

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
To use the API, send the text you wish to test in URL encoding to `http://localhost:5000/api/v1/resources/text?encoded_text=`. A sample query can be seen by clicking [here](http://localhost:5000/api/v1/resources/text?encoded_text=No%20less%20significant%20than%20Putin%E2%80%99s%20strategic%20error%20have%20been%20the%20Russian%20army%E2%80%99s%20tactical%20blunders.).

## Datasets used for ML development:
https://botometer.osome.iu.edu/bot-repository/

https://github.com/gunthercox/chatterbot-corpus/tree/master/chatterbot_corpus/data/english

https://github.com/ADGEfficiency/creative-writing-with-gpt2/blob/master/examples/alan-watts.md

https://blog.machinewrites.com/gpt-2-generated-chatbot-development-article-339/

https://github.com/gunthercox/chatterbot-corpus/tree/master/chatterbot_corpus/data/english
