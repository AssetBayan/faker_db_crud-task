# faker_db_crud-task
# 📚 Library Management System (FastAPI + SQLite + Streamlit)

간단한 도서관 관리 시스템으로, FastAPI를 사용하여 CRUD API를 제공하고  
Streamlit 대시보드에서 실시간으로 책 데이터를 조회/추가/수정/삭제할 수 있습니다.

---

## 📂 Project Structure

faker_db_crud/
│
├── database.py # SQLite 연결 및 CRUD 기능
├── main.py # FastAPI 서버 (백엔드)
├── streamlit_app.py # Streamlit 대시보드 (프론트엔드)
└── library.db # SQLite 데이터베이스

yaml
코드 복사

---

## ⚙️ Setup & Install

필요한 라이브러리 설치:

pip install fastapi uvicorn streamlit requests pandas

yaml
코드 복사

---

## 🗄️ 1) Run FastAPI Backend

uvicorn faker_db_crud.main:app --reload --port 8000

yaml
코드 복사

API 문서:  
http://127.0.0.1:8000/docs

---

## 🖥️ 2) Run Streamlit Frontend

streamlit run faker_db_crud/streamlit_app.py

yaml
코드 복사

대시보드 실행:  
http://localhost:8501

---

## 🔌 API Endpoints

- `GET /books` — 모든 책 조회  
- `GET /books/{id}` — 특정 책 조회  
- `POST /books` — 새 책 생성  
- `PUT /books/{id}` — 책 정보 업데이트  
- `DELETE /books/{id}` — 책 삭제  

---

## 🧪 Features

- 📖 책 목록 조회  
- ➕ 새 책 등록  
- ✏️ 책 정보 수정  
- ❌ 책 삭제  
- 🔄 FastAPI ↔ Streamlit 연동  

---

## 👤 Author

**Asset Bayan**  
Kyungbok University • Big Data Department
