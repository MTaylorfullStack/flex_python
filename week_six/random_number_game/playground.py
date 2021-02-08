class request:
    def __init__(self):
        self.POST={}
        self.session={}
    def form_submission(self, key, data):
        self.POST[key]=data
        return self
    def store_in_session(self, key, value):
        self.session[key]=value
        return self

my_request = request()
my_request.form_submission('username', "Nohemy")
print(my_request.POST)

my_request.store_in_session('name', my_request.POST['username'])
print(my_request.session)