from atlassian import Bitbucket


Bitbucket_apikey = 'HZU50BljxxkU038mPYhD6A07'
bitbucket = Bitbucket(
        url='https://api.bitbucket.org',
        username='isharma@zaloni.com',
        password=Bitbucket_apikey)
print(bitbucket.project_list())
