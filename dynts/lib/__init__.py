try:
    from cts import *
    hasextensions = True
except ImportError, e:
    hasextensions = False
    from .fallback import *
else:
    import fallback
    
    
def makeskiplist(data = None, expected_size = 100, use_fallback = False):
    '''Create a new skiplist'''
    if hasattr(data,'__len__'):
        expected_size = max(expected_size,len(data))
    sl = fallback.skiplist if use_fallback else skiplist
    s = sl(expected_size)
    if data is not None:
        insert = s.insert
        for value in data:
            insert(value)
    return s
    
    