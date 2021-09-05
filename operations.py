def normalize_transform(tensor,sc):
    
  for i in range(tensor.shape[1]):
    tensor[:, i, :] = sc[i].transform(tensor[:, i, :]) 
  return tensor


def normalize_fit(tensor):
  
  scalers = {}
  for i in range(tensor.shape[1]):
    scalers[i] = MinMaxScaler()
    tensor[:, i, :] = scalers[i].fit_transform(tensor[:, i, :]) 

  return tensor,scalers
