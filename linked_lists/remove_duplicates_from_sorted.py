#!/usr/bin/python 

from ds.LinkedList import LinkedList

def remove_dups(ll):
    if ll.head is None:
        return

    write = ll.head
    read_prev = write
    read = write.next_node

    # Init the map
    seen = {}
    seen[write.data] = True

    while read is not None:
        if read.data not in seen.keys():
            read_prev.next_node = None
            write.next_node = read
            write = read

        read_prev = write
        read = read.next_node
        seen[write.data] = True

    write.next_node = None

if __name__ == "__main__":
    l = LinkedList()
    l.insert_at_end(11)
    l.insert_at_end(11)
    l.insert_at_end(11)
    l.insert_at_end(21)
    l.insert_at_end(43)
    l.insert_at_end(43)
    l.insert_at_end(60)

    l.show()
    remove_dups(l)
    l.show()