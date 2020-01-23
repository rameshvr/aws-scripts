import boto3

resource = boto3.resource('iam')
client = boto3.client("iam")

KEY = 'LastUsedDate'

for user in resource.users.all():
    Metadata = client.list_access_keys(UserName=user.user_name)
    if Metadata['AccessKeyMetadata']:
        for key in user.access_keys.all():
            AccessId = key.access_key_id
            Status = key.status
            LastUsed = client.get_access_key_last_used(AccessKeyId=AccessId)
            if (Status == "Active"):
                if KEY in LastUsed['AccessKeyLastUsed']:
                    print("User: ", user.user_name,  "Key: ", AccessId,
                          "AK Last Used: ", LastUsed['AccessKeyLastUsed'][KEY])
                else:
                    print("User: ", user.user_name, "Key: ",
                          AccessId, "Key is Active but NEVER USED")
            else:
                print("User: ", user.user_name, "Key: ",
                      AccessId, "Keys is InActive")
    else:
        print("User: ", user.user_name, "No KEYS for this USER")
