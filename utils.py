import os
import shutil
import pandas as pd
from config import *

def FILE_ORGANIZER_SCRIPT(csv_dir,data_dir):
    
    df = pd.read_csv(csv_dir)
    file_label_pairs = df[['fname', 'label']].values

    for fname, label in file_label_pairs:
    # Create the label directory if it doesn't exist
        label_dir = os.path.join(data_dir, label)
        os.makedirs(label_dir, exist_ok=True)
    
    # Move the file to the label directory
        src_path = os.path.join(data_dir, fname)
        dst_path = os.path.join(label_dir, fname)
        shutil.move(src_path, dst_path)

