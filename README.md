# The Editorial - Multi-Tier Blog Platform

A modern, editorial-style blog platform built with FastAPI, PostgreSQL, and AWS. This project demonstrates a complete cloud-native architecture including containerization, infrastructure as code (Terraform), and CI/CD.

## 🚀 Features

- **Modern Editorial UI**: Clean, minimalist design inspired by premium lifestyle blogs.
- **FastAPI Backend**: High-performance Python backend with SQLAlchemy ORM.
- **Automated Seeding**: Populate your blog with high-quality content on startup.
- **Database Migrations**: Robust schema management using Alembic.
- **Containerized Architecture**: Docker-ready for both local development and production.
- **AWS Infrastructure**: Production-ready deployment using ECS Fargate, RDS, and S3.

---

## 💻 Local Development

Run the entire stack locally using Docker Compose.

### Prerequisites
- [Docker](https://www.docker.com/products/docker-desktop/) installed.

### Start the Application
```bash
docker compose up --build
```

The application will be available at [http://localhost:8000](http://localhost:8000).
- The database is automatically migrated and seeded with initial content.
- Use the "Create Post" button to add new stories.

---

## 🏗️ Architecture & Infrastructure

The project uses a simplified multi-tier architecture optimized for the AWS Free Tier:

- **Networking**: VPC with public subnets for all resources (ALB, ECS Tasks, and RDS).
- **Compute**: AWS ECS (Elastic Container Service) running on Fargate (Serverless).
- **Database**: AWS RDS (Relational Database Service) running PostgreSQL.
- **Storage**: AWS S3 for static assets and uploads.
- **Security**: Fine-grained security groups and IAM roles.

*Note: For Free Tier compatibility and simplicity, all resources are deployed in public subnets. This avoids NAT Gateway costs while maintaining ECR and internet connectivity for the tasks.*

The infrastructure is defined as Code in the `terraform/` directory.

---

## ☁️ AWS Deployment Guide

### 1. Initial Setup
1. **Configure AWS CLI**: Ensure you have AWS credentials configured locally.
2. **Create ECR Repository**: Create a repository in Amazon Elastic Container Registry (ECR) for the blog image.
3. **Push Initial Image**:
   ```bash
   aws ecr get-login-password --region <region> | docker login --username AWS --password-stdin <aws_account_id>.dkr.ecr.<region>.amazonaws.com
   docker build -t cloudstack-blog .
   docker tag cloudstack-blog:latest <aws_account_id>.dkr.ecr.<region>.amazonaws.com/cloudstack-blog:latest
   docker push <aws_account_id>.dkr.ecr.<region>.amazonaws.com/cloudstack-blog:latest
   ```

### 2. Provision Infrastructure
Navigate to the terraform directory:
```bash
cd terraform
terraform init
terraform plan
terraform apply
```

### 3. CI/CD Pipeline
The project includes a GitHub Actions pipeline (`.github/workflows/main.yml`) that automates:
1. **Build & Test**: Verifies the Python application.
2. **Docker Push**: Builds and pushes the latest image to Amazon ECR.
3. **Infrastructure Update**: Automatically runs `terraform apply`.
4. **ECS Deployment**: Updates the Fargate service to use the new image.

**Required GitHub Secrets:**
- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `DATABASE_URL` (Production endpoint)

---

## 🛠️ Tech Stack

- **Backend**: FastAPI (Python 3.11)
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Migrations**: Alembic
- **UI**: Jinja2 + Tailwind CSS
- **Infrastructure**: Terraform
- **Cloud**: AWS (ECS, RDS, S3, VPC)
- **CI/CD**: GitHub Actions
