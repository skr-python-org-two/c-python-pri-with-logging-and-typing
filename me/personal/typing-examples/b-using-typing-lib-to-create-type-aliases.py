from typing import List , Tuple , Dict , Union


def typing_on_type_aliases():
    # Simplifying a complex list of tuples
    Coordinates = List[Tuple[int, int]]
    points: Coordinates = [(1, 2), (3, 4)]
    print("points value is :::: {0} {1}".format(points , type(points)))

    # Using Union for a variable that can be an int or a string
    IntOrString = Union[int, str]
    data: IntOrString = 42  # Could also be a string
    print("data value is :::: {0} {1}".format(data , type(data)))

    # For a dictionary with string keys and values that are either integers or floats
    ValueDict = Dict[str, Union[int, float]]
    my_dict: ValueDict = {"age": 30, "temperature": 98.6}
    print("my_dict value is :::: {0} {1}".format(my_dict , type(my_dict)))


def main():
    typing_on_type_aliases()


if __name__ == "__main__":
    main()


