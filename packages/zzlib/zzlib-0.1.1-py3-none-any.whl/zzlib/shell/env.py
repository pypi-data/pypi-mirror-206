import os


class PathListEnvVar(list):
    def __init__(self, envvar: str):
        self.envvar = envvar
        spec = os.environ.get(envvar, None)
        super().__init__(spec.split(os.pathsep) if spec else ())

    def __str__(self):
        absoluted = [str(i.absolute()) if isinstance(i, P) else str(i) for i in self]
        return os.pathsep.join(absoluted)

    def save(self):
        os.environ[self.envvar] = str(self)

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.save()
