variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "vpc_cidr" {
  description = "VPC CIDR block"
  type        = string
  default     = "10.0.0.0/16"
}

variable "db_name" {
  description = "RDS database name"
  type        = string
  default     = "blogdb"
}

variable "db_username" {
  description = "RDS database username"
  type        = string
  default     = "postgres"
}

variable "db_password" {
  description = "RDS database password"
  type        = string
  sensitive   = true
}

variable "bucket_name" {
  description = "S3 bucket name for assets"
  type        = string
}

variable "container_image" {
  description = "Docker image for the blog app"
  type        = string
}
