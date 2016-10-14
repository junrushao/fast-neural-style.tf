import tensorflow as tf
import numpy as np
from scipy.misc import imread, imsave
import argparse
import time


def parse_args():
    parser = argparse.ArgumentParser(description = "Render image using pretrained model.")
    parser.add_argument("--input", type = str, required = True)
    parser.add_argument("--output", type = str, default = "./output.png")
    parser.add_argument("--model", type = str, required = True)
    parser.add_argument("--arch", type = str, default = "./models/model.meta")
    args = parser.parse_args()

    args.image = imread(args.input, mode = "RGB").astype(np.float32)
    args.image = np.expand_dims(args.image, axis = 0)
    return args


def run(session):
    args = parse_args()

    saver = tf.train.import_meta_graph(args.arch, clear_devices = True)
    saver.restore(session, args.model)
    inputs = tf.get_collection("inputs")[0]
    output = tf.get_collection("output")[0]

    time_s = time.time()
    result = output.eval({inputs : args.image})
    result = np.clip(result, 0.0, 255.0).astype(np.uint8)
    result = np.squeeze(result, 0)
    time_t = time.time()
    print "First time. Time used: ", time_t - time_s

    time_s = time.time()
    result = output.eval({inputs : args.image})
    result = np.clip(result, 0.0, 255.0).astype(np.uint8)
    result = np.squeeze(result, 0)
    time_t = time.time()
    print "Second time. Time used: ", time_t - time_s

    imsave(args.output, result)


def main():
    session = tf.Session()
    with session.as_default():
        run(session)


if __name__ == "__main__":
    main()
