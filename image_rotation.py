from PIL import Image 
from PIL import ImageFilter 
import os 
from tqdm import tqdm
import argparse 

def rotate_images(inputFolder,outputFolder,rot_angle): 
    if not os.path.exists(outputFolder):
      os.makedirs(outputFolder)

    for imagePath in tqdm(os.listdir(inputFolder)): 
        inputPath = os.path.join(inputFolder, imagePath) 
        img = Image.open(inputPath) 
        if rot_angle==90:
          img.rotate(90).save(os.path.join(outputFolder, '90'+imagePath))
        elif rot_angle==180:
          img.rotate(180).save(os.path.join(outputFolder, '180'+imagePath)) 
        elif rot_angle==270:
          img.rotate(270).save(os.path.join(outputFolder, '270'+imagePath))
        
 
if __name__ == '__main__': 
    parser=argparse.ArgumentParser()
    parser.add_argument("--input_path", type=str, default="data", help="Input data folder")
    parser.add_argument("--output_path", type=str, default="out", help="Output data folder")
    parser.add_argument("--angle", type=int, default=180, help="Image rotation angle")
    par = parser.parse_args()
    rotate_images(par.input_path,par.output_path,par.angle) 