from tasks import add

# Send task
result = add.delay(4, 5)

# Optional: wait for result
print("Task ID:", result.id)
print("Result:", result.get(timeout=30))