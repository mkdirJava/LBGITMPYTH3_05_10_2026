import pickle

#loading the pickle!
pickle_filename = "accounts.pkl"
pickle_file = open(pickle_filename, "rb")
accounts_dict = pickle.load(pickle_file)
pickle_file.close()

#checking the Pickle and its contents...
print(accounts_dict)
print(type(accounts_dict))
