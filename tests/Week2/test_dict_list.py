from src.Week2.Day8.Playing_w_dict_list import (get_every_nth_state,
                                                get_state_abbrev, get_longest_state,
                                                us_state_abbrev, states,
                                                combine_state_names_and_abbreviations)


def test_every_nth_state():
    expected = ['Massachusetts', 'Missouri', 'Hawaii', 'Vermont', 'Delaware']
    assert (get_every_nth_state() == expected)


def test_state_abbrev():
    expected = 'IL'
    assert (get_state_abbrev('Illinois') == expected)


def test_state_abbrev_not_found():
    expected = 'N/A'
    assert (get_state_abbrev('not_found_state') == expected)


def test_get_longest_abbrev():
    expected = ['North Carolina']
    assert (get_longest_state(us_state_abbrev) in expected)


def test_get_longest_state():
    expected = ['North Carolina']
    assert (get_longest_state(states) in expected)


def test_combine_states_abbrv():
    expected = ['AK',
                'AL',
                'AR',
                'AZ',
                'CA',
                'CO',
                'CT',
                'DE',
                'FL',
                'GA',
                'Arkansas',
                'Wyoming',
                'Louisiana',
                'North Dakota',
                'South Dakota',
                'Texas',
                'Illinois',
                'Iowa',
                'Michigan',
                'Delaware']
    assert (combine_state_names_and_abbreviations() == expected)
