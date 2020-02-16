def test_opencart_page(create_driver):
    create_driver['driver'].get(create_driver['url'])

    assert create_driver['driver'].current_url == create_driver['url']
