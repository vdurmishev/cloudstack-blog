resource "aws_db_subnet_group" "main" {
  name       = "blog-db-subnet-group"
  subnet_ids = var.private_subnet_ids

  tags = {
    Name = "blog-db-subnet-group"
  }
}

resource "aws_db_instance" "main" {
  identifier           = "blog-db"
  allocated_storage    = 20
  storage_type         = "gp2"
  engine               = "postgres"
  engine_version       = "15"
  instance_class       = "db.t3.micro"
  db_name              = var.db_name
  username             = var.db_username
  password             = var.db_password
  parameter_group_name = "default.postgres15"
  skip_final_snapshot  = true

  vpc_security_group_ids = [var.rds_sg_id]
  db_subnet_group_name   = aws_db_subnet_group.main.name

  tags = {
    Name = "blog-db-instance"
  }
}
