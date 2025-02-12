# Carson Werner
# Circular Linked List For Students
# Note from carmine: some debuging done with assistance from copilot by me. namely the next_slide method


class SlideNode:
    """"Slide Node class that stores slide_id and next slide"""
    def __init__(self, slide_id):
        self.slide_id = slide_id
        self.next = None

class CircularLinkedList:
    """Circular Linked List class that stores slides in a circular linked list and supports randomizing slides"""
    def __init__(self):
        self.head = None
        self.current_slide = None  # This will track the current slide
    
    def next_slide(self):
        if self.current_slide is None:
            self.current_slide = self.head  # If it's the first call, start from the head
        else:
            self.current_slide = self.current_slide.next  # Move to the next slide
        return self.current_slide  # Return the current slide

    def get_nodes(self):
        nodes = []
        current = self.head
        while True:
            nodes.append(current.slide_id)  # Append slide_id for easy reading
            current = current.next
            if current == self.head:
                break
        return nodes

    def append(self, slide_id):
        new_node = SlideNode(slide_id)
        if not self.head:
            self.head = new_node
            self.head.next = self.head  # circular link
            self.current_slide = self.head  # Start at head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head  # circular link

def create_slides(number):
    slides = CircularLinkedList()
    for i in range(1, number + 1):
        slides.append(i)
    return slides