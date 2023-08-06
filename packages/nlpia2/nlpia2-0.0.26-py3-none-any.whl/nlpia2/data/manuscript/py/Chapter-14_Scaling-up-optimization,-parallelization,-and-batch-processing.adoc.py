from nlpia.loaders import get_data
wv = get_data('word2vec')  # <1>
len(wv.vocab), len(wv[next(iter(wv.vocab))])
wv.vectors.shape
from annoy import AnnoyIndex
num_words, num_dimensions = wv.vectors.shape  # <1>
index = AnnoyIndex(num_dimensions)
from tqdm import tqdm  # <1>
for i, word in enumerate(tqdm(wv.index2word)):  # <2>
    index.add_item(i, wv[word])
import numpy as np
num_trees = int(np.log(num_words).round(0))  # <1>
num_trees
index.build(num_trees)  # <2>
index.save('Word2vec_euc_index.ann')  # <3>
w2id = dict(zip(range(len(wv.vocab)), wv.vocab))
wv.vocab['Harry_Potter'].index  # <1>
wv.vocab['Harry_Potter'].count  # <2>
w2id = dict(zip(
    wv.vocab, range(len(wv.vocab))))  # <3>
w2id['Harry_Potter']
ids = index.get_nns_by_item(
    w2id['Harry_Potter'], 11)  # <4>
ids
[wv.vocab[i] for i in _]
[wv.index2word[i] for i in _]
[word for word, similarity in wv.most_similar('Harry_Potter', topn=10)]
index_cos = AnnoyIndex(
    f=num_dimensions, metric='angular')  # <1>
for i, word in enumerate(wv.index2word):
    if not i % 100000:
        print('{}: {}'.format(i, word))  # <2>
    index_cos.add_item(i, wv[word])
index_cos.build(30)  # <1>
index_cos.save('Word2vec_cos_index.ann')
ids_cos = index_cos.get_nns_by_item(w2id['Harry_Potter'], 10)
ids_cos
[wv.index2word[i] for i in ids_cos]  # <1>
pd.DataFrame(annoy_top10, columns=['annoy_15trees',
                                   'annoy_30trees'])  # <1>
from sklearn.preprocessing import MinMaxScaler
real_values = [-1.2, 3.4, 5.6, -7.8, 9.0]
scaler = MinMaxScaler()  # <1>
scaler.fit(real_values)
import numpy as np
def training_set_generator(data_store,
                           batch_size=32):  # <1>
    X, Y = [], []
    while True: <2>
        with open(data_store) as f:  # <3>
            for i, line in enumerate(f): <4>
                if i % batch_size == 0 and X and Y: # <5>
                    yield np.array(X), np.array(Y)
                    X, Y = [], []
                x, y = line.split('|')  # <6>
                X.append(x)
                Y.append(y)
data_store = '/path/to/your/data.csv'
training_set = training_set_generator(data_store)
model.fit(x=X,
          y=Y,
          batch_size=32,
          epochs=10,
          verbose=1,
          validation_split=0.2)
data_store = '/path/to/your/data.csv'
model.fit_generator(generator=training_set_generator(data_store,
    batch_size=32),  # <1>
                    steps_per_epoch=100,  # <2>
                    epochs=10,  # <3>
                    verbose=1,
                    validation_data=[X_val, Y_val])  # <4>
model.evaluate_generator(generator=your_eval_generator(eval_data,
    batch_size=32), steps=10)
model.predict_generator(generator=your_predict_generator(\
    prediction_data, batch_size=32), steps=10)
import os
import tensorflow as tf
import numpy as np
from io import open
from tensorflow.contrib.tensorboard.plugins import projector
def create_projection(projection_data,
                      projection_name='tensorboard_viz',
                      path='/tmp/'):  # <1>
    meta_file = "{}.tsv".format(projection_name)
    vector_dim = len(projection_data[0][1])
    samples = len(projection_data)
    projection_matrix = np.zeros((samples, vector_dim))

    with open(os.path.join(path, meta_file), 'w') as file_metadata:
        for i, row in enumerate(projection_data):  # <2>
            label, vector = row[0], row[1]
            projection_matrix[i] = np.array(vector)
            file_metadata.write("{}\n".format(label))

    sess = tf.InteractiveSession()  # <3>

    embedding = tf.Variable(projection_matrix,
                            trainable=False,
                            name=projection_name)
    tf.global_variables_initializer().run()

    saver = tf.train.Saver()
    writer = tf.summary.FileWriter(path, sess.graph)  # <4>

    config = projector.ProjectorConfig()
    embed = config.embeddings.add()
    embed.tensor_name = '{}'.format(projection_name)
    embed.metadata_path = os.path.join(path, meta_file)

    projector.visualize_embeddings(writer, config) <5>
    saver.save(sess, os.path.join(path, '{}.ckpt'\
        .format(projection_name)))
    print('Run `tensorboard --logdir={0}` to run\
          visualize result on tensorboard'.format(path))
projection_name = "NLP_in_Action"
projection_data = [
    ('car', [0.34, ..., -0.72]),
    ...
    ('toy', [0.46, ..., 0.39]),
]
create_projection(projection_data, projection_name)
