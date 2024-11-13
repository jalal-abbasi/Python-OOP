from node import Node


class LinkedList:

    def __init__(self):
        self.head = None

    def insert_node(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node

        elif value <= self.head.value:
            new_node.next = self.head
            self.head = new_node

        else:
            previous = self.head
            runner = self.head.next

            while (runner is not None) and (value >= runner.value):
                previous = runner
                runner = runner.next

            previous.next = new_node
            new_node.next = runner

    def print_node_values(self):
        print()
        current = self.head

        if current is None:
            return "Empty"
        else:
            while current is not None:
                print(current.value, end=" ")
                current = current.next
        print()

    def count_nodes_loop(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next

        return count

    def count_nodes_recursive_without_argument(self):  # so the user do not need to insert an arguments in the method
        return self.count_nodes_recursive(self.head)

    def count_nodes_recursive(self, node):
        if node is None:
            return 0
        else:
            return 1 + self.count_nodes_recursive(node.next)

    def delete_node(self, target_value):
        # we have to consider three cases: first if the linked list is empty,
        # second if we are going to delete the head and third if we are going
        # to delete a node form the middle of the list (tail node inclusive)
        if self.head is None:
            return False  # this is a sign if the deletion operation has been performed correctly
        elif target_value == self.head.value:
            self.head = self.head.next
            return True
        else:
            previous = self.head
            runner = previous.next
            while (runner.value is not None) and (target_value > runner.value):
                # so while (we have not reached the end of the linked list)
                # and
                # (we have not reached the value of the target node)
                previous = runner
                runner = runner.next

            # once we have reached our target node, we have to delete it by replacing only the connectors!
            if (runner.value is not None) and (runner.value == target_value):
                # so we say if we are still in the link and the last runner position is on the target node, delete
                previous.next = runner.next
                return True  # as an indicator that we have done the deletion rightly
            else:
                return False


    def print_reversed(self):
        current = self.head
        num_nodes = self.count_nodes_loop()
        node_list = [0]*num_nodes
        for i in range(num_nodes):
            # node_list.append(current.value)
            if current is not None:
                node_list[num_nodes-1-i] = current.value
            current = current.next

        for i in range(num_nodes):
            print(node_list[i], end=" ")
        # node_list = node_list.sort(reverse=True)



