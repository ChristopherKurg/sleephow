
def train(loss, step):
    # learning_rate = tf.train.exponential_decay(LEARNING_RATE, global_step=step, decay_steps=MAX_ITERATIONS / 4,
    #                                            decay_rate=0.99)
    # return tf.train.RMSPropOptimizer(learning_rate, 0.99, momentum=0.9).minimize(loss, global_step=step)
    return tf.train.MomentumOptimizer(LEARNING_RATE, 0.9).minimize(loss, global_step=step)
