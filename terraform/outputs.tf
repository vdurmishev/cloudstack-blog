output "app_url" {
  description = "The URL of the blog application"
  value       = "http://${module.ecs.alb_dns_name}"
}

output "rds_endpoint" {
  description = "The endpoint of the RDS instance"
  value       = module.rds.db_endpoint
}

output "s3_bucket" {
  description = "The name of the S3 bucket"
  value       = module.s3.bucket_name
}
