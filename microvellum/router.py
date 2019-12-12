class MVRouter:
    """
    A router to control all database operations on models in the
    mv application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read mv models go to microvellum.
        """
        if model._meta.app_label == 'mv':
            return 'microvellum'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write mv models go to microvellum.
        """
        if model._meta.app_label == 'mv':
            return 'microvellum'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the mv app is involved.
        """
        if obj1._meta.app_label == 'mv' or \
           obj2._meta.app_label == 'mv':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the mv app only appears in the 'microvellum'
        database.
        """
        if app_label == 'mv':
            return db == 'microvellum'
        return None
