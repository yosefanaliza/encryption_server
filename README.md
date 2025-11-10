# Encryption Server

A FastAPI-based encryption service providing classic cipher implementations with built-in request logging and analytics.

## Features

- **Caesar Cipher**: Encrypt/decrypt text using offset-based substitution
- **Rail Fence Cipher**: Encrypt/decrypt text using a zigzag pattern
- **Request Logging**: Automatic tracking of endpoint usage and performance metrics
- **Analytics**: Real-time statistics on request counts and handling times

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yosefanaliza/encryption_server.git
cd encryption_server
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Starting the Server

Run the server using:
```bash
python main.py
```

The server will start on `http://localhost:8000`

### API Documentation

Once the server is running, access the interactive API documentation at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## API Endpoints

### Caesar Cipher

**Endpoint:** `POST /caesar`

Encrypt or decrypt text using the Caesar cipher algorithm.

**Request Body:**
```json
{
  "text": "hello",
  "offset": 3,
  "mode": "encrypt"
}
```

**Response:**
```json
{
  "encrypted_text": "khoor"
}
```

**Parameters:**
- `text` (string): Text to encrypt/decrypt
- `offset` (integer): Number of positions to shift
- `mode` (string): Either "encrypt" or "decrypt"

---

### Rail Fence Cipher - Encrypt

**Endpoint:** `GET /fence/encrypt`

Encrypt text using the rail fence cipher.

**Query Parameters:**
- `text` (string): Text to encrypt

**Example:**
```
GET /fence/encrypt?text=hello
```

**Response:**
```json
{
  "encrypted_text": "hloel"
}
```

---

### Rail Fence Cipher - Decrypt

**Endpoint:** `POST /fence/decrypt`

Decrypt text using the rail fence cipher.

**Request Body:**
```json
{
  "text": "hloel"
}
```

**Response:**
```json
{
  "decrypted": "hello"
}
```

---

### Health Check

**Endpoint:** `GET /health`

Check if the server is running.

**Response:**
```json
{
  "status": "healthy"
}
```

## Project Structure

```
encryption-server/
├── main.py                 # Application entry point
├── requirements.txt        # Python dependencies
├── api/
│   ├── routes.py          # API route definitions
│   └── services/
│       ├── caesar.py      # Caesar cipher implementation
│       └── fence.py       # Rail fence cipher implementation
├── utils/
│   ├── endpoint_logger.py # Endpoint usage tracking
│   └── summery_logger.py  # Analytics and statistics
└── data/
    ├── endpoints_data.json # Endpoint metrics storage
    └── summery.json        # Analytics summary
```

## Logging & Analytics

The server automatically tracks:
- Total requests received per endpoint
- Average handling time per endpoint
- Highest/lowest request counts
- Highest/lowest handling times

Analytics data is stored in:
- `data/endpoints_data.json` - Detailed endpoint statistics
- `data/summery.json` - Summary of all endpoints

## Example Usage

### Python
```python
import requests

# Caesar encryption
response = requests.post('http://localhost:8000/caesar', json={
    'text': 'secret',
    'offset': 5,
    'mode': 'encrypt'
})
print(response.json())  # {'encrypted_text': 'xjhwjy'}

# Fence encryption
response = requests.get('http://localhost:8000/fence/encrypt?text=message')
print(response.json())  # {'encrypted_text': 'msaeesg'}
```

### cURL
```bash
# Caesar encryption
curl -X POST "http://localhost:8000/caesar" \
  -H "Content-Type: application/json" \
  -d '{"text":"hello","offset":3,"mode":"encrypt"}'

# Fence encryption
curl "http://localhost:8000/fence/encrypt?text=hello"
```

## Technologies Used

- **FastAPI** - Modern web framework for building APIs
- **Uvicorn** - ASGI server for running the application
- **Pydantic** - Data validation using Python type hints

## License

MIT License

## Author

Yosef Analiza
