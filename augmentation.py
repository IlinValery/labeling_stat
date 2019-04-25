import Augmentor
import tensorflow as tf
import cv2
import os
import argparse



parser = argparse.ArgumentParser()
parser.add_argument("--folder", type=str,
                    help="Folder with *.jpg files. for example: --folder augmentation_data/carrot_L2_002/")
parser.add_argument("--videoname", type=str,
                    help="Video number for files *.jpg. For example: 004")
parser.add_argument("--additional", type=int,
                    help="Count of additional files. System create same count augmented data plus --additional count",
                    default=0)
args = parser.parse_args()


additional_augmentation = args.additional
folder = args.folder
video_number = args.videoname

path_to_source = folder + "output/"
path_to_augment = folder + "augment/"
os.system("rm -rf {0}".format(path_to_augment))
os.system("rm -rf {0}".format(path_to_source))


p = Augmentor.Pipeline(folder)
os.mkdir(path_to_augment)

p.rotate(probability=0.7, max_left_rotation=10, max_right_rotation=10)
p.zoom(probability=0.5, min_factor=1.1, max_factor=1.2)
p.random_distortion(probability=1, grid_width=2, grid_height=2, magnitude=8)
p.flip_top_bottom(0.5)
p.flip_left_right(0.5)

p.sample(additional_augmentation)

p.process()




lst = os.listdir(path_to_source)

cur_number = 0
for file in lst:
    cur_class = file.split('_')[0]
    cur_light = file.split('_')[1]
    cur_source_file = file.split('_')[2]
    cur_frame = file.split('_')[7]
    #print(file)
    #print(file.split('_'), cur_class, cur_number)
    filename = path_to_augment+"aug_"+cur_class+"_"+cur_light+"_"+video_number+"_"+str(cur_number)+"_"+"from_"+cur_source_file+"_"+cur_frame+".jpg"
    print("Create file:", filename)
    image = cv2.imread(str(path_to_source)+str(file))
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    tf_img = tf.convert_to_tensor(rgb)

    sat_image = tf.image.random_saturation(tf_img, lower=0.5, upper=1)
    contrast_image = tf.image.random_contrast(sat_image, lower=0.5, upper=1)
    brght_img = tf.image.random_brightness(contrast_image, max_delta=0.2)
    jpg = tf.image.random_jpeg_quality(brght_img, min_jpeg_quality=50, max_jpeg_quality=100)

    enc = tf.image.encode_jpeg(brght_img)
    fwrite = tf.write_file(filename, enc)


    with tf.Session() as sess:
        sess.run(fwrite)

    cur_number+=1

os.system("rm -rf {0}".format(path_to_source))
