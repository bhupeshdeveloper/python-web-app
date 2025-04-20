# 🌐 python-web-app 🚀

A **containerized web application** built with **FastAPI** (Python) and a simple **HTML frontend**, designed for quick deployment using **Docker** and **Docker Compose**. Includes optional support for calling external **Django APIs**.

---

## 📦 Tech Stack

- 🐍 **Python 3.11**
- ⚡ **FastAPI**
- 🧾 **Jinja2** (HTML Templating)
- 🐳 **Docker & Docker Compose**
- 🔗 **Optional**: Django (external API integration)

---

## 🛠️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/bhupeshdeveloper/python-web-app.git
cd python-web-app
```

### 2️⃣ Build and Run with Docker Compose

```bash
docker-compose up --build
```

> 🌟 The app will be available at: [http://localhost:8000](http://localhost:8000)

---

## 📁 Project Structure

```
python-web-app/
│
├── app/
│   ├── main.py               # FastAPI entry point
│   ├── api/                  # API routes (optional)
│   └── templates/            # HTML templates
│       └── index.html
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## 🔌 API Endpoints

| Method | Endpoint            | Description                      |
|--------|---------------------|----------------------------------|
| GET    | `/`                 | Returns the HTML frontend        |
| GET    | `/api/todos`        | Simple JSON todos                |
| GET    | `/api/from-django`  | (Optional) Fetch from Django API |

---

## 🧪 Test the API

### Example: Call the `/api/greet` endpoint

```bash
curl http://localhost:8000/api/todos
```

**Expected response:**

```json
[{"id":1,"task":"Learn FastAPI","completed":false},{"id":2,"task":"Build a ToDo App","completed":true},{"id":3,"task":"Call API from HTML","completed":false}]
```

---

## 🔄 Optional: Django API Integration

You can configure the FastAPI backend to fetch data from a Django service running alongside, via the `/api/from-django` endpoint. Be sure to define the Django service in `docker-compose.yml`.

```python
import httpx

@app.get("/api/from-django")
async def from_django():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://djangoapi:8000/api/data")
        return response.json()
```

---

## 🧰 Development Tips

- 🛠️ Use **volumes** to enable hot reload during development.
- 🔄 To rebuild containers: `docker-compose up --build`
- 📜 Update dependencies in `requirements.txt` as needed.

---

## 🤝 Contributing

Contributions are welcome! 🎉  
If you'd like to make major changes, please open an issue first to discuss your ideas.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## ✨ Acknowledgements

A big thanks to the **FastAPI** and **Docker** communities for their amazing tools and documentation! ❤️

---

## 🚀 What's Next?

- Add a **Django dummy API** for testing integration.
- Generate **Swagger/OpenAPI docs** for the FastAPI endpoints.
- Set up **GitHub Actions** for CI/CD.

Feel free to suggest more features or improvements!