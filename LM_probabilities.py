import numpy as np
import torch
import json
from transformers import AutoTokenizer, GPT2LMHeadModel, OpenAIGPTLMHeadModel, GPTNeoForCausalLM, AutoModelForCausalLM

class LM():

    def __init__(self):
        torch.cuda.empty_cache()
        torch.no_grad()

    def gen_tensor(self, in_text):
        # Process input
        context = self.enc.encode(in_text)
        context = torch.tensor(context[:50],
                               device=self.device,
                               dtype=torch.long).unsqueeze(0)   #encode then add words into tensor
        # print(context)
        return context

    def get_logits(self, tensor):
            pass

    def check_probabilities(self, in_text):
        '''
        Params:
        - in_text: str -- The text that you want to check

        Output:
        - payload: list of tuples -- tuple pair for every word in line (ranking, prob)
        '''
        #create tensor from text input
        context = self.gen_tensor(in_text)
        
        # Forward through the model
        logits = self.get_logits(context)


        # construct target and pred
        yhat = torch.softmax(logits[0, :], dim=-1)    #softmax on first column and drop last element (end of text token's logit array)
        
        y = context[0, :]  #tensor without end of text token, essentially massive list of tokens representing words
        
        # Sort the predictions for each timestep
        sorted_preds = np.argsort(-yhat.data.cpu().numpy())     #creates an array of the indexes corresponding to the yhat probabilities if they were sorted greatest to least

        # [pos, ...]
        real_topk_pos = list(
            [int(np.where(sorted_preds[i] == y[i].item())[0][0])
             for i in range(y.shape[0])])   #create vector of which place the word in text was in the returned predicted probability of every word to follow. if word was the 10th most likely, put 10 in vector

        real_topk_probs = yhat[np.arange(0, y.shape[0], 1), y].data.cpu().numpy().tolist()  #make list of probabilities of each of the tokens at each index

        real_topk_probs = list(map(lambda x: round(x, 5), real_topk_probs))     #round off decimals

        # create [(pos, prob), ...] from [pos, ...] and [prob, ...]
        out_list = list(zip(real_topk_pos, real_topk_probs))       #zip position in probability list and proabilities together
        
        if torch.cuda.is_available():
            torch.cuda.empty_cache()

        return out_list

class LM_GPT2(LM):
    def __init__(self):
        '''
        In the subclass, load the specific model and 
        tokenizer. use CUDA if available.
        '''
        self.device = torch.device(
            "cuda" if torch.cuda.is_available() else "cpu")
        self.enc = AutoTokenizer.from_pretrained("gpt2")
        self.model = GPT2LMHeadModel.from_pretrained("gpt2")
        self.model.to(self.device)
        self.model.eval()
        print("Loaded GPT-2 model!")
    
    def get_logits(self, tensor):
            return self.model(tensor).logits

class LM_GPT(LM):
    def __init__(self):
        '''
        In the subclass, load the specific model and 
        tokenizer. use CUDA if available.
        '''
        self.device = torch.device(
            "cuda" if torch.cuda.is_available() else "cpu")
        super(LM, self).__init__()
        self.enc = AutoTokenizer.from_pretrained('openai-gpt')
        self.model = OpenAIGPTLMHeadModel.from_pretrained('openai-gpt')
        self.model.to(self.device)
        self.model.eval()
        print("Loaded GPT model!")

    
    def get_logits(self, tensor):
            return self.model(tensor).logits

class LM_GPTneo(LM):
    def __init__(self):
        '''
        In the subclass, load the specific model and 
        tokenizer. use CUDA if available.
        '''
        self.device = torch.device(
            "cuda" if torch.cuda.is_available() else "cpu")
        self.enc = AutoTokenizer.from_pretrained("EleutherAI/gpt-neo-1.3B")
        self.model = GPTNeoForCausalLM.from_pretrained("EleutherAI/gpt-neo-1.3B")
        self.model.to(self.device)
        self.model.eval()
        print("Loaded GPT-neo model!")

class LM_DialoGPT(LM):
    def __init__(self):
        '''
        In the subclass, load the specific model and 
        tokenizer. use CUDA if available.
        '''
        self.device = torch.device(
            "cuda" if torch.cuda.is_available() else "cpu")
        self.enc = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
        self.model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")
        self.model.to(self.device)
        self.model.eval()
        print("Loaded DiabloGPT model!")

def run_all_tests(raw_text, models):
    '''
    given a line of text and the models to run against
    return [GPT results, GPT-2 results]
    '''
    return [ lm.check_probabilities(raw_text) for lm in models ]

def intake_file(in_file):
    '''
    given file path
    return list of each line, stripped
    '''
    obj = []
    with open(in_file, 'r') as ifile:
        while line := ifile.readline():
            obj.append(line.rstrip())
    return obj

def dump_file(out_file, obj):
    '''
    given file path and data object
    dump object to out_file
    '''
    with open(out_file, 'w') as ofile:
        json.dump(obj,ofile)

def intake_files_from_list(file_list, models):
    '''
    given list of file paths to intake and models
    intake each file
    run each line in file against models
    dump results to file paths +'.json'
    '''
    for fname in file_list:
        all_text = intake_file(fname)
        to_json = [run_all_tests(inp, models) for inp in all_text]
        dump_file(fname+".json", to_json)

def get_default_models():
    '''
    return [GPT model, GPT-2 model]
    '''
    return [LM_GPT(), LM_GPT2()]
