from ds_messenger import DirectMessenger

# ds_messenger = DirectMessenger(dsuserver="168.235.86.101",
#                                username="nicaiwoshishei",
#                                password="buxiangshuohua")
#
ds_messenger = DirectMessenger(dsuserver="168.235.86.101",
                               username="math2e",
                               password="math")


# result2 = ds_messenger.send(message="hi",
#                             recipient="nicaiwoshishei")

result2 = ds_messenger.send(message="hi, this is math2e",
                            recipient="SuperHammer")
# print(result2)

# ds_messenger.retrieve_new()
# ds_messenger.retrieve_all()
