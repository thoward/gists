#!/usr/bin/env python


class Gist(dict):
    """ Simple Gist object. """

    def __init__(self, parsed_gist={}):
        """ Initialize gist object variables. """
        super(Gist, self).__init__(parsed_gist)
        if 'files' in parsed_gist:
            self.files = [GistFile(parsed_gist['files'][filename]) for
                    filename in parsed_gist['files']]
        else:
            self.files = []
            self['files'] = {}

    @property
    def url(self):
        return self['url']

    @property
    def description(self):
        return self['description']

    @description.setter
    def description(self, description):
        self['description'] = description

    @property
    def identifier(self):
        return self['id']

    @property
    def user(self):
        return self['user']['login']

    @property
    def public(self):
        return self['public']

    @public.setter
    def public(self, public):
        self['public'] = public

    def getFile(self, requested_filename):
        candidates = [gistfile for gistfile in self.files
                if gistfile.filename == requested_filename]
        if len(candidates) == 0:
            return None
        return candidates[0]

    def addFile(self, gistfile):
        self['files'][gistfile.filename] = gistfile


class GistFile(dict):

    def __init__(self, parsed_file={}):
        super(GistFile, self).__init__(parsed_file)

    @property
    def raw_url(self):
        return self['raw_url']

    @property
    def language(self):
        return self['language']

    @property
    def filename(self):
        return self['filename']

    @filename.setter
    def filename(self, filename):
        self['filename'] = filename

    @property
    def content(self):
        return self['content']

    @content.setter
    def content(self, content):
        self['content'] = content

    @property
    def mimetype(self):
        return self['type']

    @property
    def size(self):
        return self['size']
