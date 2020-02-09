class ApiRouter(object): 
    def db_for_read(self, model, **hints):
        "Point all operations on api models to 'chinook'"
        if model._meta.app_label == 'api':
            return 'chinook'
        return 'default'

    def db_for_write(self, model, **hints):
        "Point all operations on api models to 'chinook'"
        if model._meta.app_label == 'api':
            return 'chinook'
        return 'default'
    
    def allow_relation(self, obj1, obj2, **hints):
        "Allow any relation if a both models in api app"
        if obj1._meta.app_label == 'api' and obj2._meta.app_label == 'api':
            return True
        # Allow if neither is api app
        elif 'api' not in [obj1._meta.app_label, obj2._meta.app_label]: 
            return True
        return False
    
    def allow_syncdb(self, db, model):
        if db == 'chinook' or model._meta.app_label == "api":
            return False # we're not using syncdb on our legacy database
        else: # but all other models/databases are fine
            return True