def autoencoder(X):
  from keras.layers import Input,Dropout,Dense,LSTM,TimeDistributed,RepeatVector
  from keras.models import Model 
  from keras import regularizers 

  inputs = Input(shape= (X.shape[1],X.shape[2]))
  L1 = LSTM(16, activation ='relu', return_sequences=True, 
            kernel_regularizer = regularizers.l2(0.0))(inputs)
  L2 = LSTM(4,activation ='relu',return_sequences=False)(L1)
  L3 = RepeatVector(X.shape[1])(L2)
  L4 = LSTM(4,activation ='relu',return_sequences=True)(L3)
  L5 = LSTM(16,activation ='relu',return_sequences=True)(L4)
  output = TimeDistributed(Dense(X.shape[2]))(L5)
  model =Model(inputs=inputs, outputs=output)
  return model
