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
1. **Build & Test**: Verifies the Python application on every push.
2. **Terraform Plan**: On every push to `main`, it shows the infrastructure changes that would be applied.
3. **Manual Deployment**: To apply changes, go to the **Actions** tab, select the **CI/CD Pipeline**, and run it manually with the `apply` action. This will:
   - Build and push the latest Docker image to Amazon ECR.
   - Run `terraform apply` to update infrastructure and deploy the new image to ECS.
4. **Optional Cleanup**: A manual trigger to run `terraform destroy` via the same "Run workflow" menu.

**Required GitHub Secrets:**
- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `DB_PASSWORD`
- `S3_BUCKET_NAME`
- `DATABASE_URL` (Optional for local testing)

---

## 🗑️ Destroying Resources

To avoid incurring costs when you are not using the blog, you can destroy all AWS resources:

1. Go to the **Actions** tab in your GitHub repository.
2. Select the **CI/CD Pipeline** workflow on the left.
3. Click the **Run workflow** dropdown.
4. Select **destroy** from the "Action to perform" dropdown.
5. Click **Run workflow**.

This will execute `terraform destroy` and safely remove all provisioned infrastructure.

## 🛠️ Tech Stack

- **Backend**: FastAPI (Python 3.11)
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Migrations**: Alembic
- **UI**: Jinja2 + Tailwind CSS
- **Infrastructure**: Terraform
- **Cloud**: AWS (ECS, RDS, S3, VPC)
- **CI/CD**: GitHub Actions
