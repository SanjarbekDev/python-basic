def see_methods(klass):
    return [method for method in dir(klass) if method.startswith('__') is False]