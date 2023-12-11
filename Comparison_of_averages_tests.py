from Comparison_of_averages import Comparison_of_averages


def test_correct_averages_of_lists(list_positive, list_negative):
    """Checking the average values of lists """
    comparison_lists = Comparison_of_averages(list_positive, list_negative)
    assert comparison_lists.get_averages() == (33, -33)

def test_for_nulls_list(list_positive, list_nulls):
    """ Checking a method with a null list"""
    comparison_lists = Comparison_of_averages(list_positive, list_nulls)
    assert comparison_lists.get_averages() == (33, 0)

def test_without_second_list(list_positive, list_none):
    """ Checking a method without a list"""
    comparison_lists = Comparison_of_averages(list_positive, list_none)
    assert comparison_lists.get_averages() == (33, 0)


def test_checking_list_average_when_first_list_greater(list_positive, list_negative, capsys):
    """Checking the message when the average value of the second list is greater than the first"""
    comparison_lists = Comparison_of_averages(list_positive, list_negative)
    comparison_lists.averages_comparatison()
    captured = capsys.readouterr()
    assert captured.out == 'Первый список имеет большее среднее значение\n'


def test_checking_list_average_when_second_list_greater(list_negative, list_positive, capsys):
    """Checking the message when the average value of the second list is greater than the first"""
    comparison_lists = Comparison_of_averages(list_negative, list_positive)
    comparison_lists.averages_comparatison()
    captured = capsys.readouterr()
    assert captured.out == 'Второй список имеет большее среднее значение\n'


def test_checking_list_average_when_lists_is_equal(list_positive, capsys):
    """Checking the message when the average value of the second list is greater than the first"""
    comparison_lists = Comparison_of_averages(list_positive, list_positive)
    comparison_lists.averages_comparatison()
    captured = capsys.readouterr()
    assert captured.out == 'Средние значения равны\n'
