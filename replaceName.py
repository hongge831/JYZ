import os
model_dir = 'D:/PythonSpace/R2CNN_FPN_Tensorflow-insulator/output/res101_trained_weights/v5_new/'
from tensorflow.python import pywrap_tensorflow
#checkpoint_path = os.path.join(logs_train_dir, 'model.ckpt')
checkpoint_path = os.path.join(model_dir, "voc_78007model.ckpt")
reader = pywrap_tensorflow.NewCheckpointReader(checkpoint_path)
var_to_shape_map = reader.get_variable_to_shape_map()
for idx,key in enumerate(var_to_shape_map):
    print(str(idx)+":tensor_name: ", key)
    # print(reader.get_tensor(key))

