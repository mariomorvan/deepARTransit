import os
import tensorflow as tf
from deepartransit.models import deepar
from deepartransit.utils.config import process_config
from deepartransit.data_handling import data_generator
from deepartransit.utils.dirs import create_dirs
from deepartransit.utils.logger import Logger

config_path = os.path.join('tests', 'deepar_config_test.yml')


def test_deepar_init():
    config = process_config(config_path)

    create_dirs([config.summary_dir, config.checkpoint_dir])
    model = deepar.DeepARModel(config)
    #model.delete_checkpoints()
    data = data_generator.DataGenerator(config)

    init = tf.global_variables_initializer()
    with tf.Session() as sess:
        sess.run(init)
        logger = Logger(sess, config)
        trainer = deepar.DeepARTrainer(sess, model, data, config, logger)
        trainer.train()

"""
def test_deepar_load():
    config = process_config(config_path)
    model = deepar.DeepARModel(config)
    data_handling = dataset.DataGenerator(config)

    init = tf.global_variables_initializer()
    with tf.Session() as sess:
        sess.run(init)
        trainer = deepar.DeepARTrainer(sess, model, data_handling, config)
        model.load(sess)
        model.train()
"""