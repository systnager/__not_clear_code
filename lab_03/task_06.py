import sys
import re

def measure_memory(obj, seen=None):
    if seen is None:
        seen = set()
    if id(obj) in seen:
        return 0
    seen.add(id(obj))
    size = sys.getsizeof(obj)
    if isinstance(obj, dict):
        for k, v in obj.items():
            size += measure_memory(k, seen)
            size += measure_memory(v, seen)
    elif hasattr(obj, '__dict__'):
        size += measure_memory(obj.__dict__, seen)
    elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
        for i in obj:
            size += measure_memory(i, seen)
    return size

class LightNode:
    def outerHTML(self):
        raise NotImplementedError
    def innerHTML(self):
        raise NotImplementedError
    def render_text(self):
        raise NotImplementedError

class LightTextNode(LightNode):
    def __init__(self, text):
        self.text = text
    def outerHTML(self):
        return self.text
    def innerHTML(self):
        return self.text
    def render_text(self):
        return self.text

class LightElementFlyweight:
    def __init__(self, tag, display_type, closing_type, css_classes):
        self.tag = tag
        self.display_type = display_type
        self.closing_type = closing_type
        self.css_classes = css_classes

class FlyweightFactory:
    _flyweights = {}
    @classmethod
    def get_flyweight(cls, tag, display_type, closing_type, css_classes):
        key = (tag, display_type, closing_type, tuple(css_classes))
        if key not in cls._flyweights:
            cls._flyweights[key] = LightElementFlyweight(*key)
        return cls._flyweights[key]

class LightElementNode(LightNode):
    def __init__(self, flyweight):
        self.flyweight = flyweight
        self.children = []
    def add_child(self, node):
        self.children.append(node)
    def child_count(self):
        return len(self.children)
    def innerHTML(self):
        return "".join(child.outerHTML() for child in self.children)
    def outerHTML(self):
        classes = " ".join(self.flyweight.css_classes)
        open_tag = f"<{self.flyweight.tag}" + (f' class="{classes}"' if classes else "") + ">"
        if self.flyweight.closing_type == "self-closing":
            return open_tag + " />"
        return f"{open_tag}{self.innerHTML()}</{self.flyweight.tag}>"
    def render_text(self):
        content = "".join(child.render_text() for child in self.children)
        if self.flyweight.tag == "h1":
            return f"{content.upper()}\n{'=' * len(content)}\n"
        if self.flyweight.tag == "h2":
            return f"## {content}\n"
        if self.flyweight.tag == "blockquote":
            return "\n".join("    " + line for line in content.splitlines()) + "\n"
        if self.flyweight.tag == "p":
            return f"{content}\n"
        return "".join(child.render_text() for child in self.children)

def create_element(tag, display_type="block", closing_type="normal", css_classes=None):
    if css_classes is None:
        css_classes = []
    flyweight = FlyweightFactory.get_flyweight(tag, display_type, closing_type, css_classes)
    return LightElementNode(flyweight)

def transform_line_to_node(line, is_first=False):
    line = line.rstrip("\n")
    if is_first:
        node = create_element("h1")
        node.add_child(LightTextNode(line))
        return node
    if len(line.strip()) < 20 and line.strip():
        node = create_element("h2")
        node.add_child(LightTextNode(line.strip()))
        return node
    if re.match(r"^\s", line):
        node = create_element("blockquote")
        node.add_child(LightTextNode(line.strip()))
        return node
    node = create_element("p")
    node.add_child(LightTextNode(line.strip()))
    return node

if __name__ == "__main__":
    book_text = [
        "THE PROLOGUE",
        "When in disgrace with fortune and men's eyes, I all alone beweep my outcast state.",
        "Wishing me like to one more rich in hope, featured like him, like him with friends possessed.",
        "Desiring this man's art, and that man's scope, with what I most enjoy contented least;",
        "Yet in these thoughts myself almost despising, haply I think on thee, and then my state,",
        "Like to the lark at break of day arising from sullen earth, sings hymns at heaven's gate;",
        "For thy sweet love remembered such wealth brings that then I scorn to change my state with kings.",
        "   This indented line should appear as a blockquote, signifying special formatting.",
        "A brief note.",
        "The end of the sample text."
    ]
    root = create_element("div")
    for i, line in enumerate(book_text):
        if line.strip() == "":
            continue
        node = transform_line_to_node(line, is_first=(i == 0))
        root.add_child(node)
    html_content = "<!DOCTYPE html>\n<html>\n<head>\n<meta charset=\"utf-8\">\n<title>LightHTML Output</title>\n</head>\n<body>\n" + root.outerHTML() + "\n</body>\n</html>"
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    print("index.html created with the following content:")
    print(html_content)
    print("Memory usage:", measure_memory(root), "bytes")
