import sys
import zipfile
import os
import shutil
import random
import corpus_manager as cm

if __name__ == '__main__':
    recorded_zip_path = sys.argv[1]
    dataset_zip_path = sys.argv[2]

    random.seed(42)

    with zipfile.ZipFile(recorded_zip_path, 'r') as zip_ref:
        zip_ref.extractall('tmp')
    
    shutil.rmtree('dataset', ignore_errors=True)

    os.makedirs('dataset/train', exist_ok=True)
    os.makedirs('dataset/validation', exist_ok=True)
    
    recfiles = os.listdir('tmp')
    
    # split train/val sets
    recfiles = [f for f in recfiles if f.endswith('.wav')]

    random.shuffle(recfiles)
    split_index = int(len(recfiles) * 0.9)

    train = recfiles[:split_index]  
    val = recfiles[split_index:]

    for f in train:
        shutil.move(f'tmp/{f}', f'dataset/train/{f}')
    
    for f in val:
        shutil.move(f'tmp/{f}', f'dataset/validation/{f}')
    
    train_list = [f for f in os.listdir('dataset/train') if f.endswith('.wav')]
    val_list = [f for f in os.listdir('dataset/validation') if f.endswith('.wav')]

    cm.gen_transcript('train', train_list, 'dataset/train/filelist_train.txt.cleaned')
    cm.gen_transcript('validation', val_list, 'dataset/validation/filelist_val.txt.cleaned')


    with zipfile.ZipFile(dataset_zip_path, 'a') as zip_ref:
        zip_ref.write('dataset', 'dataset', compress_type=zipfile.ZIP_DEFLATED)

    shutil.rmtree('tmp')
    shutil.rmtree('dataset')
    
