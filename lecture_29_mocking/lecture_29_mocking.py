from unittest.mock import Mock

mock = Mock()
print(mock)
print(mock.some_attr)
print(mock.some_method())

json = mock
print(json.dumps('fdgdfgdfg'))
print(json.loads('{"key": "value"}').get('key'))
print(json)

# json.loads('{"key": "value"}')
json.loads.assert_called()
json.loads.assert_called_once()
json.loads.assert_called_with('{"key": "value"}')
json.loads.assert_called_once_with('{"key": "value"}')

print(json.loads.call_count)
print(json.loads.call_args)
print(json.loads.method_calls)
