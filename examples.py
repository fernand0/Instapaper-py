from instapypaper.instapaper import InstapaperAPI

api = InstapaperAPI('Your Consumer Key', 'Your Secret')
api.get_xauth_access_token('Username', 'Password')


#Make requests like this:
print api.GET.account.verify_credentials()
print api.GET.folders.list()
'''
For a given API URL, such as 
/api/1/folders/set_order
strip everything before 'folders', and this will be your method call
i.e: api.POST.folders.set_order(order='100:1','200:2','300:3')
'''