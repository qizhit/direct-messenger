from ds_messenger import DirectMessenger

# ds_messenger = DirectMessenger(dsuserver="168.235.86.101",
#                                username="nicaiwoshishei",
#                                password="buxiangshuohua")

ds_messenger = DirectMessenger(dsuserver="168.235.86.101",
                               username="VC1",
                               password="VC")

ds_messenger.connect()
result = ds_messenger.send(message="this is juan",
                           recipient="nicaiwoshishei")
print(result)

# ds_messenger2.retrieve_new()
# ds_messenger2.retrieve_all()
