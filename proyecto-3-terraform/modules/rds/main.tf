# Subnet group — en qué subnets puede vivir RDS
resource "aws_db_subnet_group" "main" {
  name       = "${var.project}-${var.environment}-db-subnet"
  subnet_ids = var.private_subnet_ids

  tags = {
    Name        = "${var.project}-db-subnet-group"
    Environment = var.environment
  }
}

# Security Group — qué tráfico acepta RDS
resource "aws_security_group" "rds" {
  name   = "${var.project}-${var.environment}-rds-sg"
  vpc_id = var.vpc_id

  # Solo acepta conexiones desde dentro de la VPC
  ingress {
    from_port   = 5432
    to_port     = 5432
    protocol    = "tcp"
    cidr_blocks = [var.vpc_cidr]
  }

  # No permite salida a internet
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "${var.project}-rds-sg"
  }
}

# RDS PostgreSQL
resource "aws_db_instance" "main" {
  identifier        = "${var.project}-${var.environment}-db"
  engine            = "postgres"
  engine_version    = "14.7"
  instance_class    = var.instance_class
  allocated_storage = var.allocated_storage

  db_name  = var.db_name
  username = var.db_username
  password = var.db_password

  db_subnet_group_name   = aws_db_subnet_group.main.name
  vpc_security_group_ids = [aws_security_group.rds.id]

  # Seguridad
  publicly_accessible = false  # nunca expuesto a internet
  storage_encrypted   = true   # datos cifrados en disco

  # Backups
  backup_retention_period = 7  # 7 días de backups automáticos
  skip_final_snapshot     = true

  tags = {
    Name        = "${var.project}-rds"
    Environment = var.environment
  }
}
