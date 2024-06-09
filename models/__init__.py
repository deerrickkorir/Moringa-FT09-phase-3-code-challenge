def __init__(self, id=None, title=None, content=None, author_id=None, magazine_id=None):
    if id is None and title is None and content is None and author_id is None and magazine_id is None:
        raise ValueError("Must provide either id, title, content, author_id, or magazine_id")

    if id is not None:
        self._id = id
        self._load_from_db()
    else:
        self._id = None
        self.title = title
        self.content = content
        self.author_id = author_id
        self.magazine_id = magazine_id
        self._save_to_db()
