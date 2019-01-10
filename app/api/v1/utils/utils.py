def generate_id(collection):
  """
    Function to generate id for collection
  """

  if len(collection) == 0:
    return 1

    return collection[-1]['id']+1