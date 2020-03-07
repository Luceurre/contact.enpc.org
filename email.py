class Email:
    FIELDS = ['name', 'email', 'message']
    def __init__(self, dict):
        self.msg = {}
        try:
            for field in self.FIELDS:
                if dict[field] != '':
                    self.msg[field] = dict[field]
                else:
                    raise Exception("Blank flield")
        except:
            raise Exception("Inexisting field")

    def __str__(self):
        str = ""
        for field in self.FIELDS:
            str += field + ": " + self.msg[field]

        return str