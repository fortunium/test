import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf
x=2
y=3
op1=tf.add(x,y)
with tf.Session() as sess:
  op1=sess.run(op1)
print(op1)
