class HTMLNode(object):


    def __init__(self=None, tag=None, value=None, children=None, props=None):

        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None:
            return ""
        return " ".join([f'{key}="{value}"' for key, value in self.props.items() if value is not None])
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
        
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if value is None:
            raise ValueError
        super().__init__(tag=tag, value=value, children=None, props=props)
        self.children = None
    
    def to_html(self):
        if self.tag is None:
            return self.value
        props_str = self.props_to_html()
        props_str = f" {props_str}" if props_str else ""
        return f"<{self.tag}{props_str}>{self.value}</{self.tag}>"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)
        self.value = None        
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("tag cannot be None")
        if self.children is None:
            raise ValueError("children cannot be None")
        props_str = self.props_to_html()
        props_str = f" {props_str}" if props_str else ""
        html = f"<{self.tag}{props_str}>"
        for child in self.children:
            html += child.to_html()
        html += f"</{self.tag}>"
        return html
    
    
        

               
