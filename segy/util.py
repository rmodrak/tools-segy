
import numpy as np

class Struct(dict):
    def __init__(self, *args, **kwargs):
        super(Struct, self).__init__(*args, **kwargs)
        self.__dict__ = self


class SeisStruct(Struct):
    """ Holds information about data
    """

    def __init__(self, nr=0, nt=0, dt=0., ts=0.,
                 sx=[], sy=[], sz=[],
                 rx=[], ry=[], rz=[],
                 nrec=[], nsrc=[]):
        super(SeisStruct, self).__init__(
            [['nr', nr], ['nt', nt], ['dt', dt], ['ts', ts],
             ['sx', sx], ['sy', sy], ['sz', sz],
             ['rx', rx], ['ry', ry], ['rz', rz],
             ['nrec', nrec], ['nsrc', nsrc]])


def sortrows(a, return_index=False, return_inverse=False):
    """ Sorts rows of numpy array
    """
    si = np.lexsort(a.T)
    if return_inverse:
        sj = np.argsort(si)

    if return_index and return_inverse:
        return a[si], si, sj
    elif return_index:
        return a[si], si
    elif return_inverse:
        return a[si], sj
    else:
        return a[si]


def uniquerows(a, sort_array=False, return_index=False):
    """ Finds unique rows of numpy array
    """
    if sort_array:
        if return_index:
            sa, si = sortrows(a, return_index=True)
        else:
            sa = sortrows(a)
    else:
        sa, sj = sortrows(a, return_inverse=True)
    ui = np.ones(len(sa), 'bool')
    ui[1:] = (np.diff(sa, axis=0) != 0).any(axis=1)

    if sort_array:
        ua = sa[ui]
        if return_index:
            ui = si[ui]
    else:
        ua = a[ui[sj]]
        if return_index:
            ui = np.array(range(len(ui)))[ui[sj]]

    if return_index:
        return ua, ui
    else:
        return ua

