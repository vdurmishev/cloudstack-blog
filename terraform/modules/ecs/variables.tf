variable "vpc_id" {
  type = string
}

variable "public_subnet_ids" {
  type = list(string)
}

variable "private_subnet_ids" {
  type = list(string)
}

variable "alb_sg_id" {
  type = string
}

variable "ecs_tasks_sg_id" {
  type = string
}

variable "container_image" {
  type = string
}

variable "database_url" {
  type = string
}
