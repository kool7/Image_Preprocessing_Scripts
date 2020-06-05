import os
import glob
from tqdm import tqdm
from PIL import Image, ImageFile
from joblib import Parallel, delayed

ImageFile.LOAD_TRUNCATED_IMAGES = True


# resizing function
def fastResize(image_path, output_folder, resize):
    basename = os.path.basename(image_path)
    output = os.path.join(output_folder, basename)
    image = Image.open(image_path)
    image = image.resize((resize[1], resize[0]), resample = Image.BILINEAR)
    image.save(output)

# defining path
inputpath = 'input image path'
output = 'output resized image path'
images = glob.glob(os.path.join(inputpath, '*jpg'))

# parallelize operation for speed up operation.
Parallel(n_jobs=4)(
    delayed(fastResize)(
        i,
        output,
        (512, 512)
    ) for i in tqdm(images)    
)