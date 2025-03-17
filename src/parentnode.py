from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Tag is required for all ParentNodes")
        if self.children is None:
            raise ValueError("Children is required for all ParentNodes")
        result = f"<{self.tag}>"
        for child in self.children:
            result += f"{child.to_html()}"
        result += f"</{self.tag}>"
        return result
