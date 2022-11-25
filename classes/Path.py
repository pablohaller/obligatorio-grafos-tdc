class Path:
    def __init__(self, source="0", target="0", weight="0"):
        self.source = source
        self.target = target
        self.weight = weight

    def __str__(self):
        return f"Source: {self.source} | Target: {self.target} | Weight: {self.weight}"

    def __repr__(self):
        return f"{{ Source: {self.source} | Target: {self.target} | Weight: {self.weight} }}"
