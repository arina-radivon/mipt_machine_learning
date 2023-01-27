""" Task 1 """


def double_print(line):
    if len(line) == 0:
        raise ValueError('empty string is not allowed')
    else:
        print(line)
        print(line)


""" Task 2 """


class ParseError(Exception):
    """ Error while parsing file """
    def __init__(self, *args, line_no=0, text=''):
        super().__init__(*args)
        self.line_no = line_no
        self.text = text

    def __str__(self):
        if self.line_no != 0 and self.text == '':
            return f'cannot parse text on line {self.line_no}'
        elif self.line_no == 0 and len(self.text) != 0:
            return f'cannot parse text: {repr(self.text)}'
        elif self.line_no != 0 and len(self.text) != 0:
            return f'cannot parse text on line {self.line_no}: {repr(self.text)}'
        else:
            return super().__str__()


if __name__ == '__main__':
    # TESTS
    double_print('Hello')
    # raise ParseError()
    # raise ParseError(line_no=10)
    raise ParseError(text='abc')
    # raise ParseError(line_no=10, text='...')
