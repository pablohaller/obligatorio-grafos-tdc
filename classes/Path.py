class Path:
    def __init__(self, source="0", target="0"):
        self.source = source
        self.target = target

    def __str__(self):
        return f"Source: {self.source} | Target: {self.target}"

    def __repr__(self):
        return f"{{ Source: {self.source} | Target: {self.target} }}"
