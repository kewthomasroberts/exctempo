import tensorflow as tf

# Define your input image tensor
input_image = tf.placeholder(tf.float32, shape=[None, height, width, channels])

# Define your convolutional layer with stride of 2
output = tf.layers.conv2d(inputs=input_image, filters=num_filters, kernel_size=kernel_size, strides=2, padding='same')

# Run the computation
with tf.Session() as sess:
    output_image = sess.run(output, feed_dict={input_image: input_data})
