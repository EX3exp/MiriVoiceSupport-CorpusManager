import json
import glob
import os
corpus_dictionary = {}

def gen_dictionary():

    data = {}
    for json_file in glob.glob('datas/*.json'):
        with open(json_file, 'r') as f:
            data = json.load(f)
        
        for style in data['styles']:
            ipa_file = style['ipa_filename']
            with open('datas/' + data['language'] + '-' + data["corpus_identifier"] + f"/{ipa_file}", 'r', encoding="utf-8") as f:
                ipas = f.readlines()
                for ipa in ipas:
                    corpus_dictionary[ipa.split("|")[0] + ".wav"] = "|".join(ipa.split("|")[1:])

def gen_transcript(prefix, filelist: list, transcript_path: str): # e.g train, train_list , filepath
    if len(corpus_dictionary) == 0:
        gen_dictionary()

    transcription = []
    for file in filelist:
        if file in corpus_dictionary.keys():
            transcription.append((prefix + "/" + file + "|" + corpus_dictionary[file]).strip())

    with open(transcript_path, 'w', encoding="utf-8") as f:
        f.write("\n".join(transcription))
            
            