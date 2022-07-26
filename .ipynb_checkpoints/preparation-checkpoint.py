def to_lstm(dataframes,time_step,features_name,hop=1):
  import numpy as np
  import librosa,librosa.display

  data = []
  for i in dataframes:
    l=[]
    for j in features_name:
      slices = librosa.util.frame(i[j].to_numpy(),frame_length = time_step,hop_length = hop).T
      l.append(slices)
    data.append(np.stack(l,axis=-1))
  return np.concatenate(data)
