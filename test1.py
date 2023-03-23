from ds_messenger import DirectMessenger

ds_messenger = DirectMessenger(dsuserver="168.235.86.101",
                               username="nicaiwoshishei",
                               password="buxiangshuohua")

# ds_messenger = DirectMessenger(dsuserver="168.235.86.101",
#                                username="VC1",
#                                password="VC")


# result2 = ds_messenger.send(message="this is juan",
#                             recipient="nicaiwoshishei")
# print(result2)

# ds_messenger.retrieve_new()
ds_messenger.retrieve_all()
