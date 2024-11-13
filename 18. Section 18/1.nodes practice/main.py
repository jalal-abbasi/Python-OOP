from linked_list import LinkedList

my_linked_list = LinkedList()

my_linked_list.insert_node("Jalal")
my_linked_list.insert_node("Elaheh")
my_linked_list.insert_node("Ali")
my_linked_list.insert_node("Hamid")

my_linked_list.print_node_values()
print(my_linked_list.count_nodes_loop())
print(my_linked_list.count_nodes_recursive(my_linked_list.head))
print(my_linked_list.count_nodes_recursive_without_argument())


my_linked_list.print_node_values()
print(my_linked_list.delete_node("Hamid"))
my_linked_list.print_node_values()


print("===========")
print()
my_linked_list.print_reversed()
# Ali > Elaheh > Hamid > Jalal

