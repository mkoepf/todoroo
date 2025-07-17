# Manual Test Commands for Todo API

This file contains curl commands for manually testing each endpoint of the Todo API.
Make sure your FastAPI server is running (e.g., `uvicorn app:app --reload`) before executing these commands.

## 1. Create a Todo (POST /todos)

```bash
curl -X POST "http://localhost:8000/todos" \
  -H "Content-Type: application/json" \
  -d '{"id": 1, "title": "Buy groceries", "completed": false}'
```

```bash
curl -X POST "http://localhost:8000/todos" \
  -H "Content-Type: application/json" \
  -d '{"id": 2, "title": "Write documentation", "completed": true}'
```

```bash
curl -X POST "http://localhost:8000/todos" \
  -H "Content-Type: application/json" \
  -d '{"id": 3, "title": "Review code", "completed": false}'
```

## 2. Get All Todos (GET /todos)

```bash
curl -X GET "http://localhost:8000/todos"
```

## 3. Get a Specific Todo (GET /todos/{todo_id})

```bash
curl -X GET "http://localhost:8000/todos/1"
```

```bash
curl -X GET "http://localhost:8000/todos/2"
```

### Test with non-existent ID (should return 404)
```bash
curl -X GET "http://localhost:8000/todos/999"
```

## 4. Update a Todo (PUT /todos/{todo_id})

```bash
curl -X PUT "http://localhost:8000/todos/1" \
  -H "Content-Type: application/json" \
  -d '{"id": 1, "title": "Buy groceries - UPDATED", "completed": true}'
```

```bash
curl -X PUT "http://localhost:8000/todos/2" \
  -H "Content-Type: application/json" \
  -d '{"id": 2, "title": "Write comprehensive documentation", "completed": false}'
```

### Test with non-existent ID (should return 404)
```bash
curl -X PUT "http://localhost:8000/todos/999" \
  -H "Content-Type: application/json" \
  -d '{"id": 999, "title": "This should fail", "completed": false}'
```

## 5. Delete a Todo (DELETE /todos/{todo_id})

```bash
curl -X DELETE "http://localhost:8000/todos/1"
```

```bash
curl -X DELETE "http://localhost:8000/todos/2"
```

### Test with non-existent ID (should return 404)
```bash
curl -X DELETE "http://localhost:8000/todos/999"
```

## Complete Test Sequence

To test the full workflow, run these commands in order:

1. **Create some todos:**
```bash
curl -X POST "http://localhost:8000/todos" -H "Content-Type: application/json" -d '{"id": 1, "title": "Task 1", "completed": false}'
curl -X POST "http://localhost:8000/todos" -H "Content-Type: application/json" -d '{"id": 2, "title": "Task 2", "completed": false}'
```

2. **Get all todos:**
```bash
curl -X GET "http://localhost:8000/todos"
```

3. **Get a specific todo:**
```bash
curl -X GET "http://localhost:8000/todos/1"
```

4. **Update a todo:**
```bash
curl -X PUT "http://localhost:8000/todos/1" -H "Content-Type: application/json" -d '{"id": 1, "title": "Task 1 - COMPLETED", "completed": true}'
```

5. **Verify the update:**
```bash
curl -X GET "http://localhost:8000/todos/1"
```

6. **Delete a todo:**
```bash
curl -X DELETE "http://localhost:8000/todos/1"
```

7. **Verify deletion:**
```bash
curl -X GET "http://localhost:8000/todos"
```

## Notes

- Replace `localhost:8000` with your actual server address and port if different
- All requests assume the server is running with default FastAPI settings
- The API uses in-memory storage, so data will be lost when the server restarts
- Add `-v` flag to any curl command for verbose output to see response headers
- Add `-i` flag to include response headers in the output
