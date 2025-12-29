from fastapi import FastAPI, Depends, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from . import models, database
from .logging_config import get_logger

logger = get_logger(__name__)

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

templates = Jinja2Templates(directory="blog_app/templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request, category: str = None, db: Session = Depends(database.get_db)):
    query = db.query(models.Post)
    if category:
        query = query.filter(models.Post.category == category)
    posts = query.order_by(models.Post.created_at.desc()).all()
    return templates.TemplateResponse("index.html", {"request": request, "posts": posts, "current_category": category})

@app.get("/post/{post_id}", response_class=HTMLResponse)
def post_detail(request: Request, post_id: int, db: Session = Depends(database.get_db)):
    post = db.query(models.Post).filter(models.Post.id == post_id).first()
    return templates.TemplateResponse("post.html", {"request": request, "post": post})

@app.get("/create", response_class=HTMLResponse)
def create_form(request: Request):
    return templates.TemplateResponse("create.html", {"request": request})

@app.get("/about", response_class=HTMLResponse)
def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})

@app.post("/create")
def create_post(
    title: str = Form(...),
    category: str = Form("Journal"),
    summary: str = Form(None),
    content: str = Form(...),
    featured_image: str = Form(None),
    db: Session = Depends(database.get_db)
):
    logger.info(f"Creating new post: {title} in category {category}")
    db_post = models.Post(title=title, category=category, summary=summary, content=content, featured_image=featured_image)
    db.add(db_post)
    db.commit()
    logger.info(f"Post created successfully: {title}")
    return RedirectResponse(url="/", status_code=303)
