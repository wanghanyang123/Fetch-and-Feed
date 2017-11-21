import tensorflow as tf

input1=tf.constant(2)
input2=tf.constant(3)
input3=tf.constant(4)

add=tf.add(input2,input3)
mul=tf.multiply(input1,add)

with tf.Session() as sess:
    result=sess.run([add,mul])
    print(result)

x = tf.placeholder(tf.string)
y = tf.placeholder(tf.int32)
z = tf.placeholder(tf.float32)

with tf.Session() as sess:
    output = sess.run(y, feed_dict={x: 'Test String', y: 123, z: 45.67})
    print(output)
