import tensorflow as tf

mnist = tf.contrib.learn.datasets.load_dataset('mnist')

classifier = tf.contrib.learn.LinearClassifier(n_classes=10)

classifier.fit(mnist.train.images, mnist.train.labels)

score = metrics.accuracy_score(mnist.test.labels, \
  classifier.predict(mnist.test.images))

print('Accuracy: {0:f}'.format(score))
