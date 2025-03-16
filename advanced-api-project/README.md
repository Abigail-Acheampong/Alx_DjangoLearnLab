# Advanced API Project

## Book API Endpoints with Filtering, Searching, and Ordering

### **Filtering**
Users can filter books using:
- `?title=<book_title>`
- `?author=<author_name>`
- `?publication_year=<year>`

**Example:**
```sh
GET /books/?author=John Doe
