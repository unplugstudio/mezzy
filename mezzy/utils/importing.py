from mezzanine.utils.importing import import_dotted_path


def import_view(dotted_path):
    """
    Import a class or function based view by its dotted path.
    """
    obj = import_dotted_path(dotted_path)
    try:
        return obj.as_view()
    except AttributeError:
        return obj
