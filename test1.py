from ds_messenger import DirectMessenger

# ds_messenger = DirectMessenger(dsuserver="168.235.86.101",
#                                username="nicaiwoshishei",
#                                password="buxiangshuohua")

ds_messenger = DirectMessenger(dsuserver="168.235.86.101",
                               username="VC1",
                               password="VC")

result = ds_messenger.connect()
print(result)

result2 = ds_messenger.send(message="this is juan",
                            recipient=None)
print(result2)

# ds_messenger.retrieve_new()
# ds_messenger.retrieve_all()
