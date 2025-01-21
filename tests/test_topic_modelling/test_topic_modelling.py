import pytest

from src.topic_modelling import topic_modelling


@pytest.mark.parametrize("test_arr, expected", 
    [
        ([1, 2, 3, 4, 5], False), 
        ([1, 2, 3, 4, [5]], True), 
        ([], False),  
    ]
)
def test_contains_nests(test_arr, expected):
    assert topic_modelling.contains_nests(test_arr) == expected
    
@pytest.mark.parametrize("test_arr, expected", 
    [
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]), 
        ([1, 2, 3, 4, [5]], [1, 2, 3, 4, 5]), 
        ([[1], [2], [3], [4], [5]], [1, 2, 3, 4, 5]),
        ([[1, 2], [3, 4], 5], [1, 2, 3, 4, 5]),
        ([1, [2, [3, [4, [5]]]]], [1, 2, 3, 4, 5]),
        ([1, []], [1])
    ]
)
def test_flatten_list(test_arr, expected):
    assert topic_modelling.flatten_list(test_arr) == expected
    
@pytest.mark.parametrize(
    "all_responses, topic_array, current_topics, expected_all_responses, expected_current_topics",
    [
        ([], ['topic1', 'topic2'], [], [['topic1', 'topic2']], ['topic1', 'topic2']),
        ([], ['topic1', 'topic2'], ['topic1'], [['topic1', 'topic2']], ['topic1', 'topic2']),
        ([], [], ['topic1'], [[]], ['topic1']),
        (
            [['topic1']], 
            ['topic1', 'topic2', 'topic3', 'topic3'], 
            ['topic1'],
            [['topic1'], ['topic1', 'topic2', 'topic3', 'topic3']],
            ['topic1', 'topic2', 'topic3']
        )
    ]
)
def test_add_topics(
    all_responses,
    topic_array,
    current_topics, 
    expected_all_responses,
    expected_current_topics
):
    result = topic_modelling.add_topics(all_responses, topic_array, current_topics)
    
    assert result == (expected_all_responses, topic_array, expected_current_topics)
