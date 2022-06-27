from brownie import SimpleStorage, accounts


def test_deploy():
    # Arange
    account = accounts[0]
    # Act
    simple_storage = SimpleStorage.deploy({'from': account})
    starting_value = simple_storage.retrieve()
    expected = 0
    # Assert
    assert starting_value == expected


def test_updating_storage():
    # Arrenge
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({'from': account})
    # Act
    expected = 15
    simple_storage.store(expected, {'from': account})
    # Assert
    assert simple_storage.retrieve() == expected
