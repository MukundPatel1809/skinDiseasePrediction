import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from glob import glob
from PIL import Image
%matplotlib inline

base = 'C:\cloudxlab\skin_identification\dataverse_files'

metadata = pd.read_csv(os.path.join(base,'HAM10000_metadata.csv'))

#metadata.info()
#if we combine data into one directory then no need to mention *
image_path = {os.path.splitext(os.path.basename(x))[0]: x
              for x in glob(os.path.join('C:\cloudxlab\skin_identification\dataverse_files/','*','*.jpg'))}


metadata['path'] = metadata['image_id'].map(image_path.get)

#upload data into dataset with resize 254,254
metadata['image'] = metadata['path'].map(lambda x: np.asarray(Image.open(x).resize((254,254))))


n_samples = 5  # number of samples for plotting
# Plotting
fig, m_axs = plt.subplots(7, n_samples, figsize = (4*n_samples, 3*7))
for n_axs, (type_name, type_rows) in zip(m_axs, 
                                         metadata.sort_values(['dx']).groupby('dx')):
    n_axs[0].set_title(type_name)
    for c_ax, (_, c_row) in zip(n_axs, type_rows.sample(n_samples, random_state=1234).iterrows()):
        c_ax.imshow(c_row['image'])
        c_ax.axis('off')
        
        
metadata['image'].info()

plt.imshow(data[:,:,0])
metadata['image'][0]


