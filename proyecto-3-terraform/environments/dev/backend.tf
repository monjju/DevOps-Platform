terraform {
  backend "s3" {
    bucket         = "terraform-state-dev"
    key            = "dev/terraform.tfstate"
    region         = "eu-west-1"

    endpoint                    = "http://localhost:4566"
    access_key                  = "test"
    secret_key                  = "test"
    skip_credentials_validation = true
    skip_metadata_api_check     = true
    force_path_style            = true

    dynamodb_table     = "terraform-state-lock"
    dynamodb_endpoint  = "http://localhost:4566"
  }
}
