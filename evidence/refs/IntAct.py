class IntAct():

    def __init__(self, id=None):

        self.database = 'IntAct'
        self.id = id
        self._long_name = 'IntAct Molecular Interaction Database'
        self._web = 'https://www.ebi.ac.uk/intact/home'

    def __call__(self):

        tmp_dict = {
                'database' : 'IntAct',
                'id' : self.id
                }

        return tmp_dict

    def __repr__(self):

        return f'<IntAct: {self.id}>'

    def __str__(self):

        return f'IntAct: {self.id}'

    def __deepcopy__(self):

        return IntAct(id=self.id)

    def _webid(self):

        return self._web

    def _repr_html_(self):

        return f'<a href="{self._webid()}">{self.database}: {self.id}</a>'

