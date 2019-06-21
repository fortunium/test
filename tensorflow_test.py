import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf
x=2
y=3
z=4
con11=tf.constant(2)
con12=tf.constant(4)
con13=tf.constant(5)
op111=tf.multiply(x,con11)
op112=tf.multiply(y,con12)
op113=tf.multiply(z,con13)
op11=tf.add(op111,op112,op113)
with tf.Session() as sess:
  op11=sess.run(op11)
print(op11)
