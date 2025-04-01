class LightNode:
    pass


class LightTextNode(LightNode):
    def __init__(self, text):
        self.text = text

    def outerHTML(self):
        return f"{self.text}"

    def innerHTML(self):
        return f"{self.text}"


class LightElementNode(LightNode):
    def __init__(self, tag, display_type, closing_type, css_classes):
        self.tag = tag
        self.display_type = display_type
        self.closing_type = closing_type
        self.css_classes = css_classes
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    def child_count(self):
        return len(self.children)

    def innerHTML(self):
        return "".join(child.outerHTML() for child in self.children)

    def outerHTML(self):
        class_str = " ".join(self.css_classes)
        if class_str:
            open_tag = f"<{self.tag} class=\"{class_str}\">"
        else:
            open_tag = f"<{self.tag}>"
        if self.closing_type == "self-closing":
            return open_tag[:-1] + " />"
        return f"{open_tag}{self.innerHTML()}</{self.tag}>"


if __name__ == "__main__":
    ul = LightElementNode("ul", "block", "normal", ["list"])
    li1 = LightElementNode("li", "block", "normal", [])
    li2 = LightElementNode("li", "block", "normal", [])
    li1.add_child(LightTextNode("Item 1"))
    li2.add_child(LightTextNode("Item 2"))
    ul.add_child(li1)
    ul.add_child(li2)
    print(f"outerHTML:\n{ul.outerHTML()}")
    print(f"innerHTML:\n{ul.innerHTML()}")
    print(f"Child count: {ul.child_count()}")
