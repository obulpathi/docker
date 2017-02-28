import tensorflow as tf

x = tf.constant(2)
y = tf.constant(3)
z = x * y

session = tf.Session()
print(session.run(z))

######################

x = tf.constant("Hello, ")
y = tf.constant("World!")
z = x + y

session = tf.Session()
print(session.run(z))
