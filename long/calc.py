import tensorflow as tf

def calc():
    x = tf.random.normal([4,32,32,3])
    print((x+tf.random.normal([3])).shape)

if __name__ == '__main__':
    calc()
