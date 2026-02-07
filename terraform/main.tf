module "iam" {
  source       = "./modules/iam"
  project_name = var.project_name
}

module "dynamodb" {
  source       = "./modules/dynamodb"
  environment  = var.environment
  project_name = var.project_name
}

module "lambda" {
  source          = "./modules/lambda"
  project_name    = var.project_name
  environment     = var.environment
  lambda_role_arn = module.iam.lambda_role_arn
}

module "sns" {
  source       = "./modules/sns"
  project_name = var.project_name
}
