import json

# Sample Python object
data = {
    'name': 'John',
    'age': 30,
    'city': 'New York'
}

# Serialize Python object to JSON string
json_string = json.dumps(data)

# Display the serialized JSON string
print("Serialized JSON:", json_string)



# Sample JSON string
json_string = '{"name": "John", "age": 30, "city": "New York"}'

# Deserialize JSON string to Python object
data = json.loads(json_string)

# Display the deserialized Python object
print("Deserialized Python object:", data)
