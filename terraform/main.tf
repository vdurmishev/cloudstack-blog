provider "aws" {
  region = var.aws_region

  default_tags {
    tags = {
      Project   = "TheEditorial"
      ManagedBy = "Terraform"
    }
  }
}

module "vpc" {
  source   = "./modules/vpc"
  vpc_cidr = var.vpc_cidr
}

module "security" {
  source = "./modules/security"
  vpc_id = module.vpc.vpc_id
}

module "rds" {
  source            = "./modules/rds"
  public_subnet_ids = module.vpc.public_subnet_ids
  rds_sg_id         = module.security.rds_sg_id
  db_name           = var.db_name
  db_username       = var.db_username
  db_password       = var.db_password
}

module "s3" {
  source      = "./modules/s3"
  bucket_name = var.bucket_name
}

module "ecs" {
  source            = "./modules/ecs"
  vpc_id            = module.vpc.vpc_id
  public_subnet_ids = module.vpc.public_subnet_ids
  subnet_ids        = module.vpc.public_subnet_ids
  alb_sg_id         = module.security.alb_sg_id
  ecs_tasks_sg_id   = module.security.ecs_tasks_sg_id
  container_image   = var.container_image
  database_url      = "postgresql://${var.db_username}:${var.db_password}@${module.rds.db_endpoint}/${var.db_name}"
}
