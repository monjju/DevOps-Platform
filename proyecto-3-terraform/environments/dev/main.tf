module "vpc" {
  source = "../../modules/vpc"

  project     = "devops-platform"
  environment = "dev"
  vpc_cidr    = "10.0.0.0/16"

  public_subnets  = ["10.0.1.0/24", "10.0.2.0/24"]
  private_subnets = ["10.0.3.0/24", "10.0.4.0/24"]
  azs             = ["eu-west-1a", "eu-west-1b"]
}

# EKS y RDS comentados — requieren AWS real
# module "eks" { ... }
# module "rds" { ... }
