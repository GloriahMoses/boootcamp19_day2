def data_type(data):
  """
  this function 
  """

  #create datype variable to hold data types
  datype = type (data)
  #set action for string data types
  if datype == str:
    return len(data)
  #set action for when None is passed
  elif data == None:
    return 'no value'
  #set action for booleans
  elif datype == bool:
    return data

  #set action for  integers
  if datype == int:
    #set actions for integer values compared to 100
    if data < 100:
      return "less than 100"
    elif data > 100:
      return "more than 100"
    else:
      return "equal to 100"
  #set actions for lists
  elif datype == list:
    if len(data) < 3:
      return None
    else:
      return data[2]