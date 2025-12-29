terraform {
  backend "s3" {
    bucket         = "cloudstack-blog-terraform-state"
    key            = "state/terraform.tfstate"
    region         = "us-east-1"
    encrypt        = true
    use_lockfile   = true
  }
}
