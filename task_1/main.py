"""Module demonstrates the usage of the LinkedList class."""

from linked_list import LinkedList


def main():
    """Main function for testing the LinkedList class."""

    llist = LinkedList()

    # Вставляємо вузли в початок
    llist.insert_at_beginning(5)
    llist.insert_at_beginning(10)
    llist.insert_at_beginning(15)

    # Вставляємо вузли в кінець
    llist.insert_at_end(20)
    llist.insert_at_end(25)

    # Друк зв'язного списку
    print("Зв'язний список:")
    llist.print_list()

    # Видаляємо вузол
    llist.delete_node(10)

    print("\nЗв'язний список після видалення вузла з даними 10:")
    llist.print_list()

    # Пошук елемента у зв'язному списку
    print("\nШукаємо елемент 15:")
    element = llist.search_element(15)
    if element:
        print(element.data)

    # Реверсування списку
    llist.reverse()
    print("\nЗв'язний список список після реверсування:")
    llist.print_list()

    # Сортування вставками
    llist.sort()
    print("\nЗв'язний список після сортування вставками:")
    llist.print_list()

    # Об'єднання двох відсортованих списків
    llist2 = LinkedList()
    llist2.insert_at_end(2)
    llist2.insert_at_end(30)
    llist2.insert_at_end(10)
    llist2.insert_at_end(15)
    llist2.sort()
    print("\nДругий відсортований список:")
    llist2.print_list()

    merged_list = llist.merge_sorted(llist2)
    print("\nОб'єднаний відсортований список:")
    merged_list.print_list()


if __name__ == "__main__":
    main()
