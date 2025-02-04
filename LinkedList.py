# Carson Werner
# Circular Linked List For Students

class SlideNode:
    """"Slide Node class that stores slide_id and next slide"""
    def __init__(self, slide_id):
        self.slide_id = slide_id
        self.next = None

class CircularLinkedList:
    """Circular Linked List class that stores slides in a circular linked list and supports randomizing slides"""
    def __init__(self):
        self.head = None

    def iterate(self):
        current = current.next
    
    
    def nodes(self):
        nodes = []
        current = self.head
        while True:
            nodes.append(str(current.slide_id))
            current = current.next
            if current == self.head:
                break
        
        return nodes

    def append(self, slide_id):
        new_node = SlideNode(slide_id)
        if not self.head:
            self.head = new_node
            self.head.next = self.head  # circular link
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head  # circular link


def create_slides(number):
    slides = CircularLinkedList()
    for i in range(1, number+1):
        slides.append(i)
    return slides

if __name__ == "__main__": 
    slide_list = create_slides(20)
    print(slide_list.nodes())



# TEST CODE FOR SIM
# import random

# def simulate_sign_viewing(num_slides=20, display_time=20, view_duration=60, student_days=4, randomize=False):
#     # Create the circular linked list of slides
#     sign = CircularLinkedList()
#     for slide_id in range(1, num_slides + 1):
#         sign.append(slide_id)

#     # Randomize slides if needed
#     if randomize:
#         slides = list(range(1, num_slides + 1))
#         random.shuffle(slides)
#         sign = CircularLinkedList()
#         for slide_id in slides:
#             sign.append(slide_id)

#     # Simulate viewing
#     total_viewed = []
#     for day in range(student_days):
#         daily_duration = max(0, random.gauss(view_duration, 5))  # Normal distribution for view time
#         slides_seen = sign.display(daily_duration)
#         total_viewed.extend(slides_seen)

#     # Calculate unique slides seen
#     unique_slides = set(total_viewed)
#     percentage_seen = len(unique_slides) / num_slides * 100
#     return percentage_seen, unique_slides

# # Test Simulation
# percentage, slides_seen = simulate_sign_viewing(randomize=True)
# print(f"Percentage of slides seen: {percentage:.2f}%")
# print(f"Slides seen: {sorted(slides_seen)}")